import json
import random

if __name__ == "__main__":
# Read garbled code files
    with open("dict.json","r") as f:
        garbled_dict = json.load(f)
    with open("random_array.json", mode="r") as f:
        garbled_array = json.load(f)
# Get user input
    origin_str = input("Please enter original string: ")
    garbled_code = input("Please enter garbled code to be added(lower case letters only). \n\
        Other characters would be replaced by arbitrary garbled code\n")
    
    out_str = ""
    for c in origin_str:
        out_str += c
        for gc in reversed(garbled_code):
            if gc in garbled_dict:
                out_str += garbled_dict[gc]
            else:
                out_str += random.choice(garbled_array)
    
    print(out_str)



  
