# Unit 5 — Oracle / MySQL
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