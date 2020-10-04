import pandas as pd
import re

literal = dict()
var1 = list()
sym = dict()
Loc_Count = 0

re_lit = re.compile(r'=[0-9]')

f_in = open('Task.txt','r')

for line in f_in:
    line.strip()
    words = line.split()
    
    if line.startswith('START'):
        Loc_Count = int(words[-1])
        continue
    
    if len(words)>3 :
        sym[str(words[0])] = Loc_Count
        
    if 'DC' in line:
        sym[str(words[0])] = Loc_Count
    
    if re_lit.search(line):
        var1.append(str(words[-1]))
        literal[str(words[-1])] = 0
        
    if line.startswith('END'):
        for w in var1:
            if literal.get(w)==0:
                literal[w] = Loc_Count
                Loc_Count += 1

    if 'DS' in line:
        sym[str(words[0])] = Loc_Count
        Loc_Count += int(words[-1])
        continue
    
    if line.startswith('ORIGIN'):
        sub = words[-1].split('+')
        if sub[0] in sym.keys():    
            Loc_Count = sym[str(sub[0])] + int(sub[1])
        continue
    
    if 'EQU' in line:
        if words[0] not in sym.keys():
            symb[str(words[0])] = sym[str(words[-1])]
    
    if 'LTORG' in line:
        for w in var1:
            literal[w] = Loc_Count
            Loc_Count += 1
        continue
            
    Loc_Count += 1
    
lit_table = pd.DataFrame(list(literal.items()),columns=['Literal','Address'])
print(lit_table)
    
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

