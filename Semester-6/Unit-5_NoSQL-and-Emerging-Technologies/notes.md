# Unit 5 — NoSQL & Emerging Technologies
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