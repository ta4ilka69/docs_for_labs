CREATE TABLE spaceship (
    ship_id SERIAL PRIMARY KEY,
    name VARCHAR(50) NOT NULL,
    x_coordinate BIGINT,
    y_coordinate BIGINT,
    z_coordinate BIGINT
);

CREATE TABLE radar (
    radar_id SERIAL PRIMARY KEY,
    ship_id INTEGER REFERENCES spaceship(ship_id) ON DELETE RESTRICT,
    signal_frequency DECIMAL,
    send_frequency DECIMAL
);

CREATE TABLE energy_pulse (
    pulse_id SERIAL PRIMARY KEY,
    radar_id INTEGER DEFAULT -1 REFERENCES radar(radar_id) ON DELETE SET DEFAULT,
    send_time DECIMAL
);

CREATE TABLE cosmic_type (
    type_id SERIAL PRIMARY KEY,
    name VARCHAR(50)
);

CREATE TABLE cosmic_body (
    obj_id SERIAL PRIMARY KEY,
    name VARCHAR(50) NOT NULL,
    type_id INTEGER REFERENCES cosmic_type(type_id) ON UPDATE RESTRICT,
    x_coordinate BIGINT,
    y_coordinate BIGINT,
    z_coordinate BIGINT
);

CREATE TABLE cosmic_body_zone (
    zone_id SERIAL PRIMARY KEY,
    obj_id INTEGER REFERENCES cosmic_body(obj_id) ON DELETE SET NULL,
    radius INTEGER
);

CREATE TABLE destination (
    d_id SERIAL PRIMARY KEY,
    ship_id INTEGER REFERENCES spaceship(ship_id) ON UPDATE RESTRICT ON DELETE SET NULL,
    zone_id INTEGER REFERENCES cosmic_body_zone(zone_id) ON DELETE SET NULL
);

CREATE TABLE answer_pulse (
    answer_id SERIAL PRIMARY KEY,
    pulse_id INTEGER REFERENCES energy_pulse(pulse_id) ON DELETE NO ACTION,
    zone_id INTEGER REFERENCES cosmic_body_zone(zone_id) ON DELETE SET NULL,
    returned BOOLEAN
);

CREATE OR REPLACE FUNCTION check_coordinates()
RETURNS TRIGGER AS $$
BEGIN
    IF TG_OP = 'UPDATE' OR TG_OP = 'DELETE' THEN
        DELETE FROM destination
        WHERE ship_id = OLD.ship_id;
    END IF;

    IF TG_OP = 'UPDATE' OR TG_OP = 'INSERT' THEN
        INSERT INTO destination (ship_id, zone_id)
        SELECT NEW.ship_id, cz.zone_id
        FROM cosmic_body_zone cz
        INNER JOIN cosmic_body cb ON cz.obj_id = cb.obj_id
        WHERE ABS(cb.x_coordinate - NEW.x_coordinate) < cz.radius 
          AND ABS(cb.y_coordinate - NEW.y_coordinate) < cz.radius 
          AND ABS(cb.z_coordinate - NEW.z_coordinate) < cz.radius;
    END IF;

    RETURN NEW;
END;
$$ LANGUAGE plpgsql;

CREATE TRIGGER check_coordinates_trigger
AFTER INSERT OR UPDATE OF x_coordinate, y_coordinate, z_coordinate ON spaceship
FOR EACH ROW
EXECUTE FUNCTION check_coordinates();
SELECT*FROM destination;