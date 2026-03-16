# Unit 3 — SQL
> RGPV CS-502 | Semester 5

## 3.1 SQL Categories
| Category | Commands |
|---|---|
| DDL | CREATE, ALTER, DROP, TRUNCATE |
| DML | SELECT, INSERT, UPDATE, DELETE |
| DCL | GRANT, REVOKE |
| TCL | COMMIT, ROLLBACK, SAVEPOINT |

## 3.2 DDL
```sql
CREATE TABLE Student (
    RollNo   INT PRIMARY KEY,
    Name     VARCHAR(50) NOT NULL,
    Branch   VARCHAR(10),
    CGPA     DECIMAL(3,2) CHECK (CGPA BETWEEN 0 AND 10)
);
ALTER TABLE Student ADD Email VARCHAR(100);
DROP TABLE Student;
```

## 3.3 DML
```sql
INSERT INTO Student VALUES (101, 'Riya', 'CSE', 8.5);
SELECT * FROM Student WHERE Branch = 'CSE' ORDER BY CGPA DESC;
UPDATE Student SET CGPA = 9.0 WHERE RollNo = 101;
DELETE FROM Student WHERE CGPA < 5.0;
```

## 3.4 Joins
```sql
-- INNER JOIN
SELECT S.Name, D.DeptName FROM Student S
INNER JOIN Department D ON S.DeptID = D.DeptID;

-- LEFT JOIN
SELECT S.Name, D.DeptName FROM Student S
LEFT JOIN Department D ON S.DeptID = D.DeptID;
```

## 3.5 Aggregate Functions
```sql
SELECT Branch, COUNT(*), AVG(CGPA), MAX(CGPA), MIN(CGPA)
FROM Student
GROUP BY Branch
HAVING AVG(CGPA) > 7.5;
```

## 3.6 Subqueries
```sql
SELECT Name FROM Student
WHERE CGPA > (SELECT AVG(CGPA) FROM Student);
```

## 3.7 Views
```sql
CREATE VIEW CSE_Students AS
SELECT RollNo, Name, CGPA FROM Student WHERE Branch = 'CSE';
```

## RGPV Previous Year Questions
1. Write SQL queries for DDL and DML with examples. *(Nov 2023)*
2. Explain GROUP BY and HAVING with examples. *(May 2022)*
3. Write SQL for all types of JOINs. *(Nov 2022)*
4. What is a view? How is it created? *(May 2023)*