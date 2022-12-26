<span> <h1>Leetcode Solutions </h1> </span>

To understand a solution, it can be helpful to:

-   Read the problem statement carefully and make sure you understand the problem requirements and constraints.
-   Break down the solution into smaller pieces and try to understand how each part works.
-   Consider how the solution handles edge cases and special cases.
-   Test the solution with different inputs to see how it behaves.

       -   It is also a good idea to compare the solution to other solutions and understand the trade-offs and differences between them. This can help you learn different approaches to solving the same problem and improve your problem-solving skills.
## Problems & Solutions

| # | Title | Solution | Basic idea |
|---| ----- | -------- | --------------------- |
| 1 | [Roman to Integer](https://leetcode.com/problems/roman-to-integer/) | [Python](https://github.com/KOLEAJEOLAYINKA/leetcode/blob/main/algorithms/python/roman_to_integer.py) | defines a dictionary that maps Roman numerals to their corresponding integer values. Then, iterates through the characters in the input string s, and for each character, it checks if the next character has a higher integer value. If it does, it subtracts the value of the current character from the running total. If it does not, it adds the value of the current character to the running total. |
