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
    radar_id INTEGER DEFAULT -1 REFERENCES radar(radar_id)  ON DELETE SET DEFAULT,
    send_time DECIMAL
);

CREATE TABLE cosmic_type(type_id SERIAL PRIMARY KEY, name VARCHAR(50));

CREATE TABLE cosmic_body(
    obj_id SERIAL PRIMARY KEY,
    name VARCHAR(50) NOT NULL,
    type_id INTEGER REFERENCES cosmic_type(type_id) ON UPDATE RESTRICT,
    diameter INTEGER
);

CREATE TABLE cosmic_body_coordinates(
    obj_id INTEGER REFERENCES cosmic_body(obj_id) ON DELETE CASCADE,
    x_coordinate BIGINT,
    y_coordinate BIGINT,
    z_coordinate BIGINT,
    PRIMARY KEY (obj_id, x_coordinate, y_coordinate, z_coordinate)
);

CREATE TABLE moon_zone (
    zone_id SERIAL PRIMARY KEY,
    moon_id INTEGER REFERENCES cosmic_body(obj_id) ON DELETE SET NULL,
    x_coordinate BIGINT,
    y_coordinate BIGINT,
    z_coordinate BIGINT,
    radius INTEGER
);

CREATE TABLE destination (
    d_id SERIAL PRIMARY KEY,
    ship_id INTEGER REFERENCES spaceship(ship_id) ON UPDATE RESTRICT ON DELETE SET NULL,
    zone_id INTEGER REFERENCES moon_zone(zone_id) ON DELETE SET NULL
);

CREATE TABLE answer_pulse(
    answer_id SERIAL PRIMARY KEY,
    pulse_id INTEGER REFERENCES energy_pulse(pulse_id) ON DELETE NO ACTION,
    zone_id INTEGER REFERENCES moon_zone(zone_id) ON DELETE SET NULL,
    returned BOOLEAN
);

CREATE OR REPLACE FUNCTION check_coordinate_difference() RETURNS TRIGGER AS $$
DECLARE
    existing_coordinates cosmic_body_coordinates;
BEGIN
    SELECT INTO existing_coordinates
        x_coordinate, y_coordinate, z_coordinate
    FROM cosmic_body_coordinates
    WHERE obj_id <> NEW.obj_id;

    IF existing_coordinates IS NOT NULL THEN
        IF ABS(existing_coordinates.x_coordinate - NEW.x_coordinate) <= 1000 THEN
            RAISE EXCEPTION 'New object x_coordinate is within 1000 meters of existing objects.';
        END IF;

        IF ABS(existing_coordinates.y_coordinate - NEW.y_coordinate) <= 1000 THEN
            RAISE EXCEPTION 'New object y_coordinate is within 1000 meters of existing objects.';
        END IF;

        IF ABS(existing_coordinates.z_coordinate - NEW.z_coordinate) <= 1000 THEN
            RAISE EXCEPTION 'New object z_coordinate is within 1000 meters of existing objects.';
        END IF;
    END IF;

    RETURN NEW;
END;
$$ LANGUAGE plpgsql;

CREATE TRIGGER check_coordinate_trigger
BEFORE INSERT ON cosmic_body_coordinates
FOR EACH ROW
EXECUTE FUNCTION check_coordinate_difference();


INSERT INTO spaceship (name, x_coordinate, y_coordinate, z_coordinate)
VALUES ('Spaceship A', 1000000, 2000000, 3000000);

INSERT INTO radar (ship_id, signal_frequency, send_frequency)
VALUES (1, 1.5, 2.0);

INSERT INTO energy_pulse (radar_id, send_time)
VALUES (1, 5.7);


INSERT INTO cosmic_type (name)
VALUES ('Type A');

INSERT INTO cosmic_body (name, type_id, diameter)
VALUES ('Cosmic Body A', 1, 5000);
INSERT INTO cosmic_body_coordinates (obj_id, x_coordinate, y_coordinate, z_coordinate)
VALUES (1, 1000000, 2000000, 3000000);


INSERT INTO moon_zone (moon_id, x_coordinate, y_coordinate, z_coordinate, radius)
VALUES (1, 1000000, 2000000, 3000000, 500);

INSERT INTO destination (ship_id, zone_id)
VALUES (1, 1);

INSERT INTO answer_pulse (pulse_id, zone_id, returned)
VALUES (1, 1, true);