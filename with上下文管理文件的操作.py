#with上下文管理文件的操作
#注意:with不是用来取代try...expect..finally结构的，只是用来作为补充
#方便我们在进行文件管理，网络通信时候的开发
with open("d:/bb.txt") as f:
    for line in f:
        print(line)