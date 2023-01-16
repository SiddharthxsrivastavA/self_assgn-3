sp=0
st=75

for i in range(1,7):
    for j in range(1,sp+1):
        print(" ", end="")
    for k in range(65,st+1):
        print(chr(k),end=" ")
    
    print()
    sp+=2 
    st-=2