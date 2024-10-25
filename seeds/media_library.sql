DROP TABLE IF EXISTS medias;

CREATE TABLE medias (
    id SERIAL PRIMARY KEY,
    web_url VARCHAR(255), 
    rotation INTEGER, 
    brightness INTEGER
);

INSERT INTO medias (web_url, rotation, brightness) VALUES ('www.unsplash.test1', 0, 1);
INSERT INTO medias (web_url, rotation, brightness) VALUES ('www.unsplash.test2', 0, 1);
INSERT INTO medias (web_url, rotation, brightness) VALUES ('www.unsplash.test3', 0, 1);