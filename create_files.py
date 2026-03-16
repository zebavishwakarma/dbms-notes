import os

files = {}

files["Semester-5/Unit-1_Introduction-to-DBMS/notes.md"] = r"""# Unit 1 — Introduction to DBMS
> RGPV CS-502 | Semester 5

## 1.1 What is a Database?
A **database** is an organized collection of interrelated data stored electronically, managed by a **DBMS**.

## 1.2 File System vs DBMS
| Feature | File System | DBMS |
|---|---|---|
| Data redundancy | High | Controlled |
| Data inconsistency | Common | Avoided |
| Data sharing | Difficult | Easy |
| Security | Weak | Strong |
| Crash recovery | Manual | Built-in |

## 1.3 Three-Level Architecture (ANSI/SPARC)
- **External level** — User views
- **Conceptual level** — Logical structure
- **Internal level** — Physical storage

## 1.4 Data Independence
- **Logical** — change conceptual schema without affecting external
- **Physical** — change internal schema without affecting conceptual

## 1.5 ER Model
| Symbol | Meaning |
|---|---|
| Rectangle | Entity |
| Ellipse | Attribute |
| Diamond | Relationship |
| Double ellipse | Multivalued attribute |
| Dashed ellipse | Derived attribute |

### Cardinality
- 1:1 — One student has one ID card
- 1:N — One department has many employees
- M:N — Many students enroll in many courses

## 1.6 Keys
| Key | Description |
|---|---|
| Super key | Uniquely identifies a tuple |
| Candidate key | Minimal super key |
| Primary key | Chosen candidate key |
| Foreign key | References primary key of another relation |

## RGPV Previous Year Questions
1. What is DBMS? Compare file system with DBMS. *(Nov 2023)*
2. Explain three-level architecture with diagram. *(May 2022)*
3. Define entity, attribute, relationship. Draw ER diagram for university. *(Nov 2022)*
4. Discuss role of DBA and database designer. *(May 2023)*
"""

files["Semester-5/Unit-2_Relational-Model/notes.md"] = r"""# Unit 2 — Relational Model
> RGPV CS-502 | Semester 5

## 2.1 Keys
| Key Type | Description |
|---|---|
| Super key | Set of attributes uniquely identifying a tuple |
| Candidate key | Minimal super key |
| Primary key | Chosen candidate key (no NULL) |
| Foreign key | References primary key of another relation |

## 2.2 Integrity Constraints
1. **Domain** — values must belong to defined domain
2. **Entity integrity** — primary key cannot be NULL
3. **Referential integrity** — foreign key must match a primary key or be NULL

## 2.3 Relational Algebra Operators
| Operator | Symbol | Description |
|---|---|---|
| Selection | σ | Filter rows |
| Projection | π | Select columns |
| Union | ∪ | All tuples in R or S |
| Set Difference | − | Tuples in R not in S |
| Cartesian Product | × | Every combination |
| Natural Join | ⋈ | Join on common attributes |

### Examples
```
σ_Branch='CSE'(Student)         -- Select CSE students
π_Name,CGPA(Student)            -- Project Name and CGPA
Student ⋈ Department            -- Natural join
```

## 2.4 Relational Calculus
- **TRC**: { t | P(t) } — tuple variables
- **DRC**: { <x1,x2> | P(x1,x2) } — domain variables

## RGPV Previous Year Questions
1. Explain various types of keys with examples. *(Nov 2023)*
2. Write short notes on referential integrity and entity integrity. *(May 2022)*
3. Explain all relational algebra operators with examples. *(Nov 2022)*
4. Differentiate between natural join and equi join. *(Nov 2021)*
"""

files["Semester-5/Unit-3_SQL/notes.md"] = r"""# Unit 3 — SQL
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
"""

files["Semester-5/Unit-4_Transactions-and-Concurrency/notes.md"] = r"""# Unit 4 — Transactions & Concurrency Control
> RGPV CS-502 | Semester 5

## 4.1 ACID Properties
| Property | Meaning |
|---|---|
| Atomicity | All or nothing |
| Consistency | DB remains consistent before and after |
| Isolation | Concurrent transactions don't interfere |
| Durability | Committed changes are permanent |

## 4.2 Transaction States
Active → Partially Committed → Committed
Active → Failed → Aborted

## 4.3 Serializability
- **Serial schedule** — transactions one after another
- **Serializable** — concurrent schedule equivalent to some serial schedule
- **Conflict serializable** — check using precedence graph (no cycle = serializable)

## 4.4 Two-Phase Locking (2PL)
- **Growing phase** — acquire locks, do not release
- **Shrinking phase** — release locks, do not acquire
- Guarantees conflict serializability

### Lock Types
| Lock | Description |
|---|---|
| Shared (S) | Read lock — multiple allowed |
| Exclusive (X) | Write lock — only one allowed |

## 4.5 Deadlock
- Occurs when transactions wait for each other in a cycle
- **Detection** — wait-for graph (cycle = deadlock)
- **Prevention** — Wait-Die, Wound-Wait schemes

## 4.6 Recovery
- **Log-based recovery** — record every operation
- **Undo** — restore old values on failure
- **Redo** — reapply changes after crash
- **Checkpoint** — reduce recovery time

## RGPV Previous Year Questions
1. Explain ACID properties with examples. *(Nov 2023)*
2. Explain conflict serializability and precedence graph. *(May 2022)*
3. Explain Two-Phase Locking and its variants. *(Nov 2022)*
4. What is deadlock? Explain Wait-Die and Wound-Wait. *(May 2023)*
"""

files["Semester-5/Unit-5_Oracle-MySQL/notes.md"] = r"""# Unit 5 — Oracle / MySQL
> RGPV CS-502 | Semester 5

## 5.1 Oracle Architecture
- **SGA** — System Global Area (Shared Pool, Buffer Cache, Redo Log Buffer)
- **Background Processes** — DBWR, LGWR, CKPT, SMON, PMON

## 5.2 PL/SQL Block Structure
```sql
DECLARE
    v_name VARCHAR2(50);
BEGIN
    SELECT Name INTO v_name FROM Student WHERE RollNo = 101;
    DBMS_OUTPUT.PUT_LINE('Name: ' || v_name);
EXCEPTION
    WHEN NO_DATA_FOUND THEN
        DBMS_OUTPUT.PUT_LINE('Not found');
END;
/
```

## 5.3 Cursors
```sql
BEGIN
    FOR rec IN (SELECT RollNo, Name FROM Student) LOOP
        DBMS_OUTPUT.PUT_LINE(rec.RollNo || ' ' || rec.Name);
    END LOOP;
END;
/
```

## 5.4 Stored Procedure
```sql
CREATE OR REPLACE PROCEDURE update_cgpa(p_roll IN NUMBER, p_cgpa IN NUMBER) AS
BEGIN
    UPDATE Student SET CGPA = p_cgpa WHERE RollNo = p_roll;
    COMMIT;
END;
/
EXEC update_cgpa(101, 9.0);
```

## 5.5 Triggers
```sql
CREATE OR REPLACE TRIGGER check_cgpa
BEFORE INSERT OR UPDATE ON Student
FOR EACH ROW
BEGIN
    IF :NEW.CGPA < 0 OR :NEW.CGPA > 10 THEN
        RAISE_APPLICATION_ERROR(-20001, 'Invalid CGPA!');
    END IF;
END;
/
```

## RGPV Previous Year Questions
1. Explain Oracle architecture with SGA and background processes. *(Nov 2023)*
2. Write a PL/SQL block using cursors to display employee details. *(Nov 2022)*
3. Write a trigger that fires on INSERT and UPDATE after 7 PM. *(May 2023)*
"""

files["Semester-6/Unit-1_Query-Processing-and-Optimization/notes.md"] = r"""# Unit 1 — Query Processing & Optimization
> RGPV CS-502 | Semester 6

## 1.1 Query Processing Steps
SQL Query → Parser → Translator → Optimizer → Execution Engine → Results

## 1.2 Selection Algorithms
| Algorithm | Condition | Cost |
|---|---|---|
| Linear Scan | Any | b_r blocks |
| Binary Search | Ordered file | log2(b_r) |
| B+ Tree | Index on key | h_i + 1 |

## 1.3 Join Algorithms
| Algorithm | Description | Best For |
|---|---|---|
| Nested-Loop | For each r, scan all s | Small relations |
| Block Nested-Loop | Block-wise nested loop | Better buffer use |
| Sort-Merge | Sort both, then merge | Pre-sorted data |
| Hash Join | Hash smaller relation | Large equijoins |

## 1.4 Query Optimization Rules
1. Perform selections early (reduce tuples)
2. Perform projections early (reduce attributes)
3. Combine selections with Cartesian products → joins
4. Join smaller relations first

## 1.5 B+ Tree Index
- All data pointers in leaf nodes
- Leaf nodes linked for range queries
- Balanced — O(log n) search, insert, delete

## 1.6 Hashing
- **Static hashing** — fixed number of buckets
- **Dynamic hashing** — directory doubles on overflow

## RGPV Previous Year Questions
1. Explain query processing steps with diagram. *(Nov 2023)*
2. Explain B+ tree structure and operations. *(May 2023)*
3. Compare nested-loop join and hash join. *(Nov 2021)*
"""

files["Semester-6/Unit-2_Normalization/notes.md"] = r"""# Unit 2 — Normalization
> RGPV CS-502 | Semester 6

## 2.1 Why Normalize?
Eliminate anomalies:
- **Insertion anomaly** — can't insert without unrelated data
- **Deletion anomaly** — deleting causes unintended data loss
- **Update anomaly** — one fact stored in multiple places

## 2.2 Functional Dependency
X → Y means X uniquely determines Y.
- **Full FD** — Y depends on whole of X
- **Partial FD** — Y depends on part of composite key
- **Transitive FD** — X→Y and Y→Z, so X→Z

## 2.3 Normal Forms
### 1NF — Atomic values only
All attributes must have atomic (single) values. No repeating groups.

### 2NF — No partial dependencies
Must be 1NF + no non-key attribute depends on part of a composite key.

### 3NF — No transitive dependencies
Must be 2NF + no non-key attribute depends on another non-key attribute.

### BCNF — Every determinant is a superkey
Stricter than 3NF. For every X→Y, X must be a superkey.

### 4NF — No multi-valued dependencies
Must be BCNF + no multi-valued dependencies.

## 2.4 Summary Table
| NF | Eliminates |
|---|---|
| 1NF | Non-atomic values |
| 2NF | Partial dependencies |
| 3NF | Transitive dependencies |
| BCNF | All FD anomalies |
| 4NF | Multi-valued dependencies |

## RGPV Previous Year Questions
1. Explain 1NF, 2NF, 3NF, BCNF with examples. *(Nov 2023)*
2. What are insertion, deletion, update anomalies? *(May 2022)*
3. What is functional dependency? Explain Armstrong's axioms. *(Nov 2022)*
4. Difference between 3NF and BCNF. *(May 2023)*
"""

files["Semester-6/Unit-3_Advanced-SQL/notes.md"] = r"""# Unit 3 — Advanced SQL
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
"""

files["Semester-6/Unit-4_Distributed-Databases/notes.md"] = r"""# Unit 4 — Distributed Databases & Data Warehousing
> RGPV CS-502 | Semester 6

## 4.1 Distributed Database
Collection of logically related databases distributed over a network, managed by DDBMS.

## 4.2 Fragmentation
| Type | Description |
|---|---|
| Horizontal | Split rows across sites |
| Vertical | Split columns across sites |
| Mixed | Combination of both |

## 4.3 Replication
| Strategy | Description |
|---|---|
| Full | Entire DB at every site |
| No replication | Each fragment at one site |
| Partial | Some fragments replicated |

## 4.4 OLTP vs OLAP
| Feature | OLTP | OLAP |
|---|---|---|
| Purpose | Day-to-day operations | Analysis |
| Data | Current | Historical |
| Query | Simple, frequent | Complex, infrequent |
| Normalization | High | Low (star/snowflake) |

## 4.5 Data Warehouse
ETL = Extract, Transform, Load
- **Star schema** — fact table + dimension tables
- **Snowflake schema** — normalized dimension tables

## 4.6 Data Mining Tasks
| Task | Example |
|---|---|
| Classification | Spam detection |
| Clustering | Customer segmentation |
| Association Rules | Market basket analysis |
| Regression | Price prediction |

## RGPV Previous Year Questions
1. Explain horizontal and vertical fragmentation. *(Nov 2023)*
2. Differentiate OLTP and OLAP. *(May 2022)*
3. Explain star schema with diagram. *(Nov 2022)*
4. What is data mining? Explain classification and clustering. *(May 2023)*
"""

files["Semester-6/Unit-5_NoSQL-and-Emerging-Technologies/notes.md"] = r"""# Unit 5 — NoSQL & Emerging Technologies
> RGPV CS-502 | Semester 6

## 5.1 NoSQL vs SQL
| Feature | SQL | NoSQL |
|---|---|---|
| Schema | Fixed | Flexible |
| ACID | Full | BASE |
| Scalability | Vertical | Horizontal |
| Use case | Structured data | Big data, real-time |

## 5.2 Types of NoSQL
| Type | Example | Use Case |
|---|---|---|
| Key-Value | Redis, DynamoDB | Caching, sessions |
| Document | MongoDB | User profiles, catalogs |
| Column-Family | Cassandra, HBase | Time-series, analytics |
| Graph | Neo4j | Social networks, fraud |

## 5.3 MongoDB Basics
```javascript
// Insert
db.students.insertOne({ rollNo: 101, name: "Riya", branch: "CSE", cgpa: 8.5 })

// Find
db.students.find({ branch: "CSE" })
db.students.find({ cgpa: { $gt: 8.0 } })

// Update
db.students.updateOne({ rollNo: 101 }, { $set: { cgpa: 9.0 } })

// Delete
db.students.deleteOne({ rollNo: 101 })

// Aggregation
db.students.aggregate([
    { $match: { branch: "CSE" } },
    { $group: { _id: "$branch", avgCGPA: { $avg: "$cgpa" } } }
])
```

## 5.4 Temporal Databases
Stores data with time dimension.
- **Valid time** — when fact is true in real world
- **Transaction time** — when data was stored in DB
- **Bitemporal** — both valid and transaction time

## RGPV Previous Year Questions
1. Compare SQL and NoSQL databases. *(Nov 2023)*
2. Explain types of NoSQL databases with examples. *(May 2022)*
3. What is a temporal database? *(Nov 2022)*
4. Write MongoDB queries for CRUD and aggregation. *(May 2023)*
"""

files["sql-scripts/02_practice_queries.sql"] = r"""-- Practice SQL Queries
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
"""

files["sql-scripts/03_plsql_lab_exercises.sql"] = r"""-- PL/SQL Lab Exercises (Oracle)
-- RGPV CS-502 Lab Programs

-- Lab 6: Trigger for audit log
CREATE TABLE Student_Audit (
    AuditID    NUMBER GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
    RollNo     NUMBER, OldCGPA NUMBER, NewCGPA NUMBER,
    ModifiedOn DATE DEFAULT SYSDATE
);

CREATE OR REPLACE TRIGGER trg_student_audit
AFTER UPDATE OF CGPA ON Student
FOR EACH ROW
BEGIN
    INSERT INTO Student_Audit(RollNo, OldCGPA, NewCGPA)
    VALUES(:OLD.RollNo, :OLD.CGPA, :NEW.CGPA);
END;
/

-- Lab 7: Function for grade
CREATE OR REPLACE FUNCTION fn_get_grade(p_cgpa NUMBER) RETURN VARCHAR2 AS
BEGIN
    IF p_cgpa >= 9.0 THEN RETURN 'O';
    ELSIF p_cgpa >= 8.0 THEN RETURN 'A+';
    ELSIF p_cgpa >= 7.0 THEN RETURN 'A';
    ELSIF p_cgpa >= 6.0 THEN RETURN 'B+';
    ELSE RETURN 'F';
    END IF;
END;
/
SELECT RollNo, Name, CGPA, fn_get_grade(CGPA) AS Grade FROM Student;

-- Lab 8: Cursor to display employees
BEGIN
    FOR emp_rec IN (SELECT E.Name, E.Salary, D.DeptName
                    FROM Employee E JOIN Department D ON E.DeptID = D.DeptID
                    ORDER BY E.Salary DESC) LOOP
        DBMS_OUTPUT.PUT_LINE(emp_rec.Name || ' | ' || emp_rec.DeptName || ' | ' || emp_rec.Salary);
    END LOOP;
END;
/

-- Trigger: No DML after 7 PM
CREATE OR REPLACE TRIGGER trg_time_check
BEFORE INSERT OR UPDATE OR DELETE ON Student
BEGIN
    IF TO_NUMBER(TO_CHAR(SYSDATE,'HH24')) >= 19 THEN
        RAISE_APPLICATION_ERROR(-20001,'DML not allowed after 7 PM!');
    END IF;
END;
/

-- Trigger: Prevent duplicate RollNo
CREATE OR REPLACE TRIGGER trg_no_duplicate
BEFORE INSERT ON Student
FOR EACH ROW
DECLARE v_count NUMBER;
BEGIN
    SELECT COUNT(*) INTO v_count FROM Student WHERE RollNo = :NEW.RollNo;
    IF v_count > 0 THEN
        RAISE_APPLICATION_ERROR(-20002,'Duplicate RollNo: ' || :NEW.RollNo);
    END IF;
END;
/

-- Stored Procedure: Add student
CREATE OR REPLACE PROCEDURE sp_add_student(
    p_roll IN NUMBER, p_name IN VARCHAR2,
    p_branch IN VARCHAR2, p_cgpa IN NUMBER) AS
BEGIN
    INSERT INTO Student(RollNo, Name, Branch, CGPA) VALUES(p_roll, p_name, p_branch, p_cgpa);
    COMMIT;
    DBMS_OUTPUT.PUT_LINE('Added: ' || p_name);
EXCEPTION
    WHEN DUP_VAL_ON_INDEX THEN DBMS_OUTPUT.PUT_LINE('Duplicate RollNo!');
    WHEN OTHERS THEN ROLLBACK; DBMS_OUTPUT.PUT_LINE('Error: ' || SQLERRM);
END;
/
EXEC sp_add_student(109, 'Mohit Tiwari', 'CSE', 8.2);
"""

files["diagrams/README.md"] = """# Diagrams
SVG diagrams for all major DBMS topics — render directly on GitHub.

| File | Topic |
|------|-------|
| er-diagram-university.svg | ER Diagram |
| three-level-architecture.svg | DBMS Architecture |
| transaction-state-diagram.svg | Transaction States |
| bplus-tree.svg | B+ Tree Index |
| normalization-steps.svg | Normalization Flow |
"""

files[".gitignore"] = """.DS_Store
Thumbs.db
.vscode/
*.tmp
*.log
"""

# Create all files
for filepath, content in files.items():
    dirpath = os.path.dirname(filepath)
    if dirpath:
        os.makedirs(dirpath, exist_ok=True)
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content.strip())
    print(f"Created: {filepath}")

print("\nAll files created successfully!")
print(f"Total files: {len(files)}")