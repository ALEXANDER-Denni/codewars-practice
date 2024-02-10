import sys
import math

lines=sys.stdin.readlines()

result=[]
primes=[1,2,3,5,7,11,13,17,19,23,29,31,37,41]
for lineInput in lines:
    lineInput=lineInput.rstrip("\n").rstrip(" ")
    for i in range(2,int(math.sqrt(int(lineInput)))):
        if(int(lineInput)%i==0):
            result.append("("+str(i)+"*"+str(int(lineInput)/i)+")")
print(str(lineInput)+"="+", ".join(result))
