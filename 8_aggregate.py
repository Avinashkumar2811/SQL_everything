#AGGREGATE FUNCTIONS (DEEP & COMPLETE)
👉 Multiple rows ko combine karke ek single value deta hai

#1️⃣ COUNT() – Total rows ginna
#a) COUNT(*)

SELECT COUNT(*) FROM students;

✔️ Total rows
✔️ NULL bhi count hota hai


#b) COUNT(column_name)
SELECT COUNT(age) FROM students;

✔️ NULL ignore hota hai


#c) COUNT(DISTINCT)
SELECT COUNT(DISTINCT city) FROM students;

✔️ Unique cities


#-----------------------------------------------------------------------------------------------
#2️⃣ SUM() – Total nikalna
#👉 Sirf numeric column pe kaam karta hai

SELECT SUM(fees) FROM students;

❌ String column pe kaam nahi karega

#-----------------------------------------------------------------------------------------------
#3️⃣ AVG() – Average nikalna

SELECT AVG(age) FROM students;  #avg=sum/count

⚠️ NULL ignore hota hai

#-----------------------------------------------------------------------------------------------
#4️⃣ MIN() – Minimum value

SELECT MIN(age) FROM students;

✔️ Numbers
✔️ Dates
✔️ Alphabetical (strings)

#-----------------------------------------------------------------------------------------------
5️⃣ MAX() – Maximum value

SELECT MAX(salary) FROM employees;

#-----------------------------------------------------------------------------------------------
#-----------------------------------------------------------------------------------------------
#Aggregate with WHERE (VERY COMMON)

SELECT COUNT(*) 
FROM students
WHERE city = 'Delhi';

👉 Pehle filter → phir aggregate

#-----------------------------------------------------------------------------------------------
#Aggregate + GROUP BY (INTRO)

👉 Without GROUP BY → single result
👉 With GROUP BY → multiple results

#Example: City-wise student count
SELECT city, COUNT(*)
FROM students
GROUP BY city;

✔️ Har city ka count alag-alag


#Average age per city
SELECT city, AVG(age)
FROM students
GROUP BY city;

#-----------------------------------------------------------------------------------------------

#HAVING (Aggregate pe condition)
#👉 WHERE aggregate pe kaam nahi karta
SELECT city, COUNT(*)
FROM students
GROUP BY city
HAVING COUNT(*) > 2;

#-----------------------------------------------------------------------------------------------
#-----------------------------------------------------------------------------------------------

#WHERE vs HAVING (Crystal Clear)
WHERE	HAVING
Row filter	Group filter
Aggregate se pehle	Aggregate ke baad
COUNT allowed ❌	COUNT allowed ✅

#-----------------------------------------------------------------------------------------------
#-----------------------------------------------------------------------------------------------

#🔥 Real-Life Example (Interview Level)
Cities jaha avg age > 20 ho
SELECT city, AVG(age)
FROM students
GROUP BY city
HAVING AVG(age) > 20;

#🔥 Multiple Aggregates Together
SELECT 
  city,
  COUNT(*) AS total_students,
  AVG(age) AS avg_age,
  MIN(age) AS min_age,
  MAX(age) AS max_age
FROM students
GROUP BY city;

#-----------------------------------------------------------------------------------------------
#-----------------------------------------------------------------------------------------------

#🔥 DISTINCT (DEEP & COMPLETE)
👉 Duplicate values hata ke sirf UNIQUE values deta hai

#📌 Ye rows pe kaam karta hai, function nahi hai
⚠️ DISTINCT() ❌ galat
✔️ DISTINCT ✅ sahi

#-----------------------------------------------------------------------------------------------

#Basic Syntax
SELECT DISTINCT column_name FROM table_name;

#1️⃣ Single Column DISTINCT
SELECT DISTINCT city FROM students;

👉 Output:
Delhi
Mumbai
Pune
(agar 100 students ho, but sirf 3 cities)

#-----------------------------------------------------------------------------------------------

#2️⃣ Multiple Columns DISTINCT (Very Important 🔥)
#👉 Combination unique hoti hai
SELECT DISTINCT city, age FROM students;

#📌 Meaning:
Same city + same age ek baar hi aayega


#-----------------------------------------------------------------------------------------------

#3️⃣ DISTINCT with COUNT (Most Common Interview Use)
#Total unique cities
SELECT COUNT(DISTINCT city) FROM students;

✔️ Sirf unique city count hogi

#-----------------------------------------------------------------------------------------------

#4️⃣ DISTINCT with Aggregate Functions
#Unique salary ka sum
SELECT SUM(DISTINCT salary) FROM employees;

#Unique age ka average
SELECT AVG(DISTINCT age) FROM students;

#-----------------------------------------------------------------------------------------------

#5️⃣ DISTINCT + WHERE
SELECT DISTINCT city
FROM students
WHERE age > 18;

#👉 Pehle filter → phir DISTINCT

#-----------------------------------------------------------------------------------------------

#6️⃣ DISTINCT + ORDER BY
SELECT DISTINCT city
FROM students
ORDER BY city ASC;

⚠️ ORDER BY ka column SELECT me hona chahiye (mostly DBs me)

#-----------------------------------------------------------------------------------------------

#7️⃣ DISTINCT vs GROUP BY (Confusing part 🔥)
#DISTINCT
SELECT DISTINCT city FROM students;

#GROUP BY
SELECT city FROM students GROUP BY city;

#-----------------------------------------------------------------------------------------------

#👉 Output same, but:
DISTINCT	GROUP BY
Duplicate hataata	Group banata
Simple use	Aggregates ke liye
Faster (simple case)	Powerful


#📌 Interview line:
UNIQUE values chahiye → DISTINCT