dict={}

n=int(input("enter the number of entries you want to enter"))

for i in range(1,n+1):
    name =input("enter the name of the student")
    sid=int(input("enter the sid of the student"))
    dict.update({sid:name})
    
print(dict)

sortedbyKEY={k:v for k, v in sorted(dict.items())}
print(sortedbyKEY)

sortedbyvalues={k:v for k, v in sorted(dict.items(), key=lambda x:x[1]) }
print(sortedbyvalues)

key_sid=int(input("enter the sid of the student you want to search for"))
if key_sid in dict.keys():
    value=dict[key_sid]
    print(value)


    