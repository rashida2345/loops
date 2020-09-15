Number = int(input("enter the value:"))
a=0
b=1
for Num in range(0, Number):
    if(Num <= 1):
        Next= Num
    else:
            Next= a+b
            a=b
            b=Next
            print(Next)
            
            
