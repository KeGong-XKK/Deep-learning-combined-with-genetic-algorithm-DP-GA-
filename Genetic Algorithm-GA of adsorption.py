# -*- coding: utf-8 -*-
"""
Created on Mon Oct 25 15:06:13 2021

@author: GongKe
"""

# -*- coding: utf-8 -*-
"""
Created on Tue Oct 19 20:15:01 2021

@author: GongKe
"""

import math
import random
import numpy as np
import os
import time
import subprocess


def cof_building(a,k,dongtaishuzu_id,Topo_numer,Nodenumber,linkernumber):
    q = 0    
    path = os.getcwd() #当前在第N代文件夹中
    new_path = path + '/' + str(k) + '_' + str(a[k][0]) + '_' + str(a[k][1]) + '_' + str(a[k][2])+ '_' + str(a[k][3])+ '_' + str(a[k][4])
    os.mkdir(new_path)
    os.chdir(new_path) #进入到第N代第k个个体文件夹中          
    for j in range(len(dongtaishuzu_id)):
        
        if (a[k] == dongtaishuzu_id[j]).all():                
                os.chdir(path) #返回到第N代的文件夹中
                with open('old_propertity.data','a') as f:                    
                    f.write(str(dongtaishuzu_old_propertity[j]) + '\n')
                f.close()
                
                with open('vl_fraction.data','a') as f:                    
                    f.write(str(dongtaishuzu_valfaction[j]) + '\n')
                f.close()
                
                with open('PLD_LCD.data','a') as f:
                    f.write(str(dongtaishuzu_PLD_LCD[j]) + '\n')
                f.close()
        
                with open('density.data','a') as f:
                    f.write(str(dongtaishuzu_density[j]) + '\n')
                f.close()
                
                with open('gas_number.data','a') as h:
                     h.write(str(dongtaishuzu_number[j]) + '\n')
                h.close()
        
        
                with open('gas_capatity_stp.data','a') as f:
                    f.write(str(dongtaishuzu_stp[j]) + '\n')
                    
                f.close()
        
                with open('gas_desorption.data','a') as u:            
                    u.write(str(dongtaishuzu_heat_sorption[j]) + '\n')
                u.close()
        
                return(a) 
                 

                
              
        else:
            q+=1
            if q == len(dongtaishuzu_id):
            
                os.chdir(path) #返回到第N代的文件夹中
                shanchu_lujing = 'rm -rf' + ' ' + str(k) + '_' + str(a[k][0]) + '_' + str(a[k][1]) + '_' + str(a[k][2])+ '_' + str(a[k][3])+ '_' + str(a[k][4])
                os.system(shanchu_lujing)
                print('------------> Warning: The {} has been faild <-------------'.format(k))
                change_site = random.randint(1, 3)
                if change_site == 1:
                    qq = random.randint(1, Topo_numer)
                    a[k][1] = qq        
                elif change_site == 2:
                    qq = random.randint(1, Nodenumber)
                    a[k][2] = qq
                elif change_site == 3:
                    qq = random.randint(1, linkernumber)
                    a[k][3] = qq
                elif change_site == 4:
                    qq = random.randint(0,9)
                    a[k][4] = qq
    
                return(cof_building(a,k,dongtaishuzu_id,Topo_numer,Nodenumber,linkernumber))
            else:
                pass
        
def cof_build(a,i,ge_ti_shu_shumu):
    choose = 0
    l_index = []
    c = np.random.randint(0,5,size=[2,5]) 
    with open('gas_number.data','r') as f:
        lines = f.readlines()        
        lis = range(0,ge_ti_shu_shumu)
        slicce = random.sample(lis, 4)
        if float(lines[slicce[0]]) < float(lines[slicce[1]]):
            c[0] = a[slicce[1]]
            l_index.append(slicce[1])
        else:
            c[0] = a[slicce[0]]
            l_index.append(slicce[0])
            
        if float(lines[slicce[2]]) < float(lines[slicce[3]]):
            c[1] = a[slicce[3]]
            l_index.append(slicce[3])
        else:
            c[1] = a[slicce[2]]
            l_index.append(slicce[2])
    f.close()
    
    ##cross over####
    
    d = np.random.randint(0,5,size=[1,5])
    change = np.random.randint(0,5,size=[2,5])
    cross_rate = 0.68
        
    if np.random.rand() < cross_rate:
          print('------------> {} is Starting Cross <-------------'.format(i))  
          cross_site = np.random.randint(0,5)                            
                     
          if cross_site == 0:
                 if float(lines[l_index[0]]) < float(lines[l_index[1]]):
                     d[0] = c[1]
                 else:
                     d[0] = c[0]
          else:                        
                 change[0][cross_site:] = c[0][cross_site:]
                 change[1][cross_site:] = c[1][cross_site:]
                 c[0][cross_site:] = change[1][cross_site:]
                 c[1][cross_site:] = change[0][cross_site:]
                 index_live = random.randint(0, 1)
                 d[0] = c[index_live]
    else:
          if float(lines[l_index[0]]) < float(lines[l_index[1]]):
                     d[0] = c[1]
          else:
                     d[0] = c[0]
    
      
    ##Mutation over####
    mutation_rate = 0.1
    if np.random.rand() < mutation_rate:           
        print('------------> {} is Starting Mutation <-------------'.format(i))
        mutation_site = random.randint(0, 4)
        if mutation_site == 0:
            d[0][0] == random.randint(0,1)
        elif mutation_site == 1:
            d[0][1] == random.randint(1, topo_number)
        elif mutation_site == 2:
            d[0][2] == random.randint(1, node_number)
        elif mutation_site == 3:
            d[0][3] = random.randint(1, linker_number)
        elif mutation_site == 4:
            d[0][4] = random.randint(0, 9)
    else:
            pass      
    

    for j in range(len(dongtaishuzu_id)-1):
        if (d[0] == dongtaishuzu_id[j]).all():       
            return(d[0])
        else:
            choose += 1
            if choose == len(dongtaishuzu_id)-1:
                return(cof_build(a, i, ge_ti_shu_shumu))
            else:
                pass

 
    
###############################Main Process############################
generation = 21 #GA迭代次数
topo_number = 4
node_number = 8
linker_number = 29
ge_ti_shu_shumu = 100



dongtaishuzu_id = []
dongtaishuzu_number = []
dongtaishuzu_stp = []
dongtaishuzu_heat_sorption = []
dongtaishuzu_density = []
dongtaishuzu_PLD_LCD = []
dongtaishuzu_old_propertity = []
dongtaishuzu_valfaction = []

with open('fina_id_all.data','r') as f:
    lines = f.read()        
    b = lines.split('\n')    
    for i in range(len(b)-1):
        b[i] = b[i].split()
        a = np.array(b[i]).astype(np.int)       
        dongtaishuzu_id.append(a)
f.close()
print(len(dongtaishuzu_id))
with open('gas_number.data','r') as f:
    lines = f.readlines()
    for i in range(len(lines)):
        line = lines[i].split()
        dongtaishuzu_number.append(float(line[0]))
f.close()

with open('gas_capatity_stp.data','r') as f:
    lines = f.readlines()
    for i in range(len(lines)):
        line = lines[i].split()
        dongtaishuzu_stp.append(float(line[0]))
f.close()

with open('gas_desorption.data','r') as f:
    lines = f.readlines()
    for i in range(len(lines)):
        line = lines[i].split()
        dongtaishuzu_heat_sorption.append(float(line[0]))
f.close()

with open('density.data','r') as f:
    lines = f.readlines()
    for i in range(len(lines)):
        line = lines[i].split()
        dongtaishuzu_density.append(float(line[0]))
f.close()

with open('vl_fraction.data','r') as f:
    lines = f.readlines()
    for i in range(len(lines)):
        line = lines[i].split()
        dongtaishuzu_valfaction.append(float(line[0]))
f.close()

with open('PLD_LCD.data','r') as f:
    lines = f.read()
    b = lines.split('\n')
    for i in range(len(b)):       
        dongtaishuzu_PLD_LCD.append(b[i])
f.close()

with open('old_propertity.data','r') as f:
    lines = f.read()
    b = lines.split('\n')
    for i in range(len(b)):       
        dongtaishuzu_old_propertity.append(b[i])
f.close()

    
for pa in range(100):
    pa_path = os.getcwd()
    pa_new_path = pa_path + '/' + str(pa) + '_' + 'gas'
    os.mkdir(pa_new_path)
    os.chdir(pa_new_path) 
    #1=fes.cgd 2=fxt.cgd 3=hca.cgd 4=hcb.cgd
    a = [None]*ge_ti_shu_shumu

    for i in range(len(a)):
        a[i] = [0]*5
    for i in range(100):    
        a[i][0] = random.randint(0,1) #C3_C4 C3 = 0 C4 = 1    
        a[i][1] = random.randint(1, topo_number) #topo
        a[i][2] = random.randint(1, node_number) #node
        a[i][3] = random.randint(1, linker_number) #linker
        a[i][4] = random.randint(0, 9) #function id
        a[i] = np.array(a[i])


    #print('================Father and Mother is done=================')
    for j in range(1,generation):
   
        path = os.getcwd() #获得初始文件夹路径
        newpath = path + '/' + str(j) + '_' + 'gengeration'
        os.mkdir(newpath)
        os.chdir(newpath) #进入到第N代文件夹中
        start_time = time.time()
        for k in range(ge_ti_shu_shumu):
            
            cof_building(a,k,dongtaishuzu_id,topo_number,node_number,linker_number)#在第n代文件夹中 
		
            
            
        end_time = time.time()

        print('----------> The time spend in {} gas and {} generation is : {} <--------------'.format(pa,j,end_time-start_time))

        with open('0_id.data','w') as f:
            for mm in range(len(a)):
                f.write(str(a[mm][0]) + ' ')
        f.close()
        
        with open('1_id.data','w') as f:
            for mm in range(len(a)):
                f.write(str(a[mm][1]) + ' ')
        f.close()
        
        with open('2_id.data','w') as f:
            for mm in range(len(a)):
                f.write(str(a[mm][2]) + ' ')
        f.close()
        
        with open('3_id.data','w') as f:
            for mm in range(len(a)):
                f.write(str(a[mm][3]) + ' ')
        f.close()
        
        with open('4_id.data','w') as f:
            for mm in range(len(a)):
                f.write(str(a[mm][4]) + ' ')
        f.close()
        
        b = np.random.randint(0,5,size=[ge_ti_shu_shumu,5])
        #choose the biggest one
        ll_gas = []
        with open('gas_number.data','r') as f:
            lines = f.readlines()    
            length_gas = len(lines)    
            for i in range(length_gas):
                line = lines[i].split()
                ll_gas.append(line[0])    
                
            data = [float(i) for i in ll_gas]
            list_index_max = data.index(max(data))
            
        f.close()

        b[0] = a[list_index_max]
        for i in range(1,ge_ti_shu_shumu):
            b[i] = cof_build(a,i,ge_ti_shu_shumu)
            
        a = b
            
        with open('a_after.data','w') as f:
            f.write(str(a) + '\n')        
        f.close()
    
        os.chdir(path) #返回到初始路径     
    os.chdir(pa_path)        
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
