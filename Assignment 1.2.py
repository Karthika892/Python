#Assignment 1.2
#1 all methods of lists
a=[3,1,5,43,16,4,3,9,5,79]
b=[22,4,87]
a.append(7)
a
a.clear()
a
a.copy()
a
a.count(5)
a
a.extend(b)
print(a)
x=a.index(16)
print(x)
a.insert(1,5)
print(a)
a.pop(3)
print(a)
a.remove(79)
print(a)
a.reverse()
print(a)
b.sort()
print(b)


#2 all methods of strings
txt="They plays football"
x=txt.capitalize()
print(x)

x=txt.casefold()
print(x)

x=txt.center(20)
print(x)

x=txt.count("plays")
print(x)

x=txt.encode()
print(x)

x=txt.endswith(".")
print(x)

x=txt.find("y")
print(x)

c="There are {number} players"
print(c.format(number==" 11"))

x=txt.index("football")
print(x)

x=txt.isalnum()
print(x)

x=txt.isalpha()
print(x)

x=txt.isdecimal()
print(x)

z="234453434"
d=z.isdigit()
print(d)

x=txt.isidentifier()
print(x)

x=txt.islower()
print(x)

x=txt.isnumeric()
print(x)

x=txt.isprintable()
print(x)

x=txt.isspace()
print(x)

x=txt.istitle()
print(x)

x=txt.isupper()
print(x)

l1=("They","are","going")
l2=".".join(l1)
print(l2)

l3="cooking"
l4=l3.ljust(30)
print(l4,"is my passion")

l5="DAUGHTER"
l6=l5.lower()
print(l6)

l7="Karthika "
l8=l7.lstrip()
print("hi my name is", l8, "from Kerala")

l10=l7.rstrip()
print("hi my name is", l10,"from Kerala")

l11=txt.strip()
print("hi my name is", l7,"from Kerala")
      
l9="hello"
mytable=l9.maketrans("h","c")
print(l9.translate(mytable))

l10=l9.upper()
print(l10)

m1="can you borrow be a pen"
m2=m1.partition("borrow")
print(m2)

m3=m1.replace("borrow","give")
print(m3)

m4=m1.rfind("borrow")
print(m4)

m5=m1.rindex("you")
print(m5)

txt1="Shami"
t1=txt1.rjust(10)
print(t1, "is a player")

m6="i ate chocolates, chocolates are my favourite"
m7=m6.rpartition("chocolates")
print(m7)

m8="apple,orange,cherry"
m9=m8.rsplit(",")
print(m9)

m10=m6.split()
print(m10)

r1="hi,i am going to mumbai"
r2=r1.splitlines()
print(r2)

r3=r1.startswith("hi")
print(r3)

r4=t1.swapcase()
print(r4)

r5=r1.title()
print(r5)

r6="53"
r7=r6.zfill(5)
print(r7)

#3-usage of negative index
#we can use

#eg
a="Nice to meet you"
print(a[-4:-1])