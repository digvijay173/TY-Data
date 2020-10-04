import pandas as pd
import re
literal = dict()
var1 = list()
symbol = dict()
LocCount = 0

re_lit = re.compile(r'=[0-9]')

fhand = open('Task.txt','r')
for line in fhand:
    line.strip()
    words = line.split()
    if line.startswith('START'):
        LocCount = int(words[-1])
        continue
    if len(words)>3 :
        symbol[str(words[0])] = LocCount     
    if 'DC' in line:
        symbol[str(words[0])] = LocCount
    if re_lit.search(line):
        var1.append(str(words[-1]))
        literal[str(words[-1])] = 0   
    if line.startswith('END'):
        for w in var1:
            if literal.get(w)==0:
                literal[w] = LocCount
                LocCount += 1
    if 'DS' in line:
        symbol[str(words[0])] = LocCount
        LocCount += int(words[-1])
        continue
    if line.startswith('ORIGIN'):
        sub = words[-1].split('+')
        if sub[0] in symbol.keys():    
            LocCount = symbol[str(sub[0])] + int(sub[1])
        continue 
    if 'EQU' in line:
        if words[0] not in symbol.keys():
            symbol[str(words[0])] = symbol[str(words[-1])]
    if 'LTORG' in line:
        for w in var1:
            literal[w] = LocCount
            LocCount += 1
        continue         
    LocCount += 1
    
symbol_tb = pd.DataFrame(list(symbol.items()),columns=['Symbol','Address'])
print(symbol_tb)
literal_tb = pd.DataFrame(list(literal.items()),columns=['Literal','Address'])
print(literal_tb)

pool = literal.values()

p_table = list()
p_table.append('#1')
                  
counter = list(pool)[0]
cnt = 1
for i in pool:
    if i-counter>1:
        temp='#'+str(cnt)
        p_table.append(temp)
    cnt+=1
    counter = i
        
p_table = pd.DataFrame(list(p_table),columns=['Pool Table'])  
print(p_table)
optable = {
          'START':"('AD',01)",
           'END':"('AD',02)",
           'LTORG':"('AD',05)",
           'ORIGIN':"('AD',03)",
           'EQU':"('AD',04)",
           'DC':"('DL', 01)",
           'DS':"('DL', 02)",
           'ADD':"('IS', 01)",
           'SUB':"('IS', 02)",
           'MOVER':"('IS', 04)",
           'MOVEM':"('IS', 05)",
           'READ':"('IS', 09)",
           'PRINT':"('IS', 10)"
           }

register = ['AREG','BREG']
re_constant = re.compile('[0-9]+')
interLine = list()
count = 1

fhand = open('Task.txt','r')
for line in fhand:
    line.strip()    
    words = line.split()
    flag=0
        
    if words[0] in optable.keys():
        if words[0]=='ORIGIN':
            tup = list()
            tup.append(words[0])
            tup.append(words[1])
            interLine.append(tup)
            flag=1
    
        tup = list()
        tup = optable[words[0]]
        interLine.append(tup)

    elif words[0] in symbol.keys() and flag!=1:
        if words[1] in optable.keys():
            tup = list()
            tup = optable[words[1]]
            interLine.append(tup)
            
    if "AREG" in words and flag!=1:
        tup = list()
        tup.append("AREG")
        interLine.append(tup)
        
    if "BREG" in words and flag!=1:
        tup = list()
        tup.append("BREG")
        interLine.append(tup)

    if words[-1] in symbol.keys() and flag!=1:
        tup = list()
        tup.append(words[-1])
        interLine.append(tup)
        
    if words[-1] in literal.keys() and flag!=1:
        tup = list()
        tup.append("L,")
        tup.append("0"+str(count))
        count+=1
        interLine.append(tup)
       
    if words[-1][0] != "=" and flag!=1:
        if re_constant.search(words[-1][0]):
            tup = list()
            tup.append("C,")
            tup.append(words[-1])
            interLine.append(tup)
    interLine.append("NEWLINE")
            
print("Intermediate Code : ")
for i in range(len(interLine)):
    if interLine[i]=="NEWLINE":
    	print("")
        continue
    print(interLine[i]),

