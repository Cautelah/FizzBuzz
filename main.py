n = 100
for i in range(1,n+1): print("Fizz"*(i%3<1)+(i%5<1)*"Buzz" or i)