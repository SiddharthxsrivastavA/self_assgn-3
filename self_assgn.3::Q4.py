grade=int(input("enter the grade"))

if(grade<4 and grade>10 ):
    print("error! please enter a grade between 4 and 10")

else:
    if(grade==10):
        print("your grade is 'A+' and Outstanding Performance ")
    elif(grade==9):
        print("your grade is 'A' and Excellent Performance ")  
    elif(grade==8):
        print("your grade is 'B+' and Very Good Performance ")
    elif(grade==7):
        print("your grade is 'B' and Good Performance")
    elif(grade==6):
        print("your grade is 'C+' and Average Performance")
    elif(grade==5):
        print("your grade is 'C' and  Below Average Performance ")
    elif(grade==4):
        print("your grade is 'D' and Poor Performance ")
