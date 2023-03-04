dic={"A":181,"B":182,
     "C":183,"D":184,
     "E":185,"F":181}

print(dic.keys())
print(dic.values())

for name in dic:
     print(name)

dic1 = {("A",1): 181, ("A",2): 182,
        ("C",3): 183, ("D",4): 184,
        ("E",5): 185, ("F",6): 181}

for (name , tel) in dic1:
    # print("name:"+name)
    # print("tel:"+str(tel))
    if(name == "A" and tel==1):
        print("Height:"+str(dic1[(name,tel)])+"\n")