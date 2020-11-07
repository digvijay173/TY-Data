fhand = open('task.txt', 'r') 

output = [] 
code = {} 
para = {} 
curr_mac = "NULL" 

for line in fhand: 
    line.strip()
    dup_line = line 
    
    words=line.split()

    if words[0] == "MACRO": 
        curr_mac = words[1] 
        param = [] 
        for y in words[2:]:
             param.append(y)
        code[words[1]] = [] 
        para[words[1]] = param 
    elif words[0]!="MACRO" and curr_mac=="NULL": 
        output.append(dup_line)
    elif words[0] == "MEND": 
        code[curr_mac].append(words) 
        curr_mac = "NULL"
    elif words[0] != "MACRO" and curr_mac != "NULL":
        code[curr_mac].append(words) 

mdt = []
start = {} 
i = 1 
for key in code.keys(): 
    values = {}
    start[key] = i 
    for x in code[key]: 
        if x[0] not in code.keys(): 
            n = 0
            st1 = x[:]
            for element in st1:
                if element in para[key]:
                    st1[n] = values[element]
                n = n + 1
            temp = [i,st1]
            mdt.append(temp)
            i = i + 1
 
print("First Pass: ")
print()
print("Intermediate Code : ") #Display Intermediate Code
print()
for x in output:
    print(x, end=" ")
print()
print("Macro Defination Table (MDT) : ") #Display MDT
for x in mdt:
    print(x[0],end = " ")
    for y in x[1]:
        print(y,end = " ")
    print()
print()
print("Macro Name Table(MNT) : ") #Display MNT
print("Name of Macro  | No. of para | Starting Index")
for x in para.keys():
    print(x,"\t\t|",len(para[x]),"\t\t\t|",start[x])
    
fhand.close()
