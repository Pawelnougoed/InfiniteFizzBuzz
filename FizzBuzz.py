# FizzBuzz
n = 1
while n < 100:
    if (n%5==0) and (n%3==0):
        print('FizzBuzz')
        n = n+1
    elif (n%3==0):
        print('Fizz')
        n = n+1
    elif (n%5==0):
        print('Buzz')
        n = n+1

    else:
        print (n)
        n = n+1
    
input("Press Enter to exit...")
exit
