# Picking Numbers
<a href="https://www.python.org/" title="Python"><img src="https://github.com/get-icon/geticon/raw/master/icons/python.svg" alt="Python" width="51px" height="51px"></a>

Given an array of integers, find the longest subarray where the absolute difference between any two elements is less than or equal to 1.

<b>Example</b>

<em>a = [1, 1, 2, 2, 3, 3, 4, 4, 5, 5, 5]</em>

There are two subarrays meeting the criterion: <em>[1, 1, 2, 2]</em> and <em>[4, 4, 5, 5, 5].</em>The maximum length subarray has 5 elements.

<b>Function Description</b>

Complete the pickingNumbers function in the editor below.

pickingNumbers has the following parameter(s):

int a[n]: an array of integers.

<b>Returns</b>

int: the length of the longest subarray that meets the criterion

<b>Input Format</b>

he first line contains a single integer <em>n</em>, the size of the array <em>a</em>.
The second line contains  space-separated integers, each an <em>a[i]</em>.

# Left Rotation
<a href="https://developer.mozilla.org/en-US/docs/Web/JavaScript" title="JavaScript"><img src="https://github.com/get-icon/geticon/raw/master/icons/javascript.svg" alt="JavaScript" width="51px" height="51px"></a>

A left rotation operation on an array of size <em>n</em> shifts each of the array's elements 1 unit to the left. Given an integer,<em>d</em> , rotate the array that many steps left and return the result.

<b>Example</b>

<em>d = 2</em>
<em>arr = [1, 2, 3, 4, 5]</em>
After 2 rotations, <em>arr' = [3, 4, 5, 1, 2]</em>.

<b>Function Description</b>

Complete the rotateLeft function in the editor below.

rotateLeft has the following parameters:

int d: the amount to rotate by
int arr[n]: the array to rotate

<b>Returns</b>

int[n]: the rotated array

<b>Input Format</b>

The first line contains two space-separated integers that denote <em>n</em>, the number of integers, and <em>d</em>, the number of left rotations to perform.
The second line contains <em>n</em> space-separated integers that describe <em>arr[]</em>.

<b>Sample Input</b>

5 4
1 2 3 4 5

<b>Sample Output</b>

5 1 2 3 4


# Number Line Jumps
<a href="https://developer.mozilla.org/en-US/docs/Web/JavaScript" title="JavaScript"><img src="https://github.com/get-icon/geticon/raw/master/icons/javascript.svg" alt="JavaScript" width="51px" height="51px"></a>

You are choreographing a circus show with various animals. For one act, you are given two kangaroos on a number line ready to jump in the positive direction (i.e, toward positive infinity).

The first kangaroo starts at location  and moves at a rate of  meters per jump.
The second kangaroo starts at location  and moves at a rate of  meters per jump.
You have to figure out a way to get both kangaroos at the same location at the same time as part of the show. If it is possible, return YES, otherwise return NO.

<b>Example</b>

<em>X1 = 2</em>
<em>V1 = 1</em>
<em>X2 = 1</em>
<em>V2 = 2</em>

After one jump, they are both at <em>x = 3, (<em>X1 + V1 = 2 + 1, X2 + V2 = 1 + 2</em>), so the answer is YES.

<b>Function Description</em>

Complete the function kangaroo.

kangaroo has the following parameter(s):

int x1, int v1: starting position and jump distance for kangaroo 1
int x2, int v2: starting position and jump distance for kangaroo 2

<b>Returns</em>

string: either YES or NO

<b>Input Format</b>

A single line of four space-separated integers denoting the respective values of <em>X1</em>,<em>V1</em> , <em>X2</em>, and <em>V2</em>.


# Tower Breakers

<a href="https://www.python.org/" title="Python"><img src="https://github.com/get-icon/geticon/raw/master/icons/python.svg" alt="Python" width="51px" height="51px"></a>

Two players are playing a game of Tower Breakers! Player 1 always moves first, and both players always play optimally.The rules of the game are as follows:

<ul>
    <li>Initially there are n towers</li>
    <li>Each tower is of height m</li>
    <li>The players move in alternating turns</li>
    <li>
        In each turn, a player can choose a tower of height <em>x</em> and reduce its height to <em>y</em>. Where 1 <= <em>y</em><<em>x</em> and <em>y</em>evenly divides <em>x</em>
    </li>
    <li>If the current player is unable to make a move, they lose the game.</li>
</ul>

Given the values of <em>n</em> and <em>m</em>, determine which player will win. If the first player wins, return 1. Otherwise, return 2.

<b>*Example*</b>
<em>n = 2</em>
<em>m = 6</em>

There are 2 towers, each 6 units tall. Player 1 has a choice of two moves:
- remove 3 pieces from a tower to leave 3 as 6 module 3 = 0
- remove 5 pieces to leave 1.

Let Player 1 remove 3. Now the towers are 3 and  6 units tall.

Player 2 matches the move. Now the towers are both 3 units tall.

Now Player 1 has only one move.

Player 1 removes 2 pieces leaving 1. Towers are 1 and 2 units tall.
Player 2 matches again. Towers are both 1 unit tall.

Player 1 has no move and loses. Return 2.

<b>Function Description</b>

int n: the number of towers
int m: the height of each tower

<b>Returns</b>
int: the winner of the game

<b>Input Format</b>

The first line contains a single integer t, the number of test cases.
Each of the next t lines describes a test case in the form of 2 space-separated integers, n and m.

<b>Sample input</b>

STDIN   Function
-----   --------
2       t = 2
2 2     n = 2, m = 2
1 4     n = 1, m = 4

<b>Sample output</b>

2
1