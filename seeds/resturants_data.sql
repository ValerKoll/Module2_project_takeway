-- The job of this file is to reset all of our important database tables.
-- And add any data that is needed for the tests to run.
-- This is so that our tests, and application, are always operating from a fresh
-- database state, and that tests don't interfere with each other.

-- First, we must delete (drop) all our tables
DROP TABLE IF EXISTS resturants;
DROP SEQUENCE IF EXISTS resturants_id_seq;

DROP TABLE IF EXISTS dishes;
DROP SEQUENCE IF EXISTS dishes_id_seq;

-- Then, we recreate them
CREATE SEQUENCE IF NOT EXISTS resturants_id_seq;
CREATE TABLE resturants (
    id SERIAL PRIMARY KEY,
    rest_name VARCHAR(255),
    cusine VARCHAR(255)
);

CREATE SEQUENCE IF NOT EXISTS dishes_id_seq;
CREATE TABLE dishes (
    id SERIAL PRIMARY KEY,
    dish_name VARCHAR(255),
    price INTEGER,
    cook_time INTEGER,
    rest_id INTEGER
);

-- Finally, we add any records that are needed for the tests to run
INSERT INTO resturants (rest_name, cusine) VALUES ('Kung-Po', 'Chinese');
INSERT INTO resturants (rest_name, cusine) VALUES ('Random', 'Turkey');
INSERT INTO resturants (rest_name, cusine) VALUES ('Pizza Express', 'Italian');

INSERT INTO dishes (dish_name, price, cook_time, rest_id) VALUES ('King prawn', 15, 20, 1);
INSERT INTO dishes (dish_name, price, cook_time, rest_id) VALUES ('Noodle green', 21, 11, 1);
INSERT INTO dishes (dish_name, price, cook_time, rest_id) VALUES ('Spicy rice', 8, 15, 1);
INSERT INTO dishes (dish_name, price, cook_time, rest_id) VALUES ('Green prawn', 14, 10, 1);
INSERT INTO dishes (dish_name, price, cook_time, rest_id) VALUES ('Chicken Kebab', 11, 25, 2);
INSERT INTO dishes (dish_name, price, cook_time, rest_id) VALUES ('Beef green', 13, 23, 2);
INSERT INTO dishes (dish_name, price, cook_time, rest_id) VALUES ('Orange Fires', 4, 8, 2);
INSERT INTO dishes (dish_name, price, cook_time, rest_id) VALUES ('Pizza roman', 10, 12, 3);
INSERT INTO dishes (dish_name, price, cook_time, rest_id) VALUES ('Hell pizza', 27, 12, 3);
INSERT INTO dishes (dish_name, price, cook_time, rest_id) VALUES ('Garlic bread', 10, 7, 3);
