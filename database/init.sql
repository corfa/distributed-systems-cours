CREATE DATABASE links;

\c links;

CREATE TABLE links (
    id SERIAL PRIMARY KEY,
    url TEXT NOT NULL,
    status INT
);
