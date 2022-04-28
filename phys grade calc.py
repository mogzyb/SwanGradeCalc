# -*- coding: utf-8 -*-
"""
Created on Thu Jul 22 20:36:13 2021

@author: mogzy
"""

import matplotlib.pyplot as plt

lf=46.5
uf=74.5
l1=62.5
u1=78.125
# l2=74.5 #Average marks achieved in remaining Level 5 credits pursued
# u2=87 #Average of the best marks achieved in 40 credits pursued at Level 5

PH203=84
PH204=96
PH205=70
PH206=81
PH207=80
PH211=84
PH221=70
PH222=84
PH227=84
PH229=68
PH230=63
PH320=80

PH300=9.5
PH302=26
PH306=30
PH307=84
PH311=8
PH312=66
PH321=25
PH333=78*0.2
PH335=19
PH338=76
PH339=82*0.3



g2= [PH203,PH204,PH205,PH206,PH207,PH211,PH221,PH222,PH227,PH229,PH230,PH320]
g2s=g2.sort(reverse=True)
g3= [PH300,PH302,PH306,PH307,PH311,PH311,PH312,PH321,PH333,PH335,PH338,PH339]
g3s=g3.sort(reverse=True)


l2=sum(g2[4:11]) / len(g2[4:11])
u2=sum(g2[0:3]) / len(g2[0:3])
l3=sum(g3[8:11]) / len(g3[8:11])
u3=sum(g3[0:7]) / len(g3[0:7])


current=((l2)+(u2+sum(g3[8:11]) / len(g3[8:11]))+((sum(g3[0:7]) / len(g3[0:7]))*3))/6

boundry=68

for est in range(1001,-1,-1):
   
   PH300a=9.5+((est/10)*0.9)
   PH302a=26+((est/10)*0.7)
   PH306a=30+((est/10)*0.7)
   PH307a=84
   PH311a=8+((est/10)*0.9)
   PH312a=66
   PH321a=25+((est/10)*0.7)
   PH333a=(78*0.2)+((est/10)*0.8)
   PH335a=19+((est/10)*0.8)
   PH338a=76
   PH339a=(82*0.3)+((est/10)*0.7)
   
   g3a= [PH300a,PH302a,PH306a,PH307a,PH311a,PH311a,PH312a,PH321a,PH333a,PH335a,PH338a,PH339a]
   g3sa=g3a.sort(reverse=True)
   l3a=sum(g3a[8:11]) / len(g3a[8:11])
   u3a=sum(g3a[0:7]) / len(g3a[0:7])
   currenta=((l2)+(u2+sum(g3a[8:11]) / len(g3a[8:11]))+((sum(g3a[0:7]) / len(g3a[0:7]))*3))/6
   if est/10 >= 100:
       esta=est/10
       fcurrent=currenta
   else:
       if currenta >= boundry:
           esta=est/10
           fcurrent=currenta

unweight=((sum(g2) / len(g2))+(sum(g3) / len(g3)))/2
unweighta=((sum(g2) / len(g2))+(sum(g3a) / len(g3a)))/2

total=[]
godx=[]
gody=[]
gdx=[]
gdy=[]
ydx=[]
ydy=[]
rdx=[]
rdy=[]
for l in range(0,1001,1):
    for u in range(0,1001,1):

        b1=l2
        b2=u2+(l/10)
        b3=(u/10)*3
        
        total.append((u/10,l/10,((b1+b2+b3)/6)))
        
    
for n in range (0,len(total),1):
    if total[n][2]>=68 and total[n][1]<=total[n][0]:
        godx.append(total[n][0])
        gody.append(total[n][1])    
    
for n in range (0,len(total),1):
    if total[n][2]>=58 and total[n][1]<=total[n][0]:
        gdx.append(total[n][0])
        gdy.append(total[n][1])
        
for n in range (0,len(total),1):
    if total[n][2]>=48 and total[n][1]<=total[n][0]:
        ydx.append(total[n][0])
        ydy.append(total[n][1])
        
for n in range (0,len(total),1):
    if total[n][2]>=38 and total[n][1]<=total[n][0]:
        rdx.append(total[n][0])
        rdy.append(total[n][1])
      
        
plt.xlabel("Average for top 80 credits for 3rd year")
plt.ylabel("Average for bottom 40 credits for 3rd year")
plt.plot(rdx,rdy, 'r')
plt.plot(ydx,ydy, 'orange')
plt.plot(gdx,gdy, 'g')
plt.plot(godx,gody, 'gold')
plt.plot(uf, lf, 'bo')
plt.text(uf+1, lf, 'Foundation Year ('+str(round(uf,1))+', '+str(round(lf,1))+ ')')
plt.plot(u1, l1, 'bo')
plt.text(u1+1, l1, 'First Year ('+str(round(u1,1))+', '+str(round(l1,1))+ ')')
plt.plot(u2, l2, 'bo')
plt.text(u2+1, l2, 'Second Year ('+str(round(u2,1))+', '+str(round(l2,1))+ ')')
plt.plot(u3,l3, 'bo')
plt.text(u3+1,l3, 'Current Third Year Grade ('+str(round(u3,1))+', '+str(round(l3,1))+ ')')
plt.ylim(-1,80)
plt.xlim(u3-20,100)
plt.title('Current Grade - '+str(round(current,1))+'% , Assuming ' +str(round(esta,1))+'% In Ungraded Work- '+str(round(fcurrent,1))+'%')
plt.grid()
plt.locator_params(axis="x", nbins=20)
plt.locator_params(axis="y", nbins=20)
plt.show()





# import matplotlib.pyplot as plt

# l2=74.5 #Average marks achieved in remaining Level 5 credits pursued
# l3=50 #Average remaining marks in 60 Level 6 credits pursued
# u2=87  #Average of the best marks achieved in 30 credits pursued at Level 5
# u3=50 #Average best marks in 60 credits pursued at Level 6

# total=[]
# gdx=[]
# gdy=[]

# for l in range(0,101,1):
#     for u in range(0,101,1):

#         b1=l2
#         b2=((u2*2)+(l3*4))/3
#         b3=(u3*2)+l
#         b4=u*4
        
#         total.append((u,l,((b1+b2+b3+b4)/10)))
        
    
# for n in range (0,len(total),1):
#     if total[n][2]>70 and total[n][1]<=total[n][0]:
#         gdx.append(total[n][0])
#         gdy.append(total[n][1])
        
# plt.xlabel("Average for top 90 credits for 4th year")
# plt.ylabel("Average for bottom 30 credits for 4th year")
# plt.plot(gdx,gdy)
# plt.ylim(0,min(gdx))
# plt.xlim(min(gdx),100)
# plt.grid()

# plt.show()
