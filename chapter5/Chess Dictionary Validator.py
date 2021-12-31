def isvalidchessboard(chess):
    key=list(chess.keys())
    value=list(chess.values())
    n=len(chess)
    wpawn=0
    wknight=0
    wrook=0
    wqueen=0
    wbishop=0
    wking=0
    bpawn=0
    bbishop=0
    bknight=0
    brook=0
    bqueen=0
    bking=0
    piece=['wpawn','wknight','wbishop','wrook','wqueen','wking','bpawn','bknight','bbishop','brook','bqueen','bking']
    for t in range(n):
        a=key[t]
        b=value[t]
        c=0
        if a[0]>'8':
            return False
            break
        if a[1]>'h':
            return False
            break
        if(b[0]!='b' and b[0]!='w'):
            return False
            break
        if value[t]=='wpawn':
            wpawn=wpawn+1
            if wpawn>8:
                return False
                break
        elif value[t]=='wknight':
            wknight=wknight+1
            if wknight>2:
                return False
                break
        elif value[t]=='wbishop':
            wbishop=wbishop+1
            if wbishop>2:
                return False
                break
        elif value[t]=='wrook':
            wrook=wrook+1
            if wrook>2:
                return False
                break
        elif value[t]=='wqueen':
            wqueen=wqueen+1
            if wqueen>1:
                return False
                break
        elif value[t]=='wking':
            wking=wking+1
            if wking>1:
                return False
                break
        if value[t]=='bpawn':
            bpawn=bpawn+1
            if wpawn>8:
                return False
                break
        elif value[t]=='bknight':
            bknight=bknight+1
            if bknight>2:
                return False
                break
        elif value[t]=='bbishop':
            bbishop=bbishop+1
            if bbishop>2:
                return False
                break
        elif value[t]=='brook':
            brook=brook+1
            if brook>2:
                return False
                break
        elif value[t]=='bqueen':
            bqueen=bqueen+1
            if bqueen>1:
                return False
                break
        elif value[t]=='bking':
            bking=bking+1
            if wking>1:
                return False
                break
        for j in range(12):
            if value[t]==piece[j]:
                c=c+1
        if c==0:
            return False
            break
board={'1h': 'bking', '6c': 'wqueen', '2g': 'bbishop', '5h': 'bqueen', '3e': 'wking'}
result=isvalidchessboard(board)
if result!=False:
    result=True
print(result)    
   