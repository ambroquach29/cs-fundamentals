# Two Pointers Coding Pattern

As the name suggests, the two pointers pattern uses two pointers to iterate over an array or list until the conditions of the problem are satisfied. This is useful because it allows us to keep track of the values of two different indexes in a single iteration. Whenever there’s a requirement to find two data elements in an array that satisfy a certain condition, the two pointers pattern should be the first strategy to come to mind.

The pointers can be used to iterate the data structure in one or both directions, depending on the problem statement. For example, to identify whether a string is a palindrome, we can use one pointer to iterate the string from the beginning and the other to iterate it from the end. At each step, we can compare the values of the two pointers and see if they meet the palindrome properties.

The naive approach to solving this problem would be using nested loops, with a time complexity of O(n^2). However, by using two pointers moving towards the middle from either end, we exploit the symmetry property of palindromic strings. This allows us to compare the elements in a single loop, making the algorithm more efficient with a time complexity of O(n).

## Approach

The general approach of the two-pointers pattern is as follows:

1. Initialize two pointers, usually at the start and end of the data structure.
2. While the pointers haven't crossed each other:
   - Compare the values at the two pointers.
   - Based on the problem requirements, move the pointers closer or farther from each other.
   - Perform any necessary operations or checks.
3. Return the desired result.

## Examples

Reversing an Array

Valid Palindrome

Container with the Most Water

Product of Array Except Self

Sort Colors

Sum of Three Values

Trapping Rain Water
