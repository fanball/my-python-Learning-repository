#python中的保留字查看方法
import keyword #导入关键字
print(keyword.kwlist) #列出所有保留字
print("保留字的个数:",len(keyword.kwlist)) #获取保留字的个数