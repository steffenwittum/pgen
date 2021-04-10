#!/usr/bin/python

import sys, time

def pgenl(end=100,t=0):
  '''
		generates the sequence of all primes (lower end): 2,3,5 ... < end
  '''
  l=[]
  p=2
  f=1
  end+=1

  try:

    ts2=time.time()

    while(p<end or end==True):

      if f%p%2: l.append(p)
      p+=1
      f*=(p-2)

    ts2-=time.time()
    if t: sys.stderr.write("time: "+str(round(-ts2,3))+" sec\n")
    return l

  except:

#   raise KeyboardInterrupt .. Ctrl-C

    ts2-=time.time()
    if t: sys.stderr.write("time: "+str(round(-ts2,3))+" sec\n")
    return l

def main():
  pgenl(int(eval(sys.argv[1])),int(eval(sys.argv[2])))
  sys.exit()

if __name__=="__main__":
  main()
