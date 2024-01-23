x=10
y=3
z=x/y #在执行除法预算的时候，将预算的结果赋值给z
print(z,type(z)) #隐式转换，通过运算隐式的转成了结果的类型
print("----------------------")

#float类型转成int类型
print("float类型转成int类型:",int(3.14))

#将int转成float类型
print("int类型转成float类型:",float(10))

#将str转成int类型
print(int("100")+int("200"))