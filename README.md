# Project Overview

This project is meant to track and practice the progress of data structures and algorithms.

## A bit about Data Structures and Algorithms

In DSA, to solve a problem, first we need to understand problem statement & which kind of paradigm/type it can be solved. Common paradigms include:

+ Brute Force
+ Divide & Conquer
+ Greedy
+ Backtracking
+ Dynamic Programming

Once we understand the paradigm, we can then look at the data structure that is given in or can be used to solve the problem. Common data structures include:

+ Array
  + Stack
  + Queue
+ Linked List
+ HashMap/ HashTable
+ HashSet
+ Tree
  + Binary Tree
  + Binary Search Tree
+ Heap
+ Graph: (Adjacency List, Adjacency Matrix, Edge List)
  + Weighted Graph (Adjacency Map)
  + Directed Graph
  + Undirected Graph
  + Cyclic & Acyclic Graph
+ Trie

Next, comes algorithms (techniques) that can be used to solve the problem. **Objective is to understand these techniques to get a essence of them so that we can apply them to solve the problem.**
These techniques/algorithms can be look from lens of categories or paradigms.

Paradigms:
├── Brute Force
│   ├── Linear Search
│   ├── Selection Sort
│   └── Bubble Sort
├── Divide & Conquer
│   ├── Merge Sort
│   ├── Quick Sort
│   └── Binary Search
├── Greedy
│   └── Dijkstra's
├── Backtracking
│   └── DFS (and Backtracking problems)
└── Dynamic Programming
    └── (e.g., Memoized Dijkstra or DP problems)

Categories:
├── Sorting
│   ├── Array
│   │   ├── Selection Sort
│   │   ├── Bubble Sort
│   │   ├── Merge Sort
│   │   └── Quick Sort
│   └── Graph
│       └── Topological Sort
├── Search
│   ├── Array
│   │   ├── Linear Search
│   │   └── Binary Search
│   └── Graph
│       ├── DFS
│       └── BFS
└── Graph Algorithms
│   ├── Dijkstra's
│   └── Union-Find
└── Bit Manipulation
    └── Bitwise AND, OR, XOR & NOT

Another concepts is programming technique to keep in mind is recursion vs iteration. Recursion is a technique where a function calls itself in order to solve a problem, while iteration is a technique where a loop is used to repeat a set of instructions until a condition is met.

Lastly, we need to understand the **time complexity (T)** and **space complexity (M)** of the algorithms. Time complexity is a measure of how long an algorithm takes to run as a function of the size of the input, while space complexity is a measure of how much memory an algorithm uses as a function of the size of the input.

## Project Structure

```.
├── README.md
├── LICENSE
├── .gitignore
├── data_structures/ (Hold all data structures related questions)
├── categories/ (Hold all algorithm related questions)
└── paradigms/ (Hold all paradigms related questions)
```

## Boilerplate

```python
#!/usr/bin/env python3
"""
This is a boilerplate code for a Python project.
Rules to tackle problem:
1. Understand Problem.
2. Build Logic.
3. Make Edge Cases.
4. Complexity
"""

__license__ = "Apache-2.0"
__version__ = "0.1.0"
__maintainer__ = "Mihir Deo"

from typing import List, Dict, Any, Tuple, Union
from collections import defaultdict, deque
import heapq


def main():
    """
    Main function to run the project.
    """
    pass    
    # Add your code here
if __name__ == "__main__":
    main()
```
