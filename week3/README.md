# Subarray Division 2

Two children, Lily and Ron, want to share a chocolate bar. Each of the squares has an integer on it.

Lily decides to share a contiguous segment of the bar selected such that:

The length of the segment matches Ron's birth month, and,
The sum of the integers on the squares is equal to his birth day.
Determine how many ways she can divide the chocolate.

*Example*

<em>s = </em>[2, 2, 1, 3, 2]
<em>d</em>= 4
<em>m</em>= 2

Lily wants to find segments summing to Ron's birth day, <em>d = 4</em> with a length equalling his birth month, <em>m = 2</em>. In this case, there are two segments meeting her criteria: [2, 2] and [1, 3].

Function Description

Complete the birthday function in the editor below.

birthday has the following parameter(s):

int s[n]: the numbers on each of the squares of chocolate
int d: Ron's birth day
int m: Ron's birth month

Returns

int: the number of ways the bar can be divided

The first line contains an integer , the number of squares in the chocolate bar.
The second line contains <em>n</em> space-separated integers <em>s[i]</em>, the numbers on the chocolate squares where i is between 0 and <em>n</em>.
The third line contains two space-separated integers,  and , Ron's birth day and his birth month.