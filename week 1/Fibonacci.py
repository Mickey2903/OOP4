numbers = int(input('How many numbers do you want: '))

x = 0
y = 1

if numbers > 0:
    print(x)
if numbers > 1:
    print(y)

numbers = numbers - 2

for  val in range(numbers):
    ans = x + y
    print(ans)
    x = y
    y = ans
