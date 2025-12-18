#PHASE-1: WHERE, OPERATORS, FILTERING (MOST IMPORTANT)
1️⃣ WHERE Clause (Deep)

#Data filter karne ke liye.
#Comparison Operators
"""Operator	Meaning
=	equal
!= / <>	not equal
> <	greater / less
>= <=	greater/less equal"""

#-----------------------------------------------------------------------------------------------

#syntax:
SELECT column_name
FROM table_name
WHERE condition;

SELECT * FROM students WHERE age = 20;

SELECT * FROM students WHERE age != 20;

SELECT * FROM students WHERE age > 18;

SELECT * FROM students WHERE city = 'Delhi'; #ye hmesha string and string hmesha single quote me

#-----------------------------------------------------------------------------------------------

#Logical Operators AND - (Dono condition true honi chahiye)
SELECT * FROM students
WHERE age > 18 AND city = 'Delhi';

#OR (Koi ek condition true ho)
SELECT * FROM students
WHERE city = 'Delhi' OR city = 'Mumbai';

#IN -Jab OR baar-baar likhna pade, tab IN , WHERE city = 'Delhi' OR city = 'Mumbai' OR city = 'Pune'
SELECT * FROM students
WHERE city IN ('Delhi', 'Mumbai','Pune');

#NOT IN (Condition ka ulta)
SELECT * FROM students
WHERE city NOT IN ('Delhi');

#BETWEEN - same as WHERE age >= 18 AND age <= 25 , ⚠️ Numbers & Dates ke liye best
SELECT * FROM students
WHERE age BETWEEN 18 AND 25;

SELECT * FROM students
WHERE join_date BETWEEN '2023-01-01' AND '2023-12-31';
#-----------------------------------------------------------------------------------------------


#LIKE (Pattern Matching 🔥)
#Pattern	Meaning
A%	A se start
%a	a pe end
%a%	kahi bhi a
_a	2 letters, second a

SELECT * FROM students 
WHERE name LIKE 'A%';  #A% → A se start ✔️ Aman, Amit

SELECT * FROM students
WHERE name LIKE '%a';   #%a → a pe end ✔️ Neha, Pooja

SELECT * FROM students
WHERE name LIKE '%a%';  #%a% → kahi bhi a ✔️ Rahul, Aman, Sagar

#-----------------------------------------------------------------------------------------------

#7️⃣ WHERE + Multiple Filters (Real Example)
SELECT * FROM students
WHERE age BETWEEN 18 AND 25
AND city IN ('Delhi', 'Mumbai')
AND name LIKE 'A%';

#-----------------------------------------------------------------------------------------------
