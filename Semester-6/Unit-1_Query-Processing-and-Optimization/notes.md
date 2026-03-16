# Unit 1 — Query Processing & Optimization
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