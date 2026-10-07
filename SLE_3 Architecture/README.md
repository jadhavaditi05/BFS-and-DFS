# SLE-3: Architectural Design – BFS and DFS Graph Search System

## Course Information

- **Course:** 02AML204 – Introduction to Artificial Intelligence
- **Activity:** SLE-3 – Architectural Design (Full C4 Model)
- **Name:** Aditi Tanaji Jadhav
- **PRN:** 25UAM103
- **Division:** B
- **Date:** 05-10-2026

---

## 1. System Overview

The **BFS and DFS Graph Search System** takes a graph, a start node, and a goal node as input. It performs graph searching using **Breadth-First Search (BFS)** and **Depth-First Search (DFS)**.

The system measures the number of nodes expanded and the execution time of the search algorithms.

This architectural design represents the system using the four levels of the **C4 Model**:

1. C1 – Context Model
2. C2 – Container Model
3. C3 – Component Model
4. C4 – Code Level

---

## 2. C1 – Context Model

The Context Model shows the system at the highest level.

The user provides:

- Graph
- Start Node
- Goal Node

The BFS and DFS Search System processes the input and returns the search result, including:

- Nodes Expanded
- Runtime

### C1 Diagram

> Add the C1 Context Diagram here.

---

## 3. C2 – Container Model

The Container Model shows the major parts of the system.

### Main Containers

- **Input Module** – accepts the graph, start node, and goal node.
- **Search Engine** – performs BFS or DFS.
- **Visited Set** – keeps track of visited nodes and prevents repeated processing.
- **Output Module** – displays nodes expanded and runtime.

### C2 Diagram

> Add the C2 Container Diagram here.

---

## 4. C3 – Component Model

The Component Model shows the internal components of the Search Engine.

### Components

- **Frontier (Queue / Stack)** – BFS uses a queue, while DFS uses a stack.
- **Explored Set** – stores nodes that have already been explored.
- **Goal Test** – checks whether the current node is the goal.
- **Path Builder** – constructs the final search path.

### C3 Diagram

> Add the C3 Component Diagram here.

---

## 5. C4 – Code Level

The Code Level shows the important elements of the BFS and DFS implementation.

### Main Code Elements

| Element | Purpose |
|---|---|
| `graph` | Stores the graph structure |
| `bfs()` | Performs Breadth-First Search |
| `dfs()` | Performs Depth-First Search |
| `visited` | Stores already visited nodes |
| `nodes_expanded` | Counts expanded nodes |

### C4 Diagram

> Add the C4 Code-Level Diagram here.

---

## 6. Design Decisions

The following design decisions were made:

- The same graph is used for BFS and DFS for fair comparison.
- BFS uses a **queue** as its frontier.
- DFS uses a **stack** as its frontier.
- A visited set is used to avoid repeated processing of nodes.
- The system is kept simple for algorithmic performance analysis.

---

## 7. AI Contribution

ChatGPT was used to:

- Understand the C4 architectural model.
- Organize the system into C1, C2, C3, and C4 levels.
- Prepare the structure of the architectural diagrams.
- Assist in organizing the SLE-3 documentation.

The BFS and DFS implementation, graph creation, experiments, runtime measurements, profiling using **py-spy**, comparison, and final project work were performed as part of the project.

---

## 8. Conclusion

The C4 model represents the BFS and DFS Graph Search System at different levels of detail.

- **C1** shows the overall system and its interaction with the user.
- **C2** shows the major system containers.
- **C3** shows the internal components of the search engine.
- **C4** shows the important code-level elements.

BFS and DFS have a similar overall structure, but their main difference is the frontier: **BFS uses a queue, while DFS uses a stack**. This difference can affect their search behavior and performance.