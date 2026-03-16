# Unit 2 — Relational Model
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