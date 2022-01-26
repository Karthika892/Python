#Assignment 2.2
#1 Step function in for loop
for i in range(1,100,2):
    print(i)

#2 Infinte for loop
i=[1]
for j in i:
    i.append(j+1)
    print(j)

#3 Adding values in a tuple
Y=("children","playing")
a=list(Y)
a.append("today")
print(a)
Y=tuple(a)
print(Y)