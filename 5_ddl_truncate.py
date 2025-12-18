# 3️⃣ TRUNCATE
Purpose: Table ka saara data delete karne ke liye, structure bacha ke

Example:
# Table ka saara data delete karna
TRUNCATE TABLE students;


#Important difference from DELETE:
DELETE se data row-by-row delete hota hai (slow)

TRUNCATE fast, poora table clear ho jata hai

Table structure, columns, constraints waise ke waise rahte hain

Analogy:
Socho almirah ka saara content nikal diya, lekin almirah waise ka waise hai.


🔹 Quick Comparison Table
Command	Kya karta hai	Data aur Structure
ALTER	Table modify karna	Structure change, data safe
DROP	Table / Database delete karna	Data + Structure dono gone
TRUNCATE	Table ka saara data delete	Structure safe, data gone


💡 Memory Trick (simple):
ALTER → change

DROP → destroy everything

TRUNCATE → empty table, keep structure

