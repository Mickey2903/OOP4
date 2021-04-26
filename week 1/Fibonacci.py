numbers = int(input('How many numbers do you want: '))
numbers = numbers - 2

x = 0
y = 1

print(x)
print(y)

for  val in range(numbers):
    ans = x + y
    print(ans)
    x = y
    y = ans
