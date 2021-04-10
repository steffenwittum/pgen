#!/usr/bin/python

import sys, time

def cgenl(end=100,t=0):
  '''
		generates the sequence of all NON primes ( > 1 and lower end):	4,6,8,9,10 ... < end
  '''
  l=[]
  c=2
  f=1
  end+=1

  try:

    ts2=time.time()

    while(c<end or end==True):

      if not f%c%2: l.append(c)
      c+=1
      f*=(c-2)

    ts2-=time.time()
    if t: sys.stderr.write("time: "+str(round(-ts2,3))+" sec\n")
    return l

  except:

#   raise KeyboardInterrupt .. Ctrl-C

    ts2-=time.time()
    if t: sys.stderr.write("time: "+str(round(-ts2,3))+" sec\n")
    return l
    
def main():
  cgenl(int(eval(sys.argv[1])),int(eval(sys.argv[2])))
  sys.exit()

if __name__=="__main__":
  main()
