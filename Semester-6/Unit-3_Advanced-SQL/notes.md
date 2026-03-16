# Unit 3 — Advanced SQL
> RGPV CS-502 | Semester 6

## 3.1 Window Functions
```sql
SELECT Name, Salary,
    RANK() OVER (ORDER BY Salary DESC) AS Rank,
    DENSE_RANK() OVER (ORDER BY Salary DESC) AS Dense_Rank,
    ROW_NUMBER() OVER (ORDER BY Salary DESC) AS Row_Num
FROM Employee;

-- Partition by department
SELECT Name, DeptID, Salary,
    RANK() OVER (PARTITION BY DeptID ORDER BY Salary DESC) AS Dept_Rank
FROM Employee;
```

## 3.2 Common Table Expressions (CTE)
```sql
WITH TopEarners AS (
    SELECT Name, Salary FROM Employee WHERE Salary > 50000
)
SELECT T.Name, D.DeptName
FROM TopEarners T JOIN Department D ON T.DeptID = D.DeptID;
```

## 3.3 Packages (Oracle)
```sql
CREATE OR REPLACE PACKAGE student_pkg AS
    PROCEDURE add_student(p_roll NUMBER, p_name VARCHAR2);
    FUNCTION get_grade(p_cgpa NUMBER) RETURN VARCHAR2;
END student_pkg;
/
```

## 3.4 Exception Handling
```sql
BEGIN
    UPDATE Student SET CGPA = 11 WHERE RollNo = 101;
EXCEPTION
    WHEN OTHERS THEN
        DBMS_OUTPUT.PUT_LINE('Error: ' || SQLERRM);
        ROLLBACK;
END;
/
```

## 3.5 Database Connectivity
```python
import mysql.connector
conn = mysql.connector.connect(
    host="localhost", user="root",
    password="password", database="university_db"
)
cursor = conn.cursor()
cursor.execute("SELECT * FROM Student WHERE Branch = 'CSE'")
for row in cursor.fetchall():
    print(row)
conn.close()
```

## RGPV Previous Year Questions
1. Explain window functions with examples. *(Nov 2023)*
2. What is a CTE? Write a recursive CTE for employee hierarchy. *(Nov 2023)*
3. Explain packages in PL/SQL. *(May 2022)*