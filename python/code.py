a=[2,3,4,5,6,7,8,'aman','saksham','vaibhav',True,False]
x=[]
y=[]
z=[]

for i in a :
    if type(i)==int:
         x=x.append(i)
    elif type(i)==str:
         y=y.append(i)
    elif type(i)==bool:
        z=z.append(i)
print(x,y,z)
    
