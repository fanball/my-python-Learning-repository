#嵌套结构if
answer=input("请输入您是否喝酒(y/n):")
if answer=="y":
    proof=input("请输入酒精含量:")
    if proof<20:
        print("您未达到酒驾标准，可以驾驶")
    elif proof<80:
        print("您已达到酒驾标准，请勿驾驶")
    else:
        print("您已达到醉驾标准，请勿驾驶")
else:
    print("您未喝酒，可以驾驶")