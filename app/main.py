#!/usr/bin/env python3
def main(argv):
  ans = [1]
  count = 0
  for v in argv:
    for x in range(v-1):
        n=[]
        for i in ans:
            count+=1
            if p!=i:
                n.append(count)
                n.append(p)
                count=1
            p=i
        n.append(count)
        n.append(p)
        ans=n
  for v in ans:
    print(v)
