str=""
with open("hex_test", "r") as f:
    is_first = True
    key_index = ord('A')
    for line in f.readlines():
        if not is_first:
            str += ",\n"
        else:
            is_first = False

        if key_index - 1 == ord('Z'):
            key_index = ord('a')

        str = str + "\"" + chr(key_index) + "\": \""
        str += "0x"
        # str.strip() removes the \n at the end of a string
        str+=line[2:].strip()
        str += "\""
        key_index += 1
        
with open("out.json", mode="w") as f:
    f.write("{\n")
    f.write(str)
    f.write("\n}")


    

