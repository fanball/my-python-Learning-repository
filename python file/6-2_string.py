print("这是")
print("个啥") #两行print，输出的结果也会换行
print("------------------")

print("这是\n个啥") #转义字符\n的作用：换行
print("Hello\tWould") #转义字符\t作用：制表位
print("\'这是个啥\'") #转义字符\'作用：加上'
print("\"这是个啥\"") #转义字符\"作用：加上"
print("\\这是个啥\\") #转义字符\\作用：加上\
#制表位：输出空格的个数=8-转义字符前面的字符个数

print("我\n嘞\n个\n豆")
print(r"我\n嘞\n个\n豆")
print(R"我\n嘞\n个\n豆") #r或R让后面的转义字符失效