#1️⃣ ALTER
Purpose: Table ka structure badalne ke liye

#Kaam kya kar sakte hain?
Naya column add karna
Column delete karna
Column type change karna

#Example:
CREATE TABLE students (
    id INT PRIMARY KEY,
    name VARCHAR(50),
    age INT
);

#1. Column add karna
ALTER TABLE students ADD city VARCHAR(50);

#2. Column ka type change karna
ALTER TABLE students MODIFY age INT;

#3. Column delete karna
ALTER TABLE students DROP COLUMN city;


#Simple analogy:
Socho table ek form hai, ALTER se form me naye fields add / remove / change kar rahe ho.
