# Data insert
INSERT INTO students (id, name, age, city)
VALUES (1, 'Rahul', 20, 'Delhi');


# Data select
SELECT * FROM students;


# Data update
UPDATE students
SET city = 'Mumbai'
WHERE id = 1;


# Data delete
DELETE FROM students
WHERE id = 1;
