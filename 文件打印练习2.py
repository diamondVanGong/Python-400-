with open("e.txt", "r", encoding="utf-8") as f:
    lines = f.readlines()
    lines = [line.rstrip() + "#" + str(index) +"\n"+for index, line in enumerate(lines)]

with open("e.txt", "w", encoding="utf-8") as f:
    f.writelines(lines)