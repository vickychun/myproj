
# coding: utf-8

str1 = "I am learning programming"
print(str1)
print(len(str1))

print(str1[5:])
print(str1[::-1])
#只有python才有

print("{0} {1}".format(100,200))
print("num1: {0} num2: {1}".format(1,2))
print("{0:10}{1:10}".format(200,300))
print("{0:<7}{1:<7}{2:<7}".format(123,456,789))

#5/11
x = [2,3,4]
for i in x:
    print(i, end=" ")
print()
for i in range(len(x)):
    print(x[i], end=" ")
print()

for idx, i in enumerate(x):
    print(idx+1,i,sep=":")
print()

x.append(5)
print(x)

y=[1,2]
z=x+y
print(x,y,z)
#加完是一個全新的list

z=x
z[0]=99
print(x,z,sep="\n")
#"z=x"代表兩者的起始位子一樣，x也會跟著一起被改

x.append(y)
print(x)
# y is a list

print(x[ len(x)-1 ])
print(x[-1])
x[2:3]=[90,91,92]
print(x)

def prList(arr):
  for idx,el in enumerate(arr):
    if (idx!=len(arr)-1):
      print(el,end=",")
    else:
      print(el)
a = [10,20,30,40,50]
prList(a)

def enumList(arr):
  for idx,el in enumerate(arr):
    print(idx+1,el,sep=". ")
    # print("{}. {}".format(idx+1,el))
b = ['apple','orange','banana'] 
enumList(b)