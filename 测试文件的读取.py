#测试文件的读取
with open(r"e.txt","r",encoding="utf-8") as f:
    str=f.read(10)
    print(str)