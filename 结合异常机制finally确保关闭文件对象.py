try:
    f=open(r"m01.txt","w")
    strs=["aa\n","bb\n","cc\n"]
    f.writelines(strs)
except BaseException as e:
    print(e)
finally:
    f.close()
