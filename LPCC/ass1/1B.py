import pandas as pd
import re

tfile = open('Task.txt','r')
literal = dict()
var1 = list()
symbol = dict()
LocCount = 0

re_lit = re.compile(r'=[0-9]')

for line in tfile:
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
        LocCount += int(words[-1])
        symbol[str(words[0])] = LocCount
        continue
    
    if line.startswith('ORIGIN'):
        sub = words[-1].split('+')
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
    
literal_table = pd.DataFrame(list(literal.items()),columns=['Literal','Address'])
print(literal_table)
