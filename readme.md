# Distributed Snapshot Simulator

A tiny Python project that simulates the **Chandy-Lamport Snapshot Algorithm** — a classic way for distributed systems to capture a consistent global state without a shared clock.

This was built as a mini-project for the **Distributed Computing** subject.

---

## What It Does

The simulator runs **3 processes (P1, P2, P3)** arranged in a **ring topology** (P1 → P2 → P3 → P1). One process starts a snapshot, marker messages travel around the ring, and every process records its own local state plus any in-transit messages on its incoming channel.

At the end, the program prints a **consistent global snapshot** — meaning no message is lost or counted twice.

---

## Why This Project

In a distributed system:
- There is no shared memory
- There is no shared clock
- Messages are always in transit

So how do you take a clean "photo" of the whole system at one moment?  
That's exactly what the Chandy-Lamport algorithm solves. This project is a small, hands-on simulation of that idea.

---

## Algorithm in 4 Lines

1. Any process can start the snapshot.
2. It records its own state and sends a **marker** to its neighbours.
3. When a process gets a marker for the first time, it records its state and forwards the marker.
4. Any application message that arrives **after** the marker is stored as **channel state**.

---

## Files
