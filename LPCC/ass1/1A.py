import pandas as pd

tfile = open('Task.txt','r')
symbol = dict()
LocCount = 0

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

    if 'DS' in line:
        symbol[str(words[0])] = LocCount
        LocCount += int(words[-1])
        continue

    if 'EQU' in line:
        if words[0] not in symbol.keys():
            symbol[str(words[0])] = symbol[str(words[-1])]
    LocCount += 1

symbol_table = pd.DataFrame(list(symbol.items()),columns=['Symbol','Address'])

print(symbol_table)
