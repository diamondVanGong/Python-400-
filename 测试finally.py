#测试finally
try:
    f=open("d/a.txt","r")
    content=f.readline()
    print(content)
except:
    print("文件没有找到！！")
finally:
    printf("run in finally ,关闭资源！！")
    try:
        f.close()
    except BaseException as e:
        print(e)
print("程序执行结束！！！")

