import numpy as np

f = open("reportrepair.txt", "r")
arr = []
for x in f:
   arr = np.append(arr,x.rstrip())

found=False
for x in arr:
   for y in arr: 
      for z in arr:   
         if((int(x)+int(y)+int(z))==2020):
            found=True
            break
      if(found):
         break
   if(found):
      break		 
print(int(x),int(y),int(z))		 
print(int(x)*int(y)*int(z))		 
