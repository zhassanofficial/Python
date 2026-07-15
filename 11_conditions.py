#num1 = int(input("enter 1 number ; "))
#num2 = int(input("enter 2 number ; "))
#num3 = int(input("enter 3 number ; "))
#num4 = int(input("enter 4 number ; "))
#
#if(num1 > num2 and num1 > num3 and num1 > num4 ):
#    print("The Greater number is 1 st ;  ", num1)
#
#elif(num2 > num1 and num2 > num3 and num2 > num4 ):
#    print("The number 2nd is Greater ;", num2)
#elif(num3 > num1 and num3 > num2 and num3 > num4 ):
#    print("The Greater number is  3rd ; ", num3)
#elif(num4 > num2 and num4 > num3 and num4 > num1 ):
#    print("The Greater number is 4th ; ", num1)

p1 = " Make a lot of money"
p2 = "buy now"
p3 = "subcribe this "
p4 = " click this"

message = input("Enter your comment : ")
if((p1 in message) or (p2 in message) or (p3 in message) or (p4 in message)):
    print("This is a spam Message")
else:
    print("Its not a spam")