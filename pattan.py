number = int(input("Enter The last Number : "))
print(number)
for row in range(1,number):
    for colume in range(1, row + 1):
        print(colume, end = ' ')
    print("")
