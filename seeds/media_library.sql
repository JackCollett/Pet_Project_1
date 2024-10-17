DROP TABLE IF EXISTS medias;

CREATE TABLE medias (
    id SERIAL PRIMARY KEY,
    web_url VARCHAR(255)
);

INSERT INTO medias (web_url) VALUES ('www.unsplash.test1');
INSERT INTO medias (web_url) VALUES ('www.unsplash.test2');
INSERT INTO medias (web_url) VALUES ('www.unsplash.test3');