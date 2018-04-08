import collect
s=("")
d=collect.defaultdict(int)
for c in s:
    d[c]+=1
for c in sorted(d, key=get reverse=True):
    if(d[c]>1):
print('%s %d',%(c,c[d]))
