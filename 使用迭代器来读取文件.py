#使用迭代器来读取文本文件
with open(r"d:\bb.txt","r") as f:
    for a in f:
        print(a,end=" ")