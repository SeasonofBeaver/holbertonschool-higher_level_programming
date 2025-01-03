-- Select all cities in California ordered by ID
SELECT id, name FROM cities
WHERE state_id = (SELECT id FROM states WHERE name = "California")
ORDER BY cities.id;