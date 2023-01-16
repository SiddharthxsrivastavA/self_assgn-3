day=int(input("enter the day"))
month=int(input("enter the month"))
year=int(input("enter the year"))
                      
if(1<=day<=31 and 1<=month<=12 and 1800<=year<=2025):
    month_30=[4,6,9,11]
    month_31=[1,3,5,7,8,10,12]
    
    if(month in month_30 and day<=30)==True:
        if(day==30):
            print("next date will be", "1","/",month+1,"/" ,year)
        else:
            print("next date will be", day,"/",month,"/",year)    
    elif(month in month_31 and day<=31)==True:
        if(day==31 and month!=12):
            print("next date will be", "1","/",month+1,"/" ,year)
        elif(day<31):
            print("next date will be", day,"/",month,"/",year)  
        elif(day==31 and month==12):
            print("next date will be", "1","/","1","/" ,year+1)
            
    elif(month==2):
        year_str=str(year)
    
        if(year_str[2]==0 and year_str[3]==0):
            if(year%400==0):
                if(day==29):
                    print("next date will be", "1","/",month+1,"/" ,year)
                elif(day<29):
                    print("next date will be", day,"/",month,"/",year)  
                
            
        elif(year%4==0):
            if(day==29):
                print("next date will be", "1","/",month+1,"/" ,year)
            elif(day<29):
                    print("next date will be", day,"/",month,"/",year)
            
            
            
            
        elif(year%4!=0):
            if(day==28):
                print("next date will be", "1","/",month+1,"/" ,year) 
            elif(day<28):
                    print("next date will be", day,"/",month,"/",year)