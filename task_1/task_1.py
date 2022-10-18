# oneline
n = int(input("Enter the number: "))
print(f'First method answer: {int(n * (n + 1) / 2)}')

#the second version
# normal
last = n
result = 0

for i in range(1, last + 1):
    result += i
print(f'Second method answer: {result}')
 