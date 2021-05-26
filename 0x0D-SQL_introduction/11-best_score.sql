-- lists all records of the table second_table with a score >= 10
SELECT IF score >= 10, name FROM second_table ORDER BY score DESC, name;
