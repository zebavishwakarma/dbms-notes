# Unit 1 — Introduction to DBMS
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