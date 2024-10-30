-- Show all cities with its id name and the state name ordered by their ID
SELECT cities.id, cities.name, states.name FROM cities
JOIN states ON cities.state_id = states.id
ORDER BY cities.id;