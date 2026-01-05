# 217. Contains Duplicate
<span style="background-color: #000; color: #00ff00; padding: 4px 8px; border-radius: 4px; font-size: 12px;">Easy</span>

## Problem

Given an integer array *nums*, return `true` if any value appears at least twice in the array, and return `false` if every element is distinct.


## Examples

#### Example 1:

<div style="border-left: 4px solid gray; padding-left: 10px;">
Input: nums = [1,2,3,1]

Output: true

Explanation:

The element 1 occurs at the indices 0 and 3.
</div>

#### Example 2:

<div style="border-left: 4px solid gray; padding-left: 10px;">
Input: nums = [1,2,3,4]

Output: false

Explanation:

All elements are distinct.
</div>

#### Example 3:

<div style="border-left: 4px solid gray; padding-left: 10px;">
Input: nums = [1,1,1,3,3,4,3,2,4,2]

Output: true
</div>

## Approach

### Brute Force

    The idea behind this approach is to compare each number with the rest of numbers in the array. If a match found we return True. Otherwise we return False

##### Time Complexity

Suppose n is the length of the array and i is the iteration index starting at 0

**The outer loop** runs n times<br/>
**The inner loop** for each iteration of the outer loop it runs from i+1 to n-1

- i=0, inner loop runs n-1 times
- i=1, inner loop runs n-2 times
- i=2, inner loop runs n-3 times
- And so on...

The total number of comparisons is: (n-1)+(n-2)+(n-3)+...+1 = n(n-1)/2
this simplifies to n²/2 which in Big O notation is **O(n²)**
##### Space Complexity
O(1): only using a constant amount of extra space.


### Sorting

    This approach leverage sorting technique. First we sort our array of numbers then we compare each current number with the previous one.

##### Time Complexity

The time complexity of sorting is **O(n log n)**<br/>
Then we iterate over the array once which in Big O notation is **O(n)**

So the time complexity for this approach is **O(n log n)**

##### Space Complexity
<!-- Python's `list.sort()` uses Timsort, which requires:

O(n) auxiliary space in the worst case for temporary arrays during merging
O(log n) space for the recursion stack -->

The space complexity is typically O(n) in practice.

### Set

    In this approach we will use set to store distinct numbers of our nums array and we compare the total length of the set with the original length of nums

##### Time Complexity
The time complexity of this approach is O(n)
##### Space Complexity
we create a set of n elements in the worst case (all elements are distinct)
so the space complexity is O(n)