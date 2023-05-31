INSERT INTO cosmic_type (name)
VALUES ('Type 1'),
       ('Type 2'),
       ('Type 3');

INSERT INTO cosmic_body (name, type_id, x_coordinate, y_coordinate, z_coordinate)
VALUES ('Cosmic Body 1', 1, 100, 100, 100),
       ('Cosmic Body 2', 2, -100, 500, 200),
       ('Cosmic Body 3', 3, 700, 800, 900);


INSERT INTO cosmic_body_zone (obj_id, radius)
VALUES (1, 15),
       (2, 60),
       (3, 65);

INSERT INTO spaceship (name, x_coordinate, y_coordinate, z_coordinate)
VALUES ('Spaceship 1', 90, 90, 90),
       ('Spaceship 2', -50, 450, 155),
       ('Spaceship 3', 640, 740, 830);


INSERT INTO radar (ship_id, signal_frequency, send_frequency)
VALUES (1, 1.23, 4.56),
       (2, 7.89, 0.12),
       (3, 3.45, 6.78);


INSERT INTO energy_pulse (radar_id, send_time)
VALUES (1, 123.45),
       (2, 678.90),
       (3, 234.56);



INSERT INTO answer_pulse (pulse_id, zone_id, returned)
VALUES (1, 1, true),
       (2, 2, false),
       (3, 3, true);

SELECT*FROM destination;