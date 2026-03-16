-- ============================================================
-- DBMS Notes — SQL Scripts
-- Schema: University Database
-- Compatible with: MySQL 8.0+ / Oracle 19c+
-- ============================================================

-- ----------------------------
-- Create Database
-- ----------------------------
CREATE DATABASE IF NOT EXISTS university_db;
USE university_db;

-- ----------------------------
-- Table: Department
-- ----------------------------
CREATE TABLE Department (
    DeptID      INT             PRIMARY KEY,
    DeptName    VARCHAR(50)     NOT NULL UNIQUE,
    Location    VARCHAR(50),
    HOD         VARCHAR(50)
);

-- ----------------------------
-- Table: Student
-- ----------------------------
CREATE TABLE Student (
    RollNo      INT             PRIMARY KEY,
    Name        VARCHAR(100)    NOT NULL,
    Branch      VARCHAR(10)     NOT NULL,
    CGPA        DECIMAL(3,2)    CHECK (CGPA BETWEEN 0.0 AND 10.0),
    DOB         DATE,
    Email       VARCHAR(100)    UNIQUE,
    DeptID      INT,
    FOREIGN KEY (DeptID) REFERENCES Department(DeptID)
        ON DELETE SET NULL
        ON UPDATE CASCADE
);

-- ----------------------------
-- Table: Course
-- ----------------------------
CREATE TABLE Course (
    CourseID    VARCHAR(10)     PRIMARY KEY,
    CourseName  VARCHAR(100)    NOT NULL,
    Credits     INT             DEFAULT 3,
    DeptID      INT,
    FOREIGN KEY (DeptID) REFERENCES Department(DeptID)
);

-- ----------------------------
-- Table: Enrollment
-- ----------------------------
CREATE TABLE Enrollment (
    RollNo      INT,
    CourseID    VARCHAR(10),
    Semester    INT,
    Grade       CHAR(2),
    PRIMARY KEY (RollNo, CourseID),
    FOREIGN KEY (RollNo)    REFERENCES Student(RollNo) ON DELETE CASCADE,
    FOREIGN KEY (CourseID)  REFERENCES Course(CourseID) ON DELETE CASCADE
);

-- ----------------------------
-- Table: Employee
-- ----------------------------
CREATE TABLE Employee (
    EmpID       INT             PRIMARY KEY,
    Name        VARCHAR(100)    NOT NULL,
    DeptID      INT,
    Salary      DECIMAL(10,2)   CHECK (Salary > 0),
    ManagerID   INT,
    JoinDate    DATE            DEFAULT (CURRENT_DATE),
    FOREIGN KEY (DeptID)    REFERENCES Department(DeptID),
    FOREIGN KEY (ManagerID) REFERENCES Employee(EmpID)
);

-- ----------------------------
-- Sample Data: Department
-- ----------------------------
INSERT INTO Department VALUES (1, 'Computer Science', 'Block A', 'Dr. Sharma');
INSERT INTO Department VALUES (2, 'Information Technology', 'Block B', 'Dr. Gupta');
INSERT INTO Department VALUES (3, 'Electronics', 'Block C', 'Dr. Verma');
INSERT INTO Department VALUES (4, 'Mechanical', 'Block D', 'Dr. Singh');

-- ----------------------------
-- Sample Data: Student
-- ----------------------------
INSERT INTO Student VALUES (101, 'Riya Sharma',   'CSE', 8.50, '2003-04-15', 'riya@mail.com',   1);
INSERT INTO Student VALUES (102, 'Arjun Patel',   'IT',  7.80, '2003-07-20', 'arjun@mail.com',  2);
INSERT INTO Student VALUES (103, 'Priya Gupta',   'CSE', 9.10, '2003-02-11', 'priya@mail.com',  1);
INSERT INTO Student VALUES (104, 'Rahul Verma',   'EC',  7.20, '2002-12-05', 'rahul@mail.com',  3);
INSERT INTO Student VALUES (105, 'Neha Joshi',    'CSE', 8.90, '2003-09-18', 'neha@mail.com',   1);
INSERT INTO Student VALUES (106, 'Vivek Singh',   'IT',  6.50, '2002-11-30', 'vivek@mail.com',  2);
INSERT INTO Student VALUES (107, 'Anjali Rao',    'ME',  7.60, '2003-06-22', 'anjali@mail.com', 4);
INSERT INTO Student VALUES (108, 'Kunal Mishra',  'CSE', 5.80, '2003-01-09', 'kunal@mail.com',  1);

-- ----------------------------
-- Sample Data: Course
-- ----------------------------
INSERT INTO Course VALUES ('CS401', 'Database Management System',  4, 1);
INSERT INTO Course VALUES ('CS402', 'Operating System',            4, 1);
INSERT INTO Course VALUES ('CS403', 'Computer Networks',           3, 1);
INSERT INTO Course VALUES ('IT401', 'Software Engineering',        3, 2);
INSERT INTO Course VALUES ('IT402', 'Web Technologies',            3, 2);
INSERT INTO Course VALUES ('EC401', 'Digital Electronics',         4, 3);

-- ----------------------------
-- Sample Data: Enrollment
-- ----------------------------
INSERT INTO Enrollment VALUES (101, 'CS401', 5, 'O');
INSERT INTO Enrollment VALUES (101, 'CS402', 5, 'A+');
INSERT INTO Enrollment VALUES (102, 'IT401', 5, 'A');
INSERT INTO Enrollment VALUES (103, 'CS401', 5, 'O');
INSERT INTO Enrollment VALUES (103, 'CS403', 5, 'A+');
INSERT INTO Enrollment VALUES (104, 'EC401', 5, 'B+');
INSERT INTO Enrollment VALUES (105, 'CS401', 5, 'A+');
INSERT INTO Enrollment VALUES (106, 'IT402', 5, 'B');

-- ----------------------------
-- Sample Data: Employee
-- ----------------------------
INSERT INTO Employee VALUES (1,  'Dr. Rajesh Sharma', 1, 95000, NULL,  '2010-07-01');
INSERT INTO Employee VALUES (2,  'Dr. Anita Gupta',   2, 90000, NULL,  '2012-08-15');
INSERT INTO Employee VALUES (3,  'Prof. Sunil Kumar', 1, 75000, 1,     '2015-01-10');
INSERT INTO Employee VALUES (4,  'Prof. Meena Rao',   1, 72000, 1,     '2016-03-20');
INSERT INTO Employee VALUES (5,  'Prof. Amit Tiwari', 2, 68000, 2,     '2018-07-05');
INSERT INTO Employee VALUES (6,  'Dr. Pooja Mehta',   3, 85000, NULL,  '2011-09-01');
INSERT INTO Employee VALUES (7,  'Prof. Ravi Nair',   3, 70000, 6,     '2017-02-14');
