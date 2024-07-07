#选择结构if-else 双分支结构
number=eval(input("请输入您的中奖号码:"))
if number==114514:
    print("恭喜您中奖了!")
else:
    print("很遗憾，您没有中奖")

#第二种简化表达式
print("--------以下是第二种简化表达式的输出结果--------")
result="恭喜你中级了" if number==114514 else "很遗憾，您没有中奖"
print(result)

#第三种简化表达式
print("--------以下是第三种简化表达式的输出结果--------")
print("恭喜你中级了" if number==114514 else "很遗憾，您没有中奖")