'''
Create a list of all odd numbers between 1 and a max number. Max number is 
something you need to take from a user using input() function
'''
oddNumbers = []
maxNumber = int(input())
for num in range(1,maxNumber+1):
    if num%2 != 0:
        oddNumbers.append(num)
print(oddNumbers)
    