s=input("please enter your string")

list1=s.split()

dict={}

if len(list1)!=1:

    for i in list1:
      var1=list1.count(i)
      dict.update({i:var1})

    print(dict)


dict2={}

if(len(list1)==1):
    
    for i in list1:
        var2=list1.count(i)
        dict2.update({i:var2})
    print(dict2)