# Author: Chromilo Amin
# Email: chromilo.amin@gatech.edu
# Date: Dec 18, 2020
# Description: Use string manipulation to count number of valid passports as presented in adventofcode.com for day 4 in 2020.
# ---
# Part 1:
#byr (Birth Year)
#iyr (Issue Year)
#eyr (Expiration Year)
#hgt (Height)
#hcl (Hair Color)
#ecl (Eye Color)
#pid (Passport ID)
#cid (Country ID) - optional
# ---
# Part 2:
#byr (Birth Year) - four digits; at least 1920 and at most 2002.
#iyr (Issue Year) - four digits; at least 2010 and at most 2020.
#eyr (Expiration Year) - four digits; at least 2020 and at most 2030.
#hgt (Height) - a number followed by either cm or in:
#If cm, the number must be at least 150 and at most 193.
#If in, the number must be at least 59 and at most 76.
#hcl (Hair Color) - a # followed by exactly six characters 0-9 or a-f.
#ecl (Eye Color) - exactly one of: amb blu brn gry grn hzl oth.
#pid (Passport ID) - a nine-digit number, including leading zeroes.
#cid (Country ID) - ignored, missing or not.

f = open("passport.txt", "r")
s=[]
lst=[]
for x in f:
   if(len(x)>1):
      s = x.split(" ") + s
   else:
      lst.append(s)
      s=[]
lst.append(s)  

n=0   # total for part 1
m=0   # total for part 2
ecl=["amb","blu","brn","gry","grn","hzl","oth"]
for i in lst:
   print(i)	  
   part1=0
   part2=0
   for j in i:
      print(j)
      if(j.find("byr:")>=0 or j.find("iyr:")>=0 or j.find("eyr:")>=0 or j.find("hgt:")>=0 or j.find("hcl:")>=0 or j.find("ecl:")>=0 or j.find("pid:")>=0):
         part1 += 1
         if(j.find("byr:")>=0):
            val=j[4:].rstrip()
            if(int(val)>=1920 and int(val)<=2002):
               part2 += 1
         elif(j.find("iyr:")>=0):
            val=j[4:].rstrip()
            if(int(val)>=2010 and int(val)<=2020):
               part2 += 1		
         elif(j.find("eyr:")>=0):
            val=j[4:].rstrip()
            if(int(val)>=2020 and int(val)<=2030):
               part2 += 1
         elif(j.find("pid:")>=0):
            val=j[4:].rstrip()
            if(len(val)==9):
               valid=False
               for z in val:
                  if(z.isdigit()):
                     valid=True
                  else:
                     valid=False	
               if(valid==True):					 
                  part2 += 1	
         elif(j.find("ecl:")>=0):
            val=j[4:].rstrip()
            if(val in ecl):
               part2 += 1	
         elif(j.find("hcl:#")>=0):
            val=j[5:].rstrip()
            if(len(val)==6):
               valid=False
               for z in val:
                  if(z.isdigit()) or (z.isalpha() and z.isalpha() and z <= "f"):
                     valid=True
                  else:
                     valid=False
               if(valid==True):
                  part2 += 1	
         elif(j.find("hgt:")>=0):
            val=j[4:].rstrip()
            if(val[val.find("cm"):]=="cm"):
               hgt=val[:val.find("cm")]
               if(int(hgt)>=150 and int(hgt)<=193):
                  part2 += 1					 
            elif(val[val.find("in"):]=="in"):
               hgt=val[:val.find("in")]
               if(int(hgt)>=59 and int(hgt)<=76):
                  part2 += 1		
   if(part1>=7 and part1==part2): 
      m += 1
   if(part1>=7 and part2>0):
      n += 1
print(n,m)
f.close()
