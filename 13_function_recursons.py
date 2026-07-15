#def fun1(a,b):
#    return a+b
#    
#
#a = 55
#b = 5
#c = fun1(a,b)
#print(c)

#recursion
#def factorial(n):
#    if(n == 0 or n == 1):
#        return 1
#    else :
#        return n * factorial(n - 1)
#    
#n = int(input("enter a number you want to find factorial : "))   
#print(f"The factorial of {n} is : " , factorial(n))

def downcount(n):
    if(n == 0):
        print("Time's up")
    else:
        print(n)
        downcount(n - 1)


n = int(input("enter a number for downcount :"))
downcount(n)
