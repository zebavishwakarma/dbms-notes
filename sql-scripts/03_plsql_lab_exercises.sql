-- PL/SQL Lab Exercises (Oracle)
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