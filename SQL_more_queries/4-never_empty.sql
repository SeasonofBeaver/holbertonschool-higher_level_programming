-- creates a table in which the ID cannot be NULL
create table if not exists id_not_null (
    id INT DEFAULT 1,
    name VARCHAR(256)
);