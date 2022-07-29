# Lonely Integer

<a href="https://www.python.org/" title="Python"><img src="https://github.com/get-icon/geticon/raw/master/icons/python.svg" alt="Python" width="51px" height="51px"></a>

Given an array of integers, where all elements but one occur twice, find the unique element.

<b>Example</b>

a = [1, 2, 3, 4, 3, 2, 1]

The unique element is 4

<b>Function Description</b>

Complete the lonelyinteger function in the editor below.

lonelyinteger has the following parameter(s):

int a[n]: an array of integers

<b>Returns</b>

int: the element that occurs only once

<b>Input Format</b>

The first line contains a single integer, n, the number of integers in the array.
The second line contains n space-separated integers that describe the values in a.

# Grading Students

<a href="https://www.python.org/" title="Python"><img src="https://github.com/get-icon/geticon/raw/master/icons/python.svg" alt="Python" width="51px" height="51px"></a>

HackerLand University has the following grading policy:

Every student receives a grade in the inclusive range from 0 to 100.
Any grade less than 40 is a failing grade.
Sam is a professor at the university and likes to round each student's grade according to these rules:

<ul>
    <li>If the difference between the grade and the next multiple of 5 is less than 3, round grade up to the next multiple of 5.</li>
    <li>If the value of grade is less than 38, no rounding occurs as the result will still be a failing grade.</li>
</ul>

<b>Examples</b>

<ul>
    <li>
        <em>grade</em> = 84 round to 85 (85-84 is less than 3)
    </li>
    <li>
        <em>grade</em> = 29 do not round (result less than 40
    </li>
    <li>
        <em>grade</em> = 57 do not round (60-57 is 3 or higher)
    </li>
</ul>

Given the initial value of <em>grade</em> for each of Sam's n students, write code to automate the rounding process.

<b>Function Description</b>

Complete the function gradingStudents in the editor below.

gradingStudents has the following parameter(s):

int grades[n]: the grades before rounding

<b>Returns</b>

int[n]: the grades after rounding as appropriate

<b>Input Format</b>

The first line contains a single integer, n, the number of students.
Each line  of the  subsequent lines contains a single integer, grades[i].


# Flipping bits

<a href="https://www.python.org/" title="Python"><img src="https://github.com/get-icon/geticon/raw/master/icons/python.svg" alt="Python" width="51px" height="51px"></a>

You will be given a list of 32 bit unsigned integers. Flip all the bits (1 => 0 and 0 => 1) and return the result as an unisigned integer.

<b>Example</b>

<em>n = 910