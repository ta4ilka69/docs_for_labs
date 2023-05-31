ALTER TABLE answer_pulse DROP CONSTRAINT IF EXISTS answer_pulse_pulse_id_fkey;
ALTER TABLE answer_pulse DROP CONSTRAINT IF EXISTS answer_pulse_zone_id_fkey;
ALTER TABLE cosmic_body DROP CONSTRAINT IF EXISTS cosmic_body_type_id_fkey;
ALTER TABLE cosmic_body_zone DROP CONSTRAINT IF EXISTS cosmic_body_zone_obj_id_fkey;
ALTER TABLE destination DROP CONSTRAINT IF EXISTS destination_ship_id_fkey;
ALTER TABLE destination DROP CONSTRAINT IF EXISTS destination_zone_id_fkey;
ALTER TABLE energy_pulse DROP CONSTRAINT IF EXISTS energy_pulse_radar_id_fkey;
ALTER TABLE radar DROP CONSTRAINT IF EXISTS radar_ship_id_fkey;


DROP TRIGGER IF EXISTS check_coordinates_trigger ON spaceship;

DROP TABLE IF EXISTS answer_pulse;
DROP TABLE IF EXISTS destination;
DROP TABLE IF EXISTS cosmic_body_zone;
DROP TABLE IF EXISTS cosmic_body;
DROP TABLE IF EXISTS cosmic_type;
DROP TABLE IF EXISTS energy_pulse;
DROP TABLE IF EXISTS radar;
DROP TABLE IF EXISTS spaceship;

DROP SEQUENCE IF EXISTS answer_pulse_answer_id_seq;
DROP SEQUENCE IF EXISTS cosmic_body_obj_id_seq;
DROP SEQUENCE IF EXISTS cosmic_body_zone_zone_id_seq;
DROP SEQUENCE IF EXISTS cosmic_type_type_id_seq;
DROP SEQUENCE IF EXISTS destination_d_id_seq;
DROP SEQUENCE IF EXISTS energy_pulse_pulse_id_seq;
DROP SEQUENCE IF EXISTS radar_radar_id_seq;
DROP SEQUENCE IF EXISTS spaceship_ship_id_seq;