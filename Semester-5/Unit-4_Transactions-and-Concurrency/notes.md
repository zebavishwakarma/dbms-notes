# Unit 4 — Transactions & Concurrency Control
> RGPV CS-502 | Semester 5

## 4.1 ACID Properties
| Property | Meaning |
|---|---|
| Atomicity | All or nothing |
| Consistency | DB remains consistent before and after |
| Isolation | Concurrent transactions don't interfere |
| Durability | Committed changes are permanent |

## 4.2 Transaction States
Active → Partially Committed → Committed
Active → Failed → Aborted

## 4.3 Serializability
- **Serial schedule** — transactions one after another
- **Serializable** — concurrent schedule equivalent to some serial schedule
- **Conflict serializable** — check using precedence graph (no cycle = serializable)

## 4.4 Two-Phase Locking (2PL)
- **Growing phase** — acquire locks, do not release
- **Shrinking phase** — release locks, do not acquire
- Guarantees conflict serializability

### Lock Types
| Lock | Description |
|---|---|
| Shared (S) | Read lock — multiple allowed |
| Exclusive (X) | Write lock — only one allowed |

## 4.5 Deadlock
- Occurs when transactions wait for each other in a cycle
- **Detection** — wait-for graph (cycle = deadlock)
- **Prevention** — Wait-Die, Wound-Wait schemes

## 4.6 Recovery
- **Log-based recovery** — record every operation
- **Undo** — restore old values on failure
- **Redo** — reapply changes after crash
- **Checkpoint** — reduce recovery time

## RGPV Previous Year Questions
1. Explain ACID properties with examples. *(Nov 2023)*
2. Explain conflict serializability and precedence graph. *(May 2022)*
3. Explain Two-Phase Locking and its variants. *(Nov 2022)*
4. What is deadlock? Explain Wait-Die and Wound-Wait. *(May 2023)*