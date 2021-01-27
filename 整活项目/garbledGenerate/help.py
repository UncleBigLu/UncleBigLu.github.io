str=""
with open("test.txt", "r") as f:
    is_first = True
    for line in f.readlines():
        if not is_first:
            str += ", "
        else:
            is_first = False

        str += "\"\\u"
        str+=line[2:].strip()
        str += "\""
        
with open("out.json", mode="w") as f:
    f.write("[")
    f.write(str)
    f.write("]")


    

