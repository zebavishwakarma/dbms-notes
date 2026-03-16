# Unit 1 — Introduction to DBMS
> RGPV CS-502 | Semester 5

---

## 1.1 What is a Database?

A **database** is an organized collection of interrelated data stored electronically. It is managed by a **Database Management System (DBMS)** — software that allows users to define, create, maintain, and control access to the database.

---

## 1.2 File System vs DBMS

| Feature | File System | DBMS |
|---|---|---|
| Data redundancy | High | Controlled (low) |
| Data inconsistency | Common | Avoided |
| Data sharing | Difficult | Easy |
| Data security | Weak | Strong (access control) |
| Crash recovery | Manual | Built-in |
| Data independence | None | Logical & physical |
| Query support | No | Yes (SQL) |

**Why DBMS over File System?**
- Eliminates data redundancy and inconsistency
- Provides concurrent access to multiple users
- Enforces integrity constraints automatically
- Supports backup and recovery

---

## 1.3 Advantages of DBMS

1. **Data independence** — changing storage structure doesn't affect application programs
2. **Data integrity** — constraints ensure accuracy and consistency
3. **Security** — user roles and access control
4. **Concurrency control** — multiple users can access data simultaneously without conflict
5. **Backup & Recovery** — automatic mechanisms for data safety
6. **Reduced redundancy** — centralized data, no duplication

---

## 1.4 Database System Architecture

### Three-Level Architecture (ANSI/SPARC)

```
┌─────────────────────────────┐
│     External Level          │  ← User views (View 1, View 2 ...)
├─────────────────────────────┤
│     Conceptual Level        │  ← Logical structure of entire DB
├─────────────────────────────┤
│     Internal Level          │  ← Physical storage (files, indexes)
└─────────────────────────────┘
```

- **External level**: How individual users see the data (views)
- **Conceptual level**: What data is stored & relationships (schema)
- **Internal level**: How data is physically stored (B-trees, hashing)

### Data Independence
- **Logical data independence** — changing conceptual schema without changing external schema
- **Physical data independence** — changing internal schema without changing conceptual schema

---

## 1.5 Data Models

A data model defines the logical structure of a database.

| Model | Description | Example |
|---|---|---|
| Hierarchical | Tree structure, parent-child | IBM IMS |
| Network | Graph structure, many-to-many | CODASYL |
| Relational | Tables (relations) | MySQL, PostgreSQL |
| Object-Oriented | Objects with attributes & methods | db4o |
| Entity-Relationship | ER diagram for design | Used in design phase |

**Most widely used:** Relational Model

---

## 1.6 Schemas and Instances

- **Schema**: The structure/blueprint of the database (does not change often)
- **Instance**: The actual data stored at a particular moment (changes frequently)

Example:
- Schema → `Student(RollNo, Name, Branch, CGPA)`
- Instance → `(101, "Riya", "CSE", 8.5)`

---

## 1.7 Entity-Relationship (ER) Model

### Basic Concepts

| Symbol | Meaning |
|---|---|
| Rectangle | Entity |
| Ellipse | Attribute |
| Diamond | Relationship |
| Double ellipse | Multivalued attribute |
| Dashed ellipse | Derived attribute |
| Double rectangle | Weak entity |

### Entity Types
- **Strong entity** — has its own primary key (e.g., Student)
- **Weak entity** — depends on another entity for identification (e.g., Dependent of Employee)

### Attributes
- **Simple** — atomic, cannot be divided (e.g., Age)
- **Composite** — can be divided (e.g., Name → FirstName + LastName)
- **Multivalued** — can have multiple values (e.g., PhoneNumbers)
- **Derived** — computed from other attributes (e.g., Age from DOB)
- **Key attribute** — uniquely identifies entity (e.g., RollNo)

### Relationships & Cardinality
- **1:1** — One student has one ID card
- **1:N** — One department has many employees
- **M:N** — Many students enroll in many courses

### Participation Constraints
- **Total participation** (double line) — every entity must participate
- **Partial participation** (single line) — some entities may not participate

---

## 1.8 Roles of DBA and Database Designer

### Database Administrator (DBA)
- Defines schemas and storage structure
- Manages user access and security
- Monitors performance and tunes the database
- Handles backup and recovery

### Database Designer
- Identifies data to be stored
- Designs the ER diagram and schema
- Communicates with end users to understand requirements

---

## 1.9 Key Terms to Remember

| Term | Meaning |
|---|---|
| Tuple | A single row in a relation |
| Attribute | A column in a relation |
| Relation | A table |
| Domain | Set of allowed values for an attribute |
| Degree | Number of attributes in a relation |
| Cardinality | Number of tuples in a relation |

---

## RGPV Previous Year Questions

1. What is DBMS? Compare file system with DBMS. *(Nov 2023)*
2. Explain the three-level architecture of DBMS with diagram. *(May 2022)*
3. Define entity, attribute, and relationship with examples. Draw an ER diagram for a university database. *(Nov 2022)*
4. Discuss the role of DBA and database designer. *(May 2023)*
5. Explain specialization and generalization in ER diagram with example. *(Nov 2021)*
