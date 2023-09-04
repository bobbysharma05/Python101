'''Chef has infinite coins in denominations of rupees 
5
5 and rupees 
10
10.

Find the minimum number of coins Chef needs, to pay exactly 
�
X rupees. If it is impossible to pay 
�
X rupees in denominations of rupees 
5
5 and 
10
10 only, print 
−
1
−1.

Input Format
First line will contain 
�
T, number of test cases. Then the test cases follow.
Each test case contains of a single integer 
�
X.
Output Format
For each test case, print a single integer - the minimum number of coins Chef needs, to pay exactly 
�
X rupees. If it is impossible to pay 
�
X rupees in denominations of rupees 
5
5 and 
10
10 only, print 
−
1
−1.'''
t = int(input())
for i in range(0,t):
    x = int(input())
    if x%10==0 and x%5==0:
        print(min(x//10,x//5))
    elif x%5==0 and  x%10!=0:
        print(x//5- round(x//10))
    else:
        print(-1)
    