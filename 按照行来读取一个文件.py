with open(r"bb","r")as f:
    while True:
        fragment=f.readline()
        if not fragment:
            break
        else:
            print(fragment,end=" ")