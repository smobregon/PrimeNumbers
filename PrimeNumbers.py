"""
number = int(input("Enter a number: "))


if number > 2 and number %2 == 0:
 
    for i in range(number):
        total = 0
        divisor = number/2 #+ number%2
    total += 1 + divisor + number
    print('Sigma(',number,') =',int(total))
    print(number, '+ 1 =', number+1)
    print(number,"is not prime")
elif number % 3 == 0:
    for i in range(number):
        total = 0
        divisor = number/3 #+ number%3
    total += 1 + divisor + number
    print('Sigma(',number,') =',int(total))
    print(number, '+ 1 =', number+1)
    print(number,"is not prime")
else:
    total = 0
    total += 1 + number
    print('Sigma(',number,') =',int(total))
    print(number,'+ 1 =',number+1)
    print(number,"is prime")
"""    

n = int(input("Enter a number: "))
sigma = 0 #create running total

for i in range(1,n+1): #test if 1 evenly divides with n
    if n % i == 0: #means it evenly divided
        sigma += i #add i to the total
        
if sigma == (n+1):
    print ("It is prime")

else:
    print("It is not prime")












    
