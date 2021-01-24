a=4
b=11
count=0
for i in range(a,b+1):
 for j in range(1,i):
 	if i%j==0:
 		count=count+1
 if count==1:
              print(i)	
 

