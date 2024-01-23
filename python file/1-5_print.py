fp=open('note.txt','w') #打开文件，w-->write
print('HeloWorld',file=fp) #输出(写入)内容
fp.close() #写完内容后要进行关闭