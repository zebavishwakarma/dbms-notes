-- Practice SQL Queries
-- Run 01_schema_and_data.sql first
USE university_db;

-- Basic SELECT
SELECT * FROM Student;
SELECT Name, CGPA FROM Student WHERE Branch = 'CSE' ORDER BY CGPA DESC;
SELECT DISTINCT Branch FROM Student;

-- Aggregate Functions
SELECT Branch, COUNT(*) AS Total, ROUND(AVG(CGPA),2) AS Avg_CGPA
FROM Student GROUP BY Branch HAVING AVG(CGPA) > 7.5;

-- Joins
SELECT S.Name, D.DeptName
FROM Student S INNER JOIN Department D ON S.DeptID = D.DeptID;

SELECT S.Name, C.CourseName, E.Grade
FROM Student S
JOIN Enrollment E ON S.RollNo = E.RollNo
JOIN Course C ON E.CourseID = C.CourseID;

-- Subqueries
SELECT Name, CGPA FROM Student
WHERE CGPA > (SELECT AVG(CGPA) FROM Student);

SELECT Name FROM Student WHERE RollNo IN (
    SELECT E.RollNo FROM Enrollment E
    JOIN Course C ON E.CourseID = C.CourseID
    WHERE C.CourseName = 'Database Management System'
);

-- Top 3 students
SELECT Name, Branch, CGPA FROM Student ORDER BY CGPA DESC LIMIT 3;

-- Second highest CGPA
SELECT MAX(CGPA) AS Second_Highest FROM Student
WHERE CGPA < (SELECT MAX(CGPA) FROM Student);

-- Students not enrolled in any course
SELECT S.Name, S.Branch FROM Student S
WHERE S.RollNo NOT IN (SELECT DISTINCT RollNo FROM Enrollment);