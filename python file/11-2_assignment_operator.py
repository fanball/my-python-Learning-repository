#赋值运算符的示例
x=10 #先设两个变量x、y
y=3
x+=y
print(x) #展开：x=x+y
x-=y
print(x) #展开：x=x-y
x*=y
print(x) #展开：x=x*y
x/=y
print(x) #展开：x=x/y
x%=y
print(x) #展开：x=x%y
x**=y
print(x) #展开：x=x**y
x//=y
print(x) #展开：x=x//y

print("----------------------")
#链式赋值的示例
a=b=c=25
print(a,b,c)
#系列解包赋值的示例
a,b,c=4,5,6
print(a,b,c)
#交换变量的示例
a=114
b=514
print(a,b)
a,b=b,a
print(a,b)