a=["我love you","尚学堂\n","百战陈新雇\n"]
b=enumerate(a)
print(a)
print(list(b))
c=[temp+"#"+str(index) for index,temp in enumerate(a)]
print(c)