f = open("studentnames.txt", "w")
while True:
    amount = int(input('How many students does your group have: '))

    if amount == 1:
        firstName = input('Please give your first name: ')
        f.write(firstName)
        f.write('\n')

        lastName = input('Please give your last name: ')
        f.write(lastName)
        break

        

    elif amount <= 0:
        print('Please give a real amount')
        continue

    else:
        name = input('Please give the first name: ')
        f.write(name)
        f.write('\n')
        
        for val in range(1, amount):
            name = input('Please give the next name: ')
            f.write(name)
            f.write('\n')
        break

f.close()

text = open("studentnames.txt")
content = text.read()
print("The file now contains:\n", content)

x = content.count("\n") 

y = content.count(' ')
characters = len(content) - x - y
print("The file now contains ", characters, " characters.")