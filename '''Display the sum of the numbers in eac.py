'''Display the sum of the numbers in each set. You are given hundred numbers divided
in ten sets in the following order.
Set 1: 1-10
Set 2: 11-20
Set 3: 21-30
....
Set 10: 91-100'''


sets = []
for i in range(1, 101, 10):
    num1 = list(range(i, i + 10))
    sets.append(num1)
    n = (i - 1) // 10 + 1 
    print("Set", n, " = ", num1)
    print("Sum is",sum(num1))