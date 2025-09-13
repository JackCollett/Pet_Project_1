DROP TABLE IF EXISTS medias;

CREATE TABLE medias (
    id SERIAL PRIMARY KEY,
    web_url VARCHAR(255), 
    creator VARCHAR(255),
    rotation INTEGER, 
    brightness INTEGER,
    skew VARCHAR(255),
    gradient BOOLEAN,
    gradient_colors VARCHAR(255)
);

INSERT INTO medias (web_url, creator, rotation, brightness, skew, gradient, gradient_colors) VALUES ('www.unsplash.test1', 'Dr Doom', 0, 100, '1, 0, 0, 1, 0, 0', 'false', '#e66465, #000000');
INSERT INTO medias (web_url, creator, rotation, brightness, skew, gradient, gradient_colors) VALUES ('www.unsplash.test3', 'Dr Doom', 0, 100, '1, 0, 0, 1, 0, 0', 'false', '#e66465, #000000');
INSERT INTO medias (web_url, creator, rotation, brightness, skew, gradient, gradient_colors) VALUES ('www.unsplash.test2', 'Dr Doom', 0, 100, '1, 0, 0, 1, 0, 0', 'false', '#e66465, #000000');