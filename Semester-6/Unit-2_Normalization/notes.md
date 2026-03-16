# Unit 2 — Normalization
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