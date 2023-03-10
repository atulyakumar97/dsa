## Leetcode Solved Problems

This folder contains a summary and all my leetcode solutions.

<table>

  <tr>
    <th>#</th>
    <th>Title</th>
    <th style="white-space:nowrap">Date Submitted</th>
    <th>Difficulty</th>
    <th>Tags</th>
    <th>Notes</th>
  </tr>

  <tr>
    <td>1</td>
    <td><a href="https://leetcode.com/problems/two-sum">Two Sum</a></td>
    <td>2022-02-08</td>
    <td>Easy</td>
    <td>Array, Hash Table</td>
    <td></td>
  </tr>

  <tr>
    <td>2</td>
    <td><a href="https://leetcode.com/problems/add-two-numbers">Add Two Numbers</a></td>
    <td>2022-02-12</td>
    <td>Medium</td>
    <td>Linked List, Math, Recursion</td>
    <td></td>
  </tr>

  <tr>
    <td>3</td>
    <td><a href="https://leetcode.com/problems/longest-substring-without-repeating-characters/">Longest Substring Without Repeating Characters</a></td>
    <td>2023-03-04</td>
    <td>Medium</td>
    <td>Hash Table, String, Sliding Window</td>
    <td>Two pointers (r increment by 1), if r not seen add r, else increment left until r seen only once</td>
  </tr>

  <tr>
    <td>6</td>
    <td><a href="https://leetcode.com/problems/zigzag-conversion">Zigzag Conversion</a></td>
    <td>2022-02-19</td>
    <td>Medium</td>
    <td>String</td>
    <td></td>
  </tr>

  <tr>
    <td>7</td>
    <td><a href="https://leetcode.com/problems/reverse-integer">Reverse Integer</a></td>
    <td>2022-02-08</td>
    <td>Medium</td>
    <td>Math</td>
    <td></td>
  </tr>

  <tr>
    <td>9</td>
    <td><a href="https://leetcode.com/problems/palindrome-number">Palindrome Number</a></td>
    <td>2022-01-30</td>
    <td>Easy</td>
    <td>Math</td>
    <td></td>
  </tr>

  <tr>
    <td>20</td>
    <td><a href="https://leetcode.com/problems/valid-parentheses/">Valid Parentheses</a></td>
    <td>2023-03-04</td>
    <td>Easy</td>
    <td>String, Stack</td>
    <td>Keep adding opening brackets to stack, if closing bracket pop from stack and check if it's a correct pair</td>
  </tr>

  <tr>
    <td>21</td>
    <td><a href="https://leetcode.com/problems/merge-two-sorted-lists/">Merge Two Sorted Lists</a></td>
    <td>2023-02-26</td>
    <td>Easy</td>
    <td>Linked List, Recursion</td>
    <td>init head, res node. while both lists are not none: add smaller val node after comparison to end of res. check and add non-empty linked list at back of res. return head.</td>
  </tr>

  <tr>
    <td>23</td>
    <td><a href="https://leetcode.com/problems/merge-k-sorted-lists/">Merge k Sorted Lists</a></td>
    <td>2023-02-25</td>
    <td>Hard</td>
    <td>Linked List, Divide and Conquer, Heap (Priority Queue), Merge Sort</td>
    <td>Add first node of each linked list to heap. While heap exists : Min of heap gets popped and appended to result link list. Append next node of linked list to heap.</td>
  </tr>

  <tr>
    <td>26</td>
    <td><a href="https://leetcode.com/problems/remove-duplicates-from-sorted-array">Remove Duplicates from Sorted Array</a></td>
    <td>2022-02-09</td>
    <td>Easy</td>
    <td>Array, Two Pointers</td>
    <td></td>
  </tr>

  <tr>
    <td>27</td>
    <td><a href="https://leetcode.com/problems/remove-element">Remove Element</a></td>
    <td>2022-02-09</td>
    <td>Easy</td>
    <td>Array, Two Pointers</td>
    <td></td>
  </tr>

  <tr>
    <td>28</td>
    <td><a href="https://leetcode.com/problems/find-the-index-of-the-first-occurrence-in-a-string">Find the Index of the First Occurrence in a String</a></td>
    <td>2022-02-05</td>
    <td>Medium</td>
    <td>Two Pointers, String, String Matching</td>
    <td>if len of needle > haystack return -1, iterate and match window return index on match</td>
  </tr>

  <tr>
    <td>35</td>
    <td><a href="https://leetcode.com/problems/search-insert-position">Search Insert Position</a></td>
    <td>2022-02-08</td>
    <td>Easy</td>
    <td>Array, Binary Search</td>
    <td>Binary search on array, return mid if target found or if target between mid-1 and mid. Edge case return 0 or len of arr if target is smallest or biggest</td>
  </tr>

  <tr>
    <td>58</td>
    <td><a href="https://leetcode.com/problems/length-of-last-word">Length of Last Word</a></td>
    <td>2022-02-09</td>
    <td>Easy</td>
    <td>String</td>
    <td></td>
  </tr>

  <tr>
    <td>66</td>
    <td><a href="https://leetcode.com/problems/plus-one">Plus One</a></td>
    <td>2022-03-06</td>
    <td>Easy</td>
    <td>Array, Math</td>
    <td></td>
  </tr>

  <tr>
    <td>67</td>
    <td><a href="https://leetcode.com/problems/add-binary">Add Binary</a></td>
    <td>2022-02-21</td>
    <td>Easy</td>
    <td>Math, String, Bit Manipulation, Simulation</td>
    <td></td>
  </tr>

  <tr>
    <td>69</td>
    <td><a href="https://leetcode.com/problems/sqrtx">Sqrt(x)</a></td>
    <td>2022-02-04</td>
    <td>Easy</td>
    <td>Math, Binary Search</td>
    <td></td>
  </tr>

  <tr>
    <td>78</td>
    <td><a href="https://leetcode.com/problems/subsets">Subsets</a></td>
    <td>2022-02-19</td>
    <td>Medium</td>
    <td>Array, Backtracking, Bit Manipulation</td>
    <td></td>
  </tr>

  <tr>
    <td>80</td>
    <td><a href="https://leetcode.com/problems/remove-duplicates-from-sorted-array-ii">Remove Duplicates from Sorted Array II</a></td>
    <td>2022-02-06</td>
    <td>Medium</td>
    <td>Array, Two Pointers</td>
    <td></td>
  </tr>

  <tr>
    <td>83</td>
    <td><a href="https://leetcode.com/problems/remove-duplicates-from-sorted-list">Remove Duplicates from Sorted List</a></td>
    <td>2022-02-05</td>
    <td>Easy</td>
    <td>Linked List</td>
    <td></td>
  </tr>

  <tr>
    <td>88</td>
    <td><a href="https://leetcode.com/problems/merge-sorted-array">Merge Sorted Array</a></td>
    <td>2022-02-09</td>
    <td>Easy</td>
    <td>Array, Two Pointers, Sorting</td>
    <td></td>
  </tr>

  <tr>
    <td>98</td>
    <td><a href="https://leetcode.com/problems/validate-binary-search-tree/">Validate Binary Search Tree</a></td>
    <td>2023-02-19</td>
    <td>Medium</td>
    <td>Tree, Depth-First Search, Binary Search Tree, Binary Tree</td>
    <td></td>
  </tr>

  <tr>
    <td>102</td>
    <td><a href="https://leetcode.com/problems/binary-tree-level-order-traversal/">Binary Tree Level Order Traversal</a></td>
    <td>2023-02-23</td>
    <td>Medium</td>
    <td>Tree, Breadth-First Search, Binary Tree</td>
    <td>BFS on btree. while len queue is not zero, take the len of queue, keep popping and storing in a level list, add children to queue</td>
  </tr>

  <tr>
    <td>103</td>
    <td><a href="https://leetcode.com/problems/binary-tree-zigzag-level-order-traversal/">Binary Tree Zigzag Level Order Traversal</a></td>
    <td>2023-02-23</td>
    <td>Medium</td>
    <td>Tree, Breadth-First Search,Binary Tree</td>
    <td>BFS on btree. while len queue in not zero, take the len of queue, keep popping and storing in a level, append at last/insert at pos 0  alternatively, add children to queue</td>
  </tr>

  <tr>
    <td>104</td>
    <td><a href="https://leetcode.com/problems/maximum-depth-of-binary-tree/">Maximum Depth of Binary Tree</a></td>
    <td>2023-02-16</td>
    <td>Easy</td>
    <td>Tree, Depth-First Search, Breadth-First Search, Binary Tree</td>
    <td></td>
  </tr>

  <tr>
    <td>111</td>
    <td><a href="https://leetcode.com/problems/minimum-depth-of-binary-tree/">Minimum Depth of Binary Tree</a></td>
    <td>2023-02-23</td>
    <td>Easy</td>
    <td>Tree, Depth-First Search, Breadth-First Search, Binary Tree</td>
    <td>BFS on btree. init depth = 0, while len queue is no zero, take the len of queue n, increase depth by 1, keeping popping till n nodes and storing the children in the queue. if a node has no children return depth</td>
  </tr>

  <tr>
    <td>121</td>
    <td><a href="https://leetcode.com/problems/best-time-to-buy-and-sell-stock">Best Time to Buy and Sell Stock</a></td>
    <td>2022-02-01</td>
    <td>Easy</td>
    <td>Array, Dynamic Programming</td>
    <td></td>
  </tr>

  <tr>
    <td>125</td>
    <td><a href="https://leetcode.com/problems/valid-palindrome">Valid Palindrome</a></td>
    <td>2022-02-20</td>
    <td>Easy</td>
    <td>Two Pointers, String</td>
    <td></td>
  </tr>

  <tr>
    <td>141</td>
    <td><a href="https://leetcode.com/problems/linked-list-cycle/">Linked List Cycle</a></td>
    <td>2023-02-11</td>
    <td>Easy</td>
    <td>Hash Table, Linked List, Two Pointers</td>
    <td></td>
  </tr>

  <tr>
    <td>142</td>
    <td><a href="https://leetcode.com/problems/linked-list-cycle-ii/">Linked List Cycle II</a></td>
    <td>2023-03-09</td>
    <td>Medium</td>
    <td>Hash Table, Linked List, Two Pointers</td>
    <td>Init fast and slow pointer. On match, reset fast pointer to head. Move slow and fast pointer equally now until they re-intersect.</td>
  </tr>

  <tr>
    <td>148</td>
    <td><a href="https://leetcode.com/problems/sort-list/">Sort List</a></td>
    <td>2023-02-26</td>
    <td>Medium</td>
    <td>Linked List, Two Pointers, Divide and Conquer, Sorting, Merge Sort</td>
    <td>Heappush elements from linkedlist, Heappop into a new linked list. Optimization Required.</td>
  </tr>

  <tr>
    <td>167</td>
    <td><a href="https://leetcode.com/problems/two-sum-ii-input-array-is-sorted/">Two Sum II - Input Array Is Sorted</a></td>
    <td>2023-02-16</td>
    <td>Medium</td>
    <td>Array, Two Pointers, Binary Search</td>
    <td></td>
  </tr>

  <tr>
    <td>169</td>
    <td><a href="https://leetcode.com/problems/majority-element">Majority Element</a></td>
    <td>2022-02-21</td>
    <td>Easy</td>
    <td>Array, Hash Table, Divide and Conquer, Sorting, Counting</td>
    <td></td>
  </tr>

  <tr>
    <td>171</td>
    <td><a href="https://leetcode.com/problems/excel-sheet-column-number">Excel Sheet Column Number</a></td>
    <td>2022-02-22</td>
    <td>Easy</td>
    <td>Math, String</td>
    <td></td>
  </tr>

  <tr>
    <td>182</td>
    <td><a href="https://leetcode.com/problems/duplicate-emails">Duplicate Emails</a></td>
    <td>2022-02-03</td>
    <td>Easy</td>
    <td>Database</td>
    <td></td>
  </tr>

  <tr>
    <td>189</td>
    <td><a href="https://leetcode.com/problems/rotate-array">Rotate Array</a></td>
    <td>2022-01-30</td>
    <td>Medium</td>
    <td>Array, Math, Two Pointers</td>
    <td></td>
  </tr>

  <tr>
    <td>199</td>
    <td><a href="https://leetcode.com/problems/binary-tree-right-side-view/">Binary Tree Right Side View</a></td>
    <td>2023-02-23</td>
    <td>Medium</td>
    <td>Tree, Depth-First Search, Breadth-First Search, Binary Tree</td>
    <td>BFS on btree. while len queue is not zero, take the len of queue - add the last (-1) element in the queue to ans, keep popping the nodes at a level, add children to queue</td>
  </tr>

  <tr>
    <td>206</td>
    <td><a href="https://leetcode.com/problems/reverse-linked-list/">Reverse Linked List</a></td>
    <td>2023-03-04</td>
    <td>Easy</td>
    <td>Linked List, Recursion</td>
    <td>init prev as none, iterate over linked list, assign head to current, current's next is prev, store current in prev</td>
  </tr>

  <tr>
    <td>215</td>
    <td><a href="https://leetcode.com/problems/kth-largest-element-in-an-array">Kth Largest Element in an Array</a></td>
    <td>2023-02-28</td>
    <td>Medium</td>
    <td>Array, Divide and Conquer, Sorting, Heap (Priority Queue), Quickselect</td>
    <td>Create minheap with k elements. Iterate over array, if arr element greater than heap min, pop heap element & push arr element. Optimization Required (Quickselect).</td>
  </tr>

  <tr>
    <td>217</td>
    <td><a href="https://leetcode.com/problems/contains-duplicate">Contains Duplicate</a></td>
    <td>2022-02-12</td>
    <td>Easy</td>
    <td>Array, Hash Table, Sorting</td>
    <td></td>
  </tr>

  <tr>
    <td>226</td>
    <td><a href="https://leetcode.com/problems/invert-binary-tree/">Invert Binary Tree</a></td>
    <td>2023-02-19</td>
    <td>Easy</td>
    <td>Tree, Depth-First Search, Breadth-First Search, Binary Tree</td>
    <td></td>
  </tr>

  <tr>
    <td>235</td>
    <td><a href="https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-search-tree/">Lowest Common Ancestor of a Binary Search Tree</a></td>
    <td>2023-02-19</td>
    <td>Medium</td>
    <td>Tree, Depth-First Search, Binary Search Tree, Binary Tree</td>
    <td></td>
  </tr>

  <tr>
    <td>242</td>
    <td><a href="https://leetcode.com/problems/valid-anagram">Valid Anagram</a></td>
    <td>2022-02-02</td>
    <td>Easy</td>
    <td>Hash Table, String, Sorting</td>
    <td></td>
  </tr>

  <tr>
    <td>258</td>
    <td><a href="https://leetcode.com/problems/add-digits">Add Digits</a></td>
    <td>2022-02-08</td>
    <td>Easy</td>
    <td>Math, Simulation, Number Theory</td>
    <td></td>
  </tr>

  <tr>
    <td>263</td>
    <td><a href="https://leetcode.com/problems/ugly-number/">Ugly Numbers</a></td>
    <td>2023-03-04</td>
    <td>Easy</td>
    <td>Math</td>
    <td>return False if number is -ve, if (while) num is divisible by 2,3,5 keep dividing, if 1 is remainder return True</td>
  </tr>

  <tr>
    <td>264</td>
    <td><a href="https://leetcode.com/problems/ugly-number-ii/">Ugly Number II</a></td>
    <td>2023-03-04</td>
    <td>Medium</td>
    <td>Hash Table, Math, Dynamic Programming, Heap (Priority Queue)</td>
    <td>Create minheap with num 1. for n-1 time pop heap and generate 3 values and heappush. return top of heap after n-1 pops</td>
  </tr>

  <tr>
    <td>278</td>
    <td><a href="https://leetcode.com/problems/first-bad-version">First Bad Version</a></td>
    <td>2022-02-08</td>
    <td>Easy</td>
    <td>Binary Search, Interactive</td>
    <td></td>
  </tr>

  <tr>
    <td>283</td>
    <td><a href="https://leetcode.com/problems/move-zeroes">Move Zeroes</a></td>
    <td>2022-02-10</td>
    <td>Easy</td>
    <td>Array, Two Pointers</td>
    <td></td>
  </tr>

  <tr>
    <td>287</td>
    <td><a href="https://leetcode.com/problems/find-the-duplicate-number">Find the Duplicate Number</a></td>
    <td>2022-02-23</td>
    <td>Medium</td>
    <td>Array, Two Pointers, Binary Search, Bit Manipulation</td>
    <td></td>
  </tr>

  <tr>
    <td>290</td>
    <td><a href="https://leetcode.com/problems/word-pattern">Word Pattern</a></td>
    <td>2022-02-23</td>
    <td>Easy</td>
    <td>Hash Table, String</td>
    <td></td>
  </tr>

  <tr>
    <td>295</td>
    <td><a href="https://leetcode.com/problems/find-median-from-data-stream">Find Median from Data Stream</a></td>
    <td>2023-03-07</td>
    <td>Hard</td>
    <td>Two Pointers, Design, Sorting, Heap (Priority Queue), Data Stream</td>
    <td>add num - add to left if right_min_heap is empty or if num less than right_min_heap[0] else add to left_max_heap. balance if left_max_heap is smaller than right_min_heap. balance if left_max_heap is bigger than right_max_heap by 1 element.</td>
  </tr>

  <tr>
    <td>344</td>
    <td><a href="https://leetcode.com/problems/reverse-string">Reverse String</a></td>
    <td>2022-02-20</td>
    <td>Easy</td>
    <td>Two Pointers, String</td>
    <td></td>
  </tr>

  <tr>
    <td>345</td>
    <td><a href="https://leetcode.com/problems/reverse-vowels-of-a-string">Reverse Vowels of a String</a></td>
    <td>2022-02-22</td>
    <td>Easy</td>
    <td>Two Pointers, String</td>
    <td></td>
  </tr>

  <tr>
    <td>349</td>
    <td><a href="https://leetcode.com/problems/intersection-of-two-arrays/">Intersection of Two Arrays</a></td>
    <td>2023-02-02</td>
    <td>Easy</td>
    <td>Array, Hash Table, Two Pointers, Binary Search, Sorting</td>
    <td></td>
  </tr>

  <tr>
    <td>350</td>
    <td><a href="https://leetcode.com/problems/intersection-of-two-arrays-ii">Intersection of Two Arrays II</a></td>
    <td>2022-02-12</td>
    <td>Easy</td>
    <td>Array, Hash Table, Two Pointers, Binary Search, Sorting</td>
    <td></td>
  </tr>

  <tr>
    <td>378</td>
    <td><a href="https://leetcode.com/problems/kth-smallest-element-in-a-sorted-matrix">Kth Smallest Element in a Sorted Matrix</a></td>
    <td>2023-03-04</td>
    <td>Medium</td>
    <td>Array, Binary Search, Sorting, Heap (Priority Queue), Matrix</td>
    <td>add first element of each matrix row to heap. pop 1 element from heap & push next element of the corresponding row. repeat k times</td>
  </tr>

  <tr>
    <td>387</td>
    <td><a href="https://leetcode.com/problems/first-unique-character-in-a-string">First Unique Character in a String</a></td>
    <td>2022-02-12</td>
    <td>Easy</td>
    <td>Hash Table, String, Queue, Counting</td>
    <td></td>
  </tr>

  <tr>
    <td>389</td>
    <td><a href="https://leetcode.com/problems/find-the-difference">Find the Difference</a></td>
    <td>2022-02-07</td>
    <td>Easy</td>
    <td>Hash Table, String, Bit Manipulation, Sorting</td>
    <td></td>
  </tr>

  <tr>
    <td>414</td>
    <td><a href="https://leetcode.com/problems/third-maximum-number">Third Maximum Number</a></td>
    <td>2022-02-21</td>
    <td>Easy</td>
    <td>Array, Sorting</td>
    <td></td>
  </tr>

  <tr>
    <td>438</td>
    <td><a href="https://leetcode.com/problems/find-all-anagrams-in-a-string">Find All Anagrams in a String</a></td>
    <td>2023-02-08</td>
    <td>Medium</td>
    <td>Hash Table, String, Sliding Window</td>
    <td></td>
  </tr>

  <tr>
    <td>448</td>
    <td><a href="https://leetcode.com/problems/find-all-numbers-disappeared-in-an-array">Find All Numbers Disappeared in an Array</a></td>
    <td>2022-02-20</td>
    <td>Easy</td>
    <td>Array, Hash Table</td>
    <td></td>
  </tr>

  <tr>
    <td>485</td>
    <td><a href="https://leetcode.com/problems/majority-element">Max Consecutive Ones</a></td>
    <td>2022-01-13</td>
    <td>Easy</td>
    <td>Array</td>
    <td></td>
  </tr>

  <tr>
    <td>509</td>
    <td><a href="https://leetcode.com/problems/fibonacci-number">Fibonacci Number</a></td>
    <td>2022-02-12</td>
    <td>Easy</td>
    <td>Math, Dynamic Programming, Recursion, Memoization</td>
    <td></td>
  </tr>

  <tr>
    <td>525</td>
    <td><a href="https://leetcode.com/problems/contiguous-array">Contiguous Array</a></td>
    <td>2022-02-05</td>
    <td>Medium</td>
    <td>Array, Hash Table, Prefix Sum</td>
    <td></td>
  </tr>

  <tr>
    <td>532</td>
    <td><a href="https://leetcode.com/problems/k-diff-pairs-in-an-array">K-diff Pairs in an Array</a></td>
    <td>2022-02-09</td>
    <td>Medium</td>
    <td>Array, Hash Table, Two Pointers, Binary Search, Sorting</td>
    <td></td>
  </tr>

  <tr>
    <td>535</td>
    <td><a href="https://leetcode.com/problems/encode-and-decode-tinyurl">Encode and Decode TinyURL</a></td>
    <td>2022-02-20</td>
    <td>Medium</td>
    <td>Hash Table, String, Design, Hash Function</td>
    <td></td>
  </tr>

  <tr>
    <td>540</td>
    <td><a href="https://leetcode.com/problems/single-element-in-a-sorted-array/">Single Element in a Sorted Array</a></td>
    <td>2023-02-21</td>
    <td>Medium</td>
    <td>Array, Binary Search</td>
    <td>Binary search, if mid is odd mid -1 and check nums[mid] and nums[mid+1] matches then binary search on right half (mid + 2) else binary search on left half</td>
  </tr>

  <tr>
    <td>557</td>
    <td><a href="https://leetcode.com/problems/reverse-words-in-a-string-iii">Reverse Words in a String III</a></td>
    <td>2022-02-20</td>
    <td>Easy</td>
    <td>Two Pointers, String</td>
    <td></td>
  </tr>

  <tr>
    <td>560</td>
    <td><a href="https://leetcode.com/problems/subarray-sum-equals-k/">Subarray Sum Equals K</a></td>
    <td>2023-02-11</td>
    <td>Medium</td>
    <td>Array, Hash Table, Prefix Sum</td>
    <td></td>
  </tr>

  <tr>
    <td>567</td>
    <td><a href="https://leetcode.com/problems/permutation-in-string">Permutation in String</a></td>
    <td>2022-02-11</td>
    <td>Medium</td>
    <td>Hash Table, Two Pointers, String, Sliding Window</td>
    <td></td>
  </tr>

  <tr>
    <td>595</td>
    <td><a href="https://leetcode.com/problems/big-countries">Big Countries</a></td>
    <td>2022-02-06</td>
    <td>Easy</td>
    <td>Database</td>
    <td></td>
  </tr>

  <tr>
    <td>622</td>
    <td><a href="https://leetcode.com/problems/design-circular-queue">Design Circular Queue</a></td>
    <td>2022-02-27</td>
    <td>Medium</td>
    <td>Array, Linked List, Design, Queue</td>
    <td></td>
  </tr>

  <tr>
    <td>627</td>
    <td><a href="https://leetcode.com/problems/swap-salary">Swap Salary</a></td>
    <td>2022-02-03</td>
    <td>Easy</td>
    <td>Database</td>
    <td></td>
  </tr>

  <tr>
    <td>658</td>
    <td><a href="https://leetcode.com/problems/find-k-closest-elements/">Find K Closest Elements</a></td>
    <td>2023-03-10</td>
    <td>Medium</td>
    <td>Array, Two Pointers, Binary Search, Sliding Window, Sorting, Heap (Priority Queue)</td>
    <td>Init k elements max heap with dist as priority. Pop first element if max element of heap and push smaller element. Sorted and return k elements by val (not dist). Optimization Required.</td>
  </tr>

  <tr>
    <td>701</td>
    <td><a href="https://leetcode.com/problems/swap-salary">Insert into a Binary Search Tree</a></td>
    <td>2023-02-19</td>
    <td>Medium</td>
    <td>Tree, Binary Search Tree, Binary Tree</td>
    <td></td>
  </tr>

  <tr>
    <td>703</td>
    <td><a href="https://leetcode.com/problems/kth-largest-element-in-a-stream/">Kth Largest Element in a Stream</a></td>
    <td>2023-03-04</td>
    <td>Easy</td>
    <td>Tree, Design, Binary Search Tree, Heap (Priority Queue), Binary Tree, Data Stream</td>
    <td>init - Build minheap of length k. add - heappush val, pop if greater than len k. return heap min</td>
  </tr>

  <tr>
    <td>704</td>
    <td><a href="https://leetcode.com/problems/binary-search">Binary Search</a></td>
    <td>2022-02-12</td>
    <td>Easy</td>
    <td>Array, Binary Search</td>
    <td></td>
  </tr>

  <tr>
    <td>709</td>
    <td><a href="https://leetcode.com/problems/to-lower-case">To Lower Case</a></td>
    <td>2022-02-01</td>
    <td>Easy</td>
    <td>String</td>
    <td></td>
  </tr>

  <tr>
    <td>733</td>
    <td><a href="https://leetcode.com/problems/flood-fill/">Flood Fill</a></td>
    <td>2023-03-12</td>
    <td>Easy</td>
    <td>Array, Depth-First Search, Breadth-First Search, Matrix</td>
    <td>Get neighbors function to find L,R,U,D elements in matrix. BFS on image from start pixel until neighbors not found with start pixel value.</td>
  </tr>

  <tr>
    <td>767</td>
    <td><a href="https://leetcode.com/problems/reorganize-string/">Reorganize String</a></td>
    <td>2023-03-04</td>
    <td>Medium</td>
    <td>Hash Table, String, Greedy, Sorting, Heap (Priority Queue), Counting</td>
    <td>init counter of string. create max heap with freq as priority and char as value. if max freq char occupies more than all even places then exit. place max freq char in even places and then odd places.</td>
  </tr>

  <tr>
    <td>771</td>
    <td><a href="https://leetcode.com/problems/jewels-and-stones">Jewels and Stones</a></td>
    <td>2022-01-31</td>
    <td>Easy</td>
    <td>Hash Table, String</td>
    <td></td>
  </tr>

  <tr>
    <td>804</td>
    <td><a href="https://leetcode.com/problems/unique-morse-code-words">Unique Morse Code Words</a></td>
    <td>2022-02-05</td>
    <td>Easy</td>
    <td>Array, Hash Table, String</td>
    <td></td>
  </tr>

  <tr>
    <td>811</td>
    <td><a href="https://leetcode.com/problems/subdomain-visit-count">Subdomain Visit Count</a></td>
    <td>2022-02-20</td>
    <td>Medium</td>
    <td>Array, Hash Table, String, Counting</td>
    <td></td>
  </tr>

  <tr>
    <td>832</td>
    <td><a href="https://leetcode.com/problems/flipping-an-image">Flipping an Image</a></td>
    <td>2022-02-26</td>
    <td>Easy</td>
    <td>Array, Two Pointers, Matrix, Simulation</td>
    <td></td>
  </tr>

  <tr>
    <td>852</td>
    <td><a href="https://leetcode.com/problems/peak-index-in-a-mountain-array/">Peak Index in a Mountain Array</a></td>
    <td>2023-02-06</td>
    <td>Medium</td>
    <td>Array, Binary Search</td>
    <td></td>
  </tr>

  <tr>
    <td>876</td>
    <td><a href="https://leetcode.com/problems/middle-of-the-linked-list/">Middle of the Linked List</a></td>
    <td>2023-02-07</td>
    <td>Easy</td>
    <td>Linked List, Two Pointers</td>
    <td></td>
  </tr>

  <tr>
    <td>896</td>
    <td><a href="https://leetcode.com/problems/monotonic-array">Monotonic Array</a></td>
    <td>2022-02-13</td>
    <td>Easy</td>
    <td>Array</td>
    <td></td>
  </tr>

  <tr>
    <td>905</td>
    <td><a href="https://leetcode.com/problems/sort-array-by-parity">Sort Array By Parity</a></td>
    <td>2022-02-09</td>
    <td>Easy</td>
    <td>Array, Two Pointers, Sorting</td>
    <td></td>
  </tr>

  <tr>
    <td>912</td>
    <td><a href="https://leetcode.com/problems/sort-an-array/">Sort an Array</a></td>
    <td>2023-02-02</td>
    <td>Medium</td>
    <td>Array, Divide and Conquer, Sorting, Heap (Priority Queue), Merge Sort, Bucket Sort, Radix Sort, Counting Sort</td>
    <td></td>
  </tr>

  <tr>
    <td>917</td>
    <td><a href="https://leetcode.com/problems/reverse-only-letters">Reverse Only Letters</a></td>
    <td>2022-02-07</td>
    <td>Easy</td>
    <td>Two Pointers, String</td>
    <td></td>
  </tr>

  <tr>
    <td>929</td>
    <td><a href="https://leetcode.com/problems/unique-email-addresses">Unique Email Addresses</a></td>
    <td>2022-02-20</td>
    <td>Easy</td>
    <td>Array, Hash Table, String</td>
    <td></td>
  </tr>

  <tr>
    <td>941</td>
    <td><a href="https://leetcode.com/problems/valid-mountain-array">Valid Mountain Array</a></td>
    <td>2022-02-21</td>
    <td>Easy</td>
    <td>Array</td>
    <td></td>
  </tr>

  <tr>
    <td>973</td>
    <td><a href="https://leetcode.com/problems/k-closest-points-to-origin/">K Closest Points to Origin</a></td>
    <td>2023-03-04</td>
    <td>Medium</td>
    <td>Array, Math, Divide and Conquer, Geometry, Sorting, Heap (Priority Queue), Quickselect</td>
    <td>Create min heap with priority = dist from origin, val = point. Pop heap k times</td>
  </tr>

  <tr>
    <td>977</td>
    <td><a href="https://leetcode.com/problems/squares-of-a-sorted-array">Squares of a Sorted Array</a></td>
    <td>2022-02-10</td>
    <td>Easy</td>
    <td>Array, Two Pointers, Sorting</td>
    <td></td>
  </tr>

  <tr>
    <td>989</td>
    <td><a href="https://leetcode.com/problems/add-to-array-form-of-integer/">Add to Array-Form of Integer</a></td>
    <td>2023-02-15</td>
    <td>Easy</td>
    <td>Array, Math</td>
    <td></td>
  </tr>

  <tr>
    <td>1046</td>
    <td><a href="https://leetcode.com/problems/last-stone-weight/">Last Stone Weight</a></td>
    <td>2023-03-07</td>
    <td>Easy</td>
    <td>Array, Heap (Priority Queue)</td>
    <td>Create max heap. pop 2 elements, store the abs(difference) if it is non-zero. return top element if only 1 element remains else return 0</td>
  </tr>

  <tr>
    <td>1051</td>
    <td><a href="https://leetcode.com/problems/height-checker">Height Checker</a></td>
    <td>2022-02-21</td>
    <td>Easy</td>
    <td>Array, Sorting, Counting Sort</td>
    <td></td>
  </tr>

  <tr>
    <td>1089</td>
    <td><a href="https://leetcode.com/problems/duplicate-emails">Duplicate Zeros</a></td>
    <td>2022-01-14</td>
    <td>Easy</td>
    <td>Array, Two Pointers</td>
    <td></td>
  </tr>

  <tr>
    <td>1108</td>
    <td><a href="https://leetcode.com/problems/defanging-an-ip-address">Defanging an IP Address</a></td>
    <td>2022-01-30</td>
    <td>Easy</td>
    <td>String</td>
    <td></td>
  </tr>

  <tr>
    <td>1137</td>
    <td><a href="https://leetcode.com/problems/n-th-tribonacci-number">N-th Tribonacci Number</a></td>
    <td>2023-01-30</td>
    <td>Easy</td>
    <td>Math, Dynamic Programming, Memoization</td>
    <td></td>
  </tr>

  <tr>
    <td>1207</td>
    <td><a href="https://leetcode.com/problems/unique-number-of-occurrences">Unique Number of Occurrences</a></td>
    <td>2022-02-05</td>
    <td>Easy</td>
    <td>Array, Hash Table</td>
    <td></td>
  </tr>

  <tr>
    <td>1221</td>
    <td><a href="https://leetcode.com/problems/split-a-string-in-balanced-strings">Split a String in Balanced Strings</a></td>
    <td>2022-01-31</td>
    <td>Easy</td>
    <td>String, Greedy, Counting</td>
    <td></td>
  </tr>

  <tr>
    <td>1281</td>
    <td><a href="https://leetcode.com/problems/subtract-the-product-and-sum-of-digits-of-an-integer">Subtract the Product and Sum of Digits of an Integer</a></td>
    <td>2022-01-31</td>
    <td>Easy</td>
    <td>Math</td>
    <td></td>
  </tr>

  <tr>
    <td>1288</td>
    <td><a href="https://leetcode.com/problems/remove-covered-intervals">Remove Covered Intervals</a></td>
    <td>2022-02-20</td>
    <td>Medium</td>
    <td>Array, Sorting</td>
    <td></td>
  </tr>

  <tr>
    <td>1290</td>
    <td><a href="https://leetcode.com/problems/convert-binary-number-in-a-linked-list-to-integer">Convert Binary Number in a Linked List to Integer</a></td>
    <td>2022-02-21</td>
    <td>Easy</td>
    <td>Linked List, Math</td>
    <td></td>
  </tr>

  <tr>
    <td>1295</td>
    <td><a href="https://leetcode.com/problems/find-first-palindromic-string-in-the-array">Find Numbers with Even Number of Digits</a></td>
    <td>2022-01-13</td>
    <td>Easy</td>
    <td>Array</td>
    <td></td>
  </tr>

  <tr>
    <td>1299</td>
    <td><a href="https://leetcode.com/problems/replace-elements-with-greatest-element-on-right-side">Replace Elements with Greatest Element on Right Side</a></td>
    <td>2022-01-30</td>
    <td>Easy</td>
    <td>Array</td>
    <td></td>
  </tr>

  <tr>
    <td>1309</td>
    <td><a href="https://leetcode.com/problems/decrypt-string-from-alphabet-to-integer-mapping">Decrypt String from Alphabet to Integer Mapping</a></td>
    <td>2022-02-06</td>
    <td>Easy</td>
    <td>String</td>
    <td></td>
  </tr>

  <tr>
    <td>1313</td>
    <td><a href="https://leetcode.com/problems/decompress-run-length-encoded-list">Decompress Run-Length Encoded List</a></td>
    <td>2022-01-31</td>
    <td>Easy</td>
    <td>Array</td>
    <td></td>
  </tr>

  <tr>
    <td>1323</td>
    <td><a href="https://leetcode.com/problems/maximum-69-number">Maximum 69 Number</a></td>
    <td>2022-02-06</td>
    <td>Easy</td>
    <td>Math, Greedy</td>
    <td></td>
  </tr>

  <tr>
    <td>1342</td>
    <td><a href="https://leetcode.com/problems/number-of-steps-to-reduce-a-number-to-zero">Number of Steps to Reduce a Number to Zero</a></td>
    <td>2022-01-31</td>
    <td>Easy</td>
    <td>Math, Bit Manipulation</td>
    <td></td>
  </tr>

  <tr>
    <td>1346</td>
    <td><a href="https://leetcode.com/problems/check-if-n-and-its-double-exist">Check If N and Its Double Exist</a></td>
    <td>2022-02-09</td>
    <td>Easy</td>
    <td>Array, Hash Table, Two Pointers, Binary Search, Sorting</td>
    <td></td>
  </tr>

  <tr>
    <td>1365</td>
    <td><a href="https://leetcode.com/problems/how-many-numbers-are-smaller-than-the-current-number">How Many Numbers Are Smaller Than the Current Number</a></td>
    <td>2022-01-31</td>
    <td>Easy</td>
    <td>Array, Hash Table, Sorting, Counting</td>
    <td></td>
  </tr>

  <tr>
    <td>1389</td>
    <td><a href="https://leetcode.com/problems/create-target-array-in-the-given-order">Create Target Array in the Given Order</a></td>
    <td>2022-01-31</td>
    <td>Easy</td>
    <td>Array, Simulation</td>
    <td></td>
  </tr>

  <tr>
    <td>1431</td>
    <td><a href="https://leetcode.com/problems/kids-with-the-greatest-number-of-candies">Kids With the Greatest Number of Candies</a></td>
    <td>2022-01-31</td>
    <td>Easy</td>
    <td>Array</td>
    <td></td>
  </tr>

  <tr>
    <td>1448</td>
    <td><a href="https://leetcode.com/problems/count-good-nodes-in-binary-tree/">Count Good Nodes in Binary Tree</a></td>
    <td>2022-02-11</td>
    <td>Medium</td>
    <td>Tree, Depth-First Search, Breadth-First Search, Binary Tree</td>
    <td></td>
  </tr>

  <tr>
    <td>1470</td>
    <td><a href="https://leetcode.com/problems/shuffle-the-array">Shuffle the Array</a></td>
    <td>2022-01-30</td>
    <td>Easy</td>
    <td>Array</td>
    <td></td>
  </tr>

  <tr>
    <td>1480</td>
    <td><a href="https://leetcode.com/problems/running-sum-of-1d-array">Running Sum of 1d Array</a></td>
    <td>2022-01-30</td>
    <td>Easy</td>
    <td>Array, Prefix Sum</td>
    <td></td>
  </tr>

  <tr>
    <td>1484</td>
    <td><a href="https://leetcode.com/problems/group-sold-products-by-the-date">Group Sold Products By The Date</a></td>
    <td>2022-05-20</td>
    <td>Easy</td>
    <td>Database</td>
    <td></td>
  </tr>

  <tr>
    <td>1486</td>
    <td><a href="https://leetcode.com/problems/xor-operation-in-an-array">XOR Operation in an Array</a></td>
    <td>2022-02-01</td>
    <td>Easy</td>
    <td>Math, Bit Manipulation</td>
    <td></td>
  </tr>

  <tr>
    <td>1491</td>
    <td><a href="https://leetcode.com/problems/average-salary-excluding-the-minimum-and-maximum-salary">Average Salary Excluding the Minimum and Maximum Salary</a></td>
    <td>2022-02-23</td>
    <td>Easy</td>
    <td>Array, Sorting</td>
    <td></td>
  </tr>

  <tr>
    <td>1507</td>
    <td><a href="https://leetcode.com/problems/reformat-date">Reformat Date</a></td>
    <td>2022-02-07</td>
    <td>Easy</td>
    <td>String</td>
    <td></td>
  </tr>

  <tr>
    <td>1512</td>
    <td><a href="https://leetcode.com/problems/number-of-good-pairs">Number of Good Pairs</a></td>
    <td>2022-01-30</td>
    <td>Easy</td>
    <td>Array, Hash Table, Math, Counting</td>
    <td></td>
  </tr>

  <tr>
    <td>1528</td>
    <td><a href="https://leetcode.com/problems/shuffle-string">Shuffle String</a></td>
    <td>2022-01-31</td>
    <td>Easy</td>
    <td>Array, String</td>
    <td></td>
  </tr>

  <tr>
    <td>1539</td>
    <td><a href="https://leetcode.com/problems/kth-missing-positive-number/">Kth Missing Positive Number</a></td>
    <td>2023-03-06</td>
    <td>Easy</td>
    <td>Array, Binary Search</td>
    <td>Track missing positive numbers as you scan the array</td>
  </tr>

  <tr>
    <td>1550</td>
    <td><a href="https://leetcode.com/problems/three-consecutive-odds">Three Consecutive Odds</a></td>
    <td>2022-02-27</td>
    <td>Easy</td>
    <td>Array</td>
    <td></td>
  </tr>

  <tr>
    <td>1581</td>
    <td><a href="https://leetcode.com/problems/customer-who-visited-but-did-not-make-any-transactions">Customer Who Visited but Did Not Make Any Transactions</a></td>
    <td>2022-05-17</td>
    <td>Easy</td>
    <td>Database</td>
    <td></td>
  </tr>

  <tr>
    <td>1587</td>
    <td><a href="https://leetcode.com/problems/bank-account-summary-ii">Bank Account Summary II</a></td>
    <td>2022-05-16</td>
    <td>Easy</td>
    <td>Database</td>
    <td></td>
  </tr>

  <tr>
    <td>1603</td>
    <td><a href="https://leetcode.com/problems/design-parking-system">Design Parking System</a></td>
    <td>2022-01-31</td>
    <td>Easy</td>
    <td>Design, Simulation, Counting</td>
    <td></td>
  </tr>

  <tr>
    <td>1662</td>
    <td><a href="https://leetcode.com/problems/check-if-two-string-arrays-are-equivalent">Check If Two String Arrays are Equivalent</a></td>
    <td>2022-02-01</td>
    <td>Easy</td>
    <td>Array, String</td>
    <td></td>
  </tr>

  <tr>
    <td>1672</td>
    <td><a href="https://leetcode.com/problems/richest-customer-wealth">Richest Customer Wealth</a></td>
    <td>2022-01-31</td>
    <td>Easy</td>
    <td>Array, Matrix</td>
    <td></td>
  </tr>

  <tr>
    <td>1678</td>
    <td><a href="https://leetcode.com/problems/goal-parser-interpretation">Goal Parser Interpretation</a></td>
    <td>2022-02-01</td>
    <td>Easy</td>
    <td>String</td>
    <td></td>
  </tr>

  <tr>
    <td>1684</td>
    <td><a href="https://leetcode.com/problems/count-the-number-of-consistent-strings">Count the Number of Consistent Strings</a></td>
    <td>2022-02-05</td>
    <td>Easy</td>
    <td>Array, Hash Table, String, Bit Manipulation</td>
    <td></td>
  </tr>

  <tr>
    <td>1689</td>
    <td><a href="https://leetcode.com/problems/partitioning-into-minimum-number-of-deci-binary-numbers">Partitioning Into Minimum Number Of Deci-Binary Numbers</a></td>
    <td>2022-02-20</td>
    <td>Medium</td>
    <td>String, Greedy</td>
    <td></td>
  </tr>

  <tr>
    <td>1693</td>
    <td><a href="https://leetcode.com/problems/daily-leads-and-partners">Daily Leads and Partners</a></td>
    <td>2022-05-14</td>
    <td>Easy</td>
    <td>Database</td>
    <td></td>
  </tr>

  <tr>
    <td>1704</td>
    <td><a href="https://leetcode.com/problems/determine-if-string-halves-are-alike">Determine if String Halves Are Alike</a></td>
    <td>2022-02-06</td>
    <td>Easy</td>
    <td>String, Counting</td>
    <td></td>
  </tr>

  <tr>
    <td>1720</td>
    <td><a href="https://leetcode.com/problems/decode-xored-array">Decode XORed Array</a></td>
    <td>2022-01-31</td>
    <td>Easy</td>
    <td>Array, Bit Manipulation</td>
    <td></td>
  </tr>

  <tr>
    <td>1732</td>
    <td><a href="https://leetcode.com/problems/find-the-highest-altitude">Find the Highest Altitude</a></td>
    <td>2022-02-06</td>
    <td>Easy</td>
    <td>Array, Prefix Sum</td>
    <td></td>
  </tr>

  <tr>
    <td>1741</td>
    <td><a href="https://leetcode.com/problems/find-total-time-spent-by-each-employee">Find Total Time Spent by Each Employee</a></td>
    <td>2022-05-14</td>
    <td>Easy</td>
    <td>Database</td>
    <td></td>
  </tr>

  <tr>
    <td>1748</td>
    <td><a href="https://leetcode.com/problems/sum-of-unique-elements">Sum of Unique Elements</a></td>
    <td>2022-02-23</td>
    <td>Easy</td>
    <td>Array, Hash Table, Counting</td>
    <td></td>
  </tr>

  <tr>
    <td>1757</td>
    <td><a href="https://leetcode.com/problems/recyclable-and-low-fat-products">Recyclable and Low Fat Products</a></td>
    <td>2022-03-27</td>
    <td>Easy</td>
    <td>Database</td>
    <td></td>
  </tr>

  <tr>
    <td>1768</td>
    <td><a href="https://leetcode.com/problems/merge-strings-alternately">Merge Strings Alternately</a></td>
    <td>2022-02-20</td>
    <td>Easy</td>
    <td>Two Pointers, String</td>
    <td></td>
  </tr>

  <tr>
    <td>1773</td>
    <td><a href="https://leetcode.com/problems/count-items-matching-a-rule">Count Items Matching a Rule</a></td>
    <td>2022-02-01</td>
    <td>Easy</td>
    <td>Array, String</td>
    <td></td>
  </tr>

  <tr>
    <td>1795</td>
    <td><a href="https://leetcode.com/problems/rearrange-products-table">Rearrange Products Table</a></td>
    <td>2022-05-15</td>
    <td>Easy</td>
    <td>Database</td>
    <td></td>
  </tr>

  <tr>
    <td>1816</td>
    <td><a href="https://leetcode.com/problems/truncate-sentence">Truncate Sentence</a></td>
    <td>2022-02-01</td>
    <td>Easy</td>
    <td>Array, String</td>
    <td></td>
  </tr>

  <tr>
    <td>1832</td>
    <td><a href="https://leetcode.com/problems/check-if-the-sentence-is-pangram">Check if the Sentence Is Pangram</a></td>
    <td>2022-02-02</td>
    <td>Easy</td>
    <td>Hash Table, String</td>
    <td></td>
  </tr>

  <tr>
    <td>1844</td>
    <td><a href="https://leetcode.com/problems/replace-all-digits-with-characters">Replace All Digits with Characters</a></td>
    <td>2022-02-05</td>
    <td>Easy</td>
    <td>String</td>
    <td></td>
  </tr>

  <tr>
    <td>1859</td>
    <td><a href="https://leetcode.com/problems/sorting-the-sentence">Sorting the Sentence</a></td>
    <td>2022-02-01</td>
    <td>Easy</td>
    <td>String, Sorting</td>
    <td></td>
  </tr>

  <tr>
    <td>1873</td>
    <td><a href="https://leetcode.com/problems/calculate-special-bonus">Calculate Special Bonus</a></td>
    <td>2022-05-19</td>
    <td>Easy</td>
    <td>Database</td>
    <td></td>
  </tr>

  <tr>
    <td>1876</td>
    <td><a href="https://leetcode.com/problems/substrings-of-size-three-with-distinct-characters">Substrings of Size Three with Distinct Characters</a></td>
    <td>2022-02-12</td>
    <td>Easy</td>
    <td>Hash Table, String, Sliding Window, Counting</td>
    <td></td>
  </tr>

  <tr>
    <td>1920</td>
    <td><a href="https://leetcode.com/problems/build-array-from-permutation">Build Array from Permutation</a></td>
    <td>2022-01-30</td>
    <td>Easy</td>
    <td>Array, Simulation</td>
    <td></td>
  </tr>

  <tr>
    <td>1929</td>
    <td><a href="https://leetcode.com/problems/concatenation-of-array">Concatenation of Array</a></td>
    <td>2022-01-22</td>
    <td>Easy</td>
    <td>Array</td>
    <td></td>
  </tr>

  <tr>
    <td>1935</td>
    <td><a href="https://leetcode.com/problems/maximum-number-of-words-you-can-type">Maximum Number of Words You Can Type</a></td>
    <td>2022-02-20</td>
    <td>Easy</td>
    <td>Hash Table, String</td>
    <td></td>
  </tr>

  <tr>
    <td>1945</td>
    <td><a href="https://leetcode.com/problems/sum-of-digits-of-string-after-convert">Sum of Digits of String After Convert</a></td>
    <td>2022-02-07</td>
    <td>Easy</td>
    <td>String, Simulation</td>
    <td></td>
  </tr>

  <tr>
    <td>1967</td>
    <td><a href="https://leetcode.com/problems/number-of-strings-that-appear-as-substrings-in-word">Number of Strings That Appear as Substrings in Word</a></td>
    <td>2022-02-20</td>
    <td>Easy</td>
    <td>String</td>
    <td></td>
  </tr>

  <tr>
    <td>2000</td>
    <td><a href="https://leetcode.com/problems/reverse-prefix-of-word">Reverse Prefix of Word</a></td>
    <td>2022-02-06</td>
    <td>Easy</td>
    <td>Two Pointers, String</td>
    <td></td>
  </tr>

  <tr>
    <td>2006</td>
    <td><a href="https://leetcode.com/problems/count-number-of-pairs-with-absolute-difference-k">Count Number of Pairs With Absolute Difference K</a></td>
    <td>2022-02-01</td>
    <td>Easy</td>
    <td>Array, Hash Table, Counting</td>
    <td></td>
  </tr>

  <tr>
    <td>2011</td>
    <td><a href="https://leetcode.com/problems/final-value-of-variable-after-performing-operations">Final Value of Variable After Performing Operations</a></td>
    <td>2022-01-30</td>
    <td>Easy</td>
    <td>Array, String, Simulation</td>
    <td></td>
  </tr>

  <tr>
    <td>2032</td>
    <td><a href="https://leetcode.com/problems/two-out-of-three/">Two Out of Three</a></td>
    <td>2023-02-10</td>
    <td>Easy</td>
    <td>Array, Hash Table</td>
    <td></td>
  </tr>


  <tr>
    <td>2042</td>
    <td><a href="https://leetcode.com/problems/check-if-numbers-are-ascending-in-a-sentence">Check if Numbers Are Ascending in a Sentence</a></td>
    <td>2022-02-20</td>
    <td>Easy</td>
    <td>String</td>
    <td></td>
  </tr>

  <tr>
    <td>2053</td>
    <td><a href="https://leetcode.com/problems/kth-distinct-string-in-an-array">Kth Distinct String in an Array</a></td>
    <td>2022-02-05</td>
    <td>Easy</td>
    <td>Array, Hash Table, String, Counting</td>
    <td></td>
  </tr>

  <tr>
    <td>2068</td>
    <td><a href="https://leetcode.com/problems/check-whether-two-strings-are-almost-equivalent">Check Whether Two Strings are Almost Equivalent</a></td>
    <td>2022-02-27</td>
    <td>Easy</td>
    <td>Hash Table, String, Counting</td>
    <td></td>
  </tr>

  <tr>
    <td>2085</td>
    <td><a href="https://leetcode.com/problems/count-common-words-with-one-occurrence">Count Common Words With One Occurrence</a></td>
    <td>2022-02-05</td>
    <td>Easy</td>
    <td>Array, Hash Table, String, Counting</td>
    <td></td>
  </tr>

  <tr>
    <td>2089</td>
    <td><a href="https://leetcode.com/problems/find-target-indices-after-sorting-array">Find Target Indices After Sorting Array</a></td>
    <td>2022-02-01</td>
    <td>Easy</td>
    <td>Array, Binary Search, Sorting</td>
    <td></td>
  </tr>

  <tr>
    <td>2103</td>
    <td><a href="https://leetcode.com/problems/rings-and-rods">Rings and Rods</a></td>
    <td>2022-02-20</td>
    <td>Easy</td>
    <td>Hash Table, String</td>
    <td></td>
  </tr>

  <tr>
    <td>2108</td>
    <td><a href="https://leetcode.com/problems/find-first-palindromic-string-in-the-array">Find First Palindromic String in the Array</a></td>
    <td>2022-02-01</td>
    <td>Easy</td>
    <td>Array, Two Pointers, String</td>
    <td></td>
  </tr>

  <tr>
    <td>2114</td>
    <td><a href="https://leetcode.com/problems/maximum-number-of-words-found-in-sentences">Maximum Number of Words Found in Sentences</a></td>
    <td>2022-01-30</td>
    <td>Easy</td>
    <td>Array, String</td>
    <td></td>
  </tr>

  <tr>
    <td>2119</td>
    <td><a href="https://leetcode.com/problems/a-number-after-a-double-reversal">A Number After a Double Reversal</a></td>
    <td>2022-02-08</td>
    <td>Easy</td>
    <td>Math</td>
    <td></td>
  </tr>

  <tr>
    <td>2124</td>
    <td><a href="https://leetcode.com/problems/check-if-all-as-appears-before-all-bs">Check if All A's Appears Before All B's</a></td>
    <td>2022-02-20</td>
    <td>Easy</td>
    <td>String</td>
    <td></td>
  </tr>

  <tr>
    <td>2129</td>
    <td><a href="https://leetcode.com/problems/capitalize-the-title">Capitalize the Title</a></td>
    <td>2022-02-20</td>
    <td>Easy</td>
    <td>String</td>
    <td></td>
  </tr>

  <tr>
    <td>2138</td>
    <td><a href="https://leetcode.com/problems/divide-a-string-into-groups-of-size-k">Divide a String Into Groups of Size k</a></td>
    <td>2022-02-27</td>
    <td>Easy</td>
    <td>String, Simulation</td>
    <td></td>
  </tr>

  <tr>
    <td>2149</td>
    <td><a href="https://leetcode.com/problems/rearrange-array-elements-by-sign">Rearrange Array Elements by Sign</a></td>
    <td>2022-05-23</td>
    <td>Medium</td>
    <td>Array, Two Pointers, Simulation</td>
    <td></td>
  </tr>

  <tr>
    <td>2154</td>
    <td><a href="https://leetcode.com/problems/keep-multiplying-found-values-by-two">Keep Multiplying Found Values by Two</a></td>
    <td>2022-02-26</td>
    <td>Easy</td>
    <td>Array, Hash Table, Sorting, Simulation</td>
    <td></td>
  </tr>

  <tr>
    <td>2160</td>
    <td><a href="https://leetcode.com/problems/minimum-sum-of-four-digit-number-after-splitting-digits">Minimum Sum of Four Digit Number After Splitting Digits</a></td>
    <td>2022-02-05</td>
    <td>Easy</td>
    <td>Math, Greedy, Sorting</td>
    <td></td>
  </tr>

  <tr>
    <td>2161</td>
    <td><a href="https://leetcode.com/problems/partition-array-according-to-given-pivot">Partition Array According to Given Pivot</a></td>
    <td>2022-02-05</td>
    <td>Medium</td>
    <td>Array, Two Pointers, Simulation</td>
    <td></td>
  </tr>

  <tr>
    <td>2169</td>
    <td><a href="https://leetcode.com/problems/count-operations-to-obtain-zero">Count Operations to Obtain Zero</a></td>
    <td>2022-02-26</td>
    <td>Easy</td>
    <td>Math, Simulation</td>
    <td></td>
  </tr>

  <tr>
    <td>2176</td>
    <td><a href="https://leetcode.com/problems/count-equal-and-divisible-pairs-in-an-array">Count Equal and Divisible Pairs in an Array</a></td>
    <td>2022-02-19</td>
    <td>Easy</td>
    <td>Array</td>
    <td></td>
  </tr>

  <tr>
    <td>2177</td>
    <td><a href="https://leetcode.com/problems/find-three-consecutive-integers-that-sum-to-a-given-number">Find Three Consecutive Integers That Sum to a Given Number</a></td>
    <td>2022-02-19</td>
    <td>Medium</td>
    <td>Math, Simulation</td>
    <td></td>
  </tr>

  <tr>
    <td>2180</td>
    <td><a href="https://leetcode.com/problems/count-integers-with-even-digit-sum">Count Integers With Even Digit Sum</a></td>
    <td>2022-02-20</td>
    <td>Easy</td>
    <td>Math, Simulation</td>
    <td></td>
  </tr>

  <tr>
    <td>2181</td>
    <td><a href="https://leetcode.com/problems/merge-nodes-in-between-zeros">Merge Nodes in Between Zeros</a></td>
    <td>2022-02-20</td>
    <td>Medium</td>
    <td>Linked List, Simulation</td>
    <td></td>
  </tr>

  <tr>
    <td>2185</td>
    <td><a href="https://leetcode.com/problems/counting-words-with-a-given-prefix">Counting Words With a Given Prefix</a></td>
    <td>2022-02-27</td>
    <td>Easy</td>
    <td>Array, String</td>
    <td></td>
  </tr>

  <tr>
    <td>2194</td>
    <td><a href="https://leetcode.com/problems/cells-in-a-range-on-an-excel-sheet">Cells in a Range on an Excel Sheet</a></td>
    <td>2022-03-06</td>
    <td>Easy</td>
    <td>String</td>
    <td></td>
  </tr>

  <tr>
    <td>2235</td>
    <td><a href="https://leetcode.com/problems/add-two-integers">Add Two Integers</a></td>
    <td>2022-05-14</td>
    <td>Easy</td>
    <td>Math</td>
    <td></td>
  </tr>

  <tr>
    <td>2236</td>
    <td><a href="https://leetcode.com/problems/root-equals-sum-of-children">Root Equals Sum of Children</a></td>
    <td>2022-05-18</td>
    <td>Easy</td>
    <td>Tree, Binary Tree</td>
    <td></td>
  </tr>

  <tr>
    <td>2260</td>
    <td><a href="https://leetcode.com/problems/minimum-consecutive-cards-to-pick-up/description/">Minimum Consecutive Cards to Pick Up</a></td>
    <td>2023-02-10</td>
    <td>Medium</td>
    <td>Array, Hash Table, Sliding Window</td>
    <td></td>
  </tr>

  <tr>
    <td>2469</td>
    <td><a href="https://leetcode.com/problems/convert-the-temperature">Convert the Temperature</a></td>
    <td>2023-01-29</td>
    <td>Easy</td>
    <td>Math</td>
    <td></td>
  </tr>

</table>