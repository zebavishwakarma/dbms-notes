# dbms-notes

![MySQL](https://img.shields.io/badge/MySQL-informational?style=flat) ![PostgreSQL](https://img.shields.io/badge/PostgreSQL-informational?style=flat) ![Oracle](https://img.shields.io/badge/Oracle-informational?style=flat) ![License](https://img.shields.io/badge/license-MIT-green?style=flat) ![RGPV](https://img.shields.io/badge/University-RGPV-blue?style=flat)

A comprehensive collection of DBMS concepts, notes, SQL scripts, and PL/SQL lab exercises aligned with the **RGPV B.Tech CS-502 syllabus** (Semesters 5 & 6).

---

## Table of contents

- [Folder structure](#folder-structure)
- [Semester 5](#semester-5)
- [Semester 6](#semester-6)
- [SQL Scripts](#sql-scripts)
- [Diagrams](#diagrams)
- [Prerequisites](#prerequisites)
- [How to use](#how-to-use)
- [Contributing](#contributing)
- [References](#references)
- [License](#license)

---

## Folder structure

```
dbms-notes/
│
├── Semester-5/
│   ├── Unit-1_Introduction-to-DBMS/         → DBMS basics, ER model, architecture
│   ├── Unit-2_Relational-Model/              → Keys, relational algebra, calculus
│   ├── Unit-3_SQL/                           → DDL, DML, joins, views, subqueries
│   ├── Unit-4_Transactions-and-Concurrency/  → ACID, 2PL, deadlock, recovery
│   └── Unit-5_Oracle-MySQL/                  → Oracle architecture, PL/SQL, triggers
│
├── Semester-6/
│   ├── Unit-1_Query-Processing-and-Optimization/  → Query pipeline, B+ trees, hash join
│   ├── Unit-2_Normalization/                       → 1NF to BCNF, FDs, decomposition
│   ├── Unit-3_Advanced-SQL/                        → CTEs, window functions, packages
│   ├── Unit-4_Distributed-Databases/               → Fragmentation, data warehousing
│   └── Unit-5_NoSQL-and-Emerging-Technologies/     → MongoDB, NoSQL types, temporal DB
│
├── sql-scripts/
│   ├── 01_schema_and_data.sql     → University DB schema with sample data
│   ├── 02_practice_queries.sql    → Practice queries for all units
│   └── 03_plsql_lab_exercises.sql → PL/SQL lab programs (Oracle)
│
└── diagrams/                      → ER diagrams, architecture diagrams
```

---

## Semester 5

| Unit | Topic | Key Concepts |
|------|-------|--------------|
| 1 | Introduction to DBMS | File system vs DBMS, 3-level architecture, ER model |
| 2 | Relational Model | Keys, relational algebra (σ, π, ⋈), relational calculus |
| 3 | SQL | DDL, DML, joins, subqueries, views, integrity constraints |
| 4 | Transactions & Concurrency | ACID, 2PL, deadlock, serializability, log-based recovery |
| 5 | Oracle/MySQL | SGA, background processes, PL/SQL, cursors, triggers |

---

## Semester 6

| Unit | Topic | Key Concepts |
|------|-------|--------------|
| 1 | Query Processing & Optimization | Parse → optimize → execute, B+ tree, hash join |
| 2 | Normalization | 1NF→BCNF, functional dependencies, lossless decomposition |
| 3 | Advanced SQL | Window functions, CTEs, packages, dynamic SQL |
| 4 | Distributed Databases | Fragmentation, replication, data warehousing, data mining |
| 5 | NoSQL & Emerging Tech | MongoDB, graph DB, temporal DB, multimedia DB |

---

## SQL Scripts

| File | Description |
|------|-------------|
| `01_schema_and_data.sql` | Creates university DB schema (Student, Course, Employee, Dept) with sample data |
| `02_practice_queries.sql` | 25+ practice queries covering all exam topics |
| `03_plsql_lab_exercises.sql` | PL/SQL: cursors, procedures, triggers, transactions (Oracle) |

---

## Diagrams

The `diagrams/` folder contains:
- ER diagram — University database
- Three-level architecture of DBMS
- B+ tree structure
- Transaction state diagram
- 2PL (Two-Phase Locking) diagram

---

## Prerequisites

- MySQL 8.0+ or Oracle 19c / PostgreSQL 14+
- Any SQL client: MySQL Workbench, DBeaver, SQL*Plus, pgAdmin
- Basic programming knowledge

---

## How to use

```bash
# Clone the repo
git clone https://github.com/zebavishwakarma/dbms-notes.git
cd dbms-notes

# Run the schema script in MySQL
mysql -u root -p < sql-scripts/01_schema_and_data.sql

# Then run practice queries
mysql -u root -p university_db < sql-scripts/02_practice_queries.sql
```

Each unit folder has a `notes.md` with:
- Concept explanations with examples
- Comparison tables
- Code snippets
- RGPV previous year questions

---

## Contributing

Pull requests are welcome! If you spot an error or want to add content:
1. Fork the repo
2. Create a branch: `git checkout -b add-unit-content`
3. Commit changes: `git commit -m 'Add: topic notes'`
4. Push and open a pull request

---

## References

- [Database System Concepts – Silberschatz, Korth & Sudarshan](https://db-book.com/)
- [NPTEL DBMS Lectures – IIT Bombay](https://nptel.ac.in/courses/106101169)
- [RGPV Notes – rgpvnotes.in](https://www.rgpvnotes.in/)
- [W3Schools SQL Tutorial](https://www.w3schools.com/sql/)
- [MongoDB Documentation](https://www.mongodb.com/docs/)

---

## License

[MIT](LICENSE)

Copyright © 2025 zebavishwakarma
