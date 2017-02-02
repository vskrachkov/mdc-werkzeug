CREATE TABLE IF NOT EXISTS resource (
    id SERIAL PRIMARY KEY
);

CREATE TABLE IF NOT EXISTS process (
    id          SERIAL PRIMARY KEY,
    resource_id INTEGER REFERENCES resource (id)
);