#Assignment 2.0
#1 methods of dictionary
l1={"name":"James","place":"Mumbai"}
l1.clear()
print(l1)

l2=l1.copy()
print(l2)

l3={"value1","value2","value3"}
l4=1
x=dict.fromkeys(l3,l4)
print(x)

l1={"name":"James","place":"Mumbai"}
l5=l1.get("name")
print(l5)

l6=l1.items()
print(l6)

l7=l1.keys()
print(l7)

l1.pop("place")
print(l1)

l1.popitem()
print(l1)

l8=l1.setdefault("place","Canada")
print(l8)

l1.update({"color": "blue"})
print(l1)

l9=l1.values()
print(l9)


#2 create a set
set1={"BMW","benz","swift"}
print(set1)

#3 sorted function
func=("21","43","12","68")
y=sorted(func,reverse=True)
print(y)

#4 filename
filename=input("input the filename:")
f_extns=filename.split(".")[-1]
print ("The extension of the file is: ",f_extns)

#5 Our owncalculator
def add(num1, num2): 
    return num1 + num2 
def subtract(num1, num2): 
    return num1 - num2 
def multiply(num1, num2): 
    return num1 * num2 
def divide(num1, num2): 
    return num1 / num2 
 

print("Please select operation :\n" 
        "1. Add\n" 
        "2. Subtract\n"  
        "3. Multiply\n" 
        "4. Divide\n") 

choice = int(input("Select operation 1, 2, 3, 4 :")) 

num1 = int(input("Enter first number: ")) 
num2 = int(input("Enter second number: ")) 

if choice == 1: 
    print(num1, "+", num2, "=",add(num1, num2)) 

elif choice == 2: 
    print(num1, "-", num2, "=",subtract(num1, num2)) 

elif choice == 3: 
    print(num1, "*", num2, "=",multiply(num1, num2)) 

elif choice == 4: 
    print(num1, "/", num2, "=",divide(num1, num2)) 

else: 
    print("not defined")