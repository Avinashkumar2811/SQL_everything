#SQL (Structured Query Language) database se baat karne ki language hai.
"""Iska use hota hai:
Data store karna, Data nikalna (fetch), Data update / delete karna"""

#Examples of databases:
"""MySQL
PostgreSQL
SQLite"""

#Database → Table → Rows → Columns
"school - students - id_name_age_city"


#command to create a db = create databse db_naam;
CREATE DATABASE school;

#go into that databse = use db_naam
USE school;


#Table banana
CREATE TABLE students (
    id INT PRIMARY KEY AUTO_INCREMENT, #primary key = unique + not null
    name CHAR(5),  #'avi_ _'  -> size=5, name=avi but, total 5 characters hi rhgea, 2 extra spaces extra rhega
    age INT,
    city VARCHAR(5)     #'avi'  -> size=5, name=avi, toh bas 3 characters bnayega, extra space nahi lega
);


#data ko table me daalna
INSERT INTO students (name, age, city)
VALUES 
('Rahul', 20, 'Delhi'),
('Aman', 22, 'Mumbai'),
('Ajit', 24, 'Goa');






