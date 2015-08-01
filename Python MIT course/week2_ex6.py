def clip(lo, x, hi):
     # lo if x<lo
     # hi if x>hi
     # else x 
    return min(max(x,lo),max(min(x,hi),lo))

print clip(1,20,3)


