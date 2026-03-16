# Unit 4 — Distributed Databases & Data Warehousing
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