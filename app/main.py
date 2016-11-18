#!/usr/bin/env python3
def main(argv):
  ans = [1]
  for v in argv:
    for x in range(int(v)-1):
        p = -1
        n=[]
        count = 0
        for i in ans:
            count+=1
            if p==-1:
                p=i
                count=0
            if p!=i:
                n.append(count)
                n.append(p)
                count=0
            p=i
        if p!=i:
            n.append(count)
            n.append(p)
            n.append(1)
            n.append(i)
        else:
            n.append(count+1)
            n.append(p)
        ans=n
  for v in ans:
    print(v, end='')
