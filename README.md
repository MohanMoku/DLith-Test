# DLithe-Test

# DLithe Company - Training Overview

**DLithe** is a professional technology solutions company focused on bridging the gap between academia and industry.  
They conducted a **1-week training session** that covered key **technical concepts** aimed at enhancing practical knowledge and industry readiness among students.

The training was interactive, informative, and provided valuable insights into real-world technical applications.

---
# Test
Last day they conducted a technical test on solving a coding problems

## Given Questions are 


### Question 1

There are **n houses** built in a line, each of which contains some value in it.

A thief is going to steal the maximal value of these houses, but he can't steal from two adjacent houses because the owner of the stolen houses will tell his two neighbors (left and right side).

*What is the maximum stolen value?*

#### Example:
    Input: val[] = {6, 7, 1, 3, 8, 2, 5}

    output: 20
    Explanation: 6 + 1 + 8 + 5 = 20

* By using Recursion we can solve this

#### Code:
```python
class Solution:
    def thief_problem(self, arr, got_now):

        if len(arr) == 0:
            return 0

        b = self.thief_problem(arr[1:], got_now)
        got_now_temp = got_now + arr[0]
        a = arr[0] + self.thief_problem(arr[2:], got_now_temp)

        return max(a,b)
```
---
### Question 2

print the pattern

#### Example:
    Input: 5

    output: 11112
            32222
            33334
            54444
            55556

* if row number is odd increase number in last
* if row number is even increase number in first

#### Code:
```python
class Solution:
    def pattern(self, n):
        for i in range(1, n+1):
            if i % 2 == 1:
                print( f'{i}' * (n-1) + f'{i+1}' )
            else:
                print( f'{i+1}' + f'{i}'*(n-1) )
```
---
### Question 3

Write programs to find first n **Disarium numbers** and Disarium numbers between two given numbers.

A number is said to be Disarium if it isi equal to sum of its digits raised to the power of their respective position in number.

#### Example:
135 is a Disarium number  
**Explanation:**  
135 = 1<sup>1</sup> + 3<sup>2</sup> + 5<sup>3</sup>  
135 = 1 + 9 + 125

#### Code to find if the number is Disarium or not
```python
class Solution:
    def disarium(self, n):
        sum = 0
        number_list = str(n)
        for i, num in enumerate(number_list,1):
            sum += (int(num)**i)
        if sum == n:
            return True
        else:
            return False
```
#### Sub Question 1
    For finding Disarium numbers upto n
    Input: 100
    Output: [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 89]

#### Code:
```python
class Solution:
    def disarium_upto_n(self, n):
        list_of_disarium = list()
        for i in range(n+1):
            if self.disarium(i):
                list_of_disarium.append(i)
        print(f'upto {n} disarium numbers are:\n', list_of_disarium)
```
#### Sub Question 2
    For finding Disarium numbers in given range
    Input: 1 to 200
    Output: [1, 2, 3, 4, 5, 6, 7, 8, 9, 89, 135, 175]

#### Code:
```python
class Solution:
    def disarium_in_range(self, a, b):

        list_of_disarium = list()
        for i in range(a, b+1):
            if self.disarium(i):
                list_of_disarium.append(i)
        
        print(f'disarium numbers in range {a}, {b}:\n', list_of_disarium)
```
---
<br/>

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;I would like to extend my sincere gratitude to ***Merwin Dsouza*** for their invaluable guidance and support throughout my learning journey. Their exceptional problem-solving skills and insightful approach have significantly contributed to my growth and understanding of **technical concepts of programming**. I truly appreciate the opportunity to learn under their mentorship and am grateful for the impact they've had on my development of **coding proficiency, algorithm design, and logical thinking**.

Thank you for your continued support and dedication.

**Thank you *DLithe***