-- lists all records in the table that have a name.
SELECT score, name
FROM second_table
WHERE name IS NOT NULL
ORDER BY score DESC;