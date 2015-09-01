# -*- coding: utf-8 -*-

import matplotlib.pyplot as plt
import numpy as np

#f=open('clocks208Asm2.txt','r')
#a=[]
#for l in f:
#  a.append(int(l[:-2]))
#f.close()    
#plt.hist(a, bins=25)
#i = 0
#for i in range(len(a)):
#  print a[i]

fig, ax = plt.subplots()
loc = [1,2,3,4]
loc=np.arange(4)
width=0.35
#C, ASM1, ASM2, ASM1_MejoraenScalar, ASM2_MejoraenScalar, ASM2_mejoraconrgb
medias=[0.66029 ,0.71213,0.75875,1.370972 ]  
std=[0,0,0,0]                 
barras=ax.bar(loc,medias,width,yerr=std,error_kw=dict(ecolor='k', lw=2, capsize=5, capthick=2))

dicolor={0:'b',1:'g',2:'r',3:'wheat',4:'m',5:'darkred',6:'darkgray',7:'chartreuse',8:'olive',9:'teal',10:'aquamarine',11:'orangered',12:'yellow',13:'deeppink'}
for i in loc:
  barras[i].set_color(dicolor[i])
    
#ax.errorbar(loc,medias,yerr=std,linewidth=8)    
    
ax.set_ylabel('Tiempo de ejecucion')
ax.set_xlabel('Test para ronda de 8 exploradoras')
ax.set_xticks(loc+width*1.2/2)
ax.set_title('Tiempo esperado de ejecucion en el peor caso y promedios con poda')
ax.set_xticklabels(('Random', 'Random', 'Random', 'Peor caso')) 

plt.show()