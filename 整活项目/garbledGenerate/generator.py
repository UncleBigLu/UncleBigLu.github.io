import json
import random

def garbled():
    # Read garbled code files
    with open("dict.json","r") as f:
        garbled_dict = json.load(f)
    with open("random_array.json", mode="r") as f:
        garbled_array = json.load(f)
# Get user input
    origin_str = input("Please enter original string: \n")
    garbled_code = input("Please enter garbled code to be added(lower case letters only). \n\
        Other characters would be replaced by arbitrary garbled code\n")
    
    out_str = ""
    for c in origin_str:
        # Add original character
        out_str += c
        # Add garbled character
        for gc in reversed(garbled_code):
            if gc in garbled_dict:
                out_str += garbled_dict[gc]
            else:
                out_str += random.choice(garbled_array)
    
    print(out_str)

def mathematicalScript():
    with open('mathematical_bold_script.json', mode='r') as f:
        mscript_dict = json.load(f)

    outstr = ""
    str = input("Please enter original string\n")
    for c in str:
        if c in mscript_dict:
            # Convert the hex string character code to interger,
            # then convert it to corresponding character 
            outstr += chr(int(mscript_dict[c], 16))
        else:
            outstr += c
    print(outstr)

if __name__ == "__main__":
    cmd = ''
    while cmd != 'q':
        cmd = input("Please choose effects:\n\
            1. e\u0301\u0305r\u0306\u0307r\u0308\u0309o\u0310\u030Ar\n\
            2. mathematical bold script\n\
            q. quit\n")
        if cmd == '1':
            garbled()
        elif cmd == '2':
            mathematicalScript()
        else:
            break
