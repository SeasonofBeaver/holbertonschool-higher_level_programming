-- creates a table in which a unique ID
create table if not exists unique_id (
    id INT DEFAULT 1 UNIQUE,
    name VARCHAR(256)
);