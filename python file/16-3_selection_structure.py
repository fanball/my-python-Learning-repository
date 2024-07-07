#选择结构if-elif-else
score=int(input("请输入您的的成绩:"))
if score<0 or score>100:
    print("输入的成绩无效")
elif 0<=score<60:
    print("成绩为E")
elif 60<=score<70:
    print("成绩为D")
elif 70<=score<80:
    print("成绩为C")
elif 80<=score<90:
    print("成绩为B")
else:
    print("成绩为A")
print("程序结束")