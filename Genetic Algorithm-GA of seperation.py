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





def function_add(a1,k1):
    a = a1
    k = k1
    
    
    func_id = a[k][4]
    site_1 = []
    site = []
    function_list = ['H','F','Cl','Br','O','O','N','N','N','C'] #=O -OH -NH -NH2 -CH
    #add function group in node.xyz
    
    
    if func_id == 0:
        with open('linker.xyz','r') as f:
            with open('linker_1.xyz','w') as q:
                lines = f.readlines()
                length = len(lines)
                for i in range(2):
                    q.write(str(lines[i]))
                for j in range(2,length):
                    line = lines[j].split()
                    if line[0] == 'Xx':
                        line[0] = 'H'
                        q.write(str('         '.join(line)) + '\n')
                    else:
                        q.write(str(lines[j]))
            q.close()
        f.close() 
               
    elif func_id == 1:
        with open('linker.xyz','r') as f:
            with open('linker_1.xyz','w') as q:
                lines = f.readlines()
                length = len(lines)
                for i in range(2):
                    q.write(str(lines[i]))
                for j in range(2,length):
                    line = lines[j].split()
                    if line[0] == 'Xx':
                        line[0] = 'F'
                        q.write(str('         '.join(line)) + '\n')
                    else:
                        q.write(str(lines[j]))
            q.close()
        f.close()
        
    elif func_id == 2:
        with open('linker.xyz','r') as f:
            with open('linker_1.xyz','w') as q:
                lines = f.readlines()
                length = len(lines)
                for i in range(2):
                    q.write(str(lines[i]))
                for j in range(2,length):
                    line = lines[j].split()
                    if line[0] == 'Xx':
                        line[0] = 'Cl'
                        q.write(str('         '.join(line)) + '\n')
                    else:
                        q.write(str(lines[j]))
            q.close()
        f.close()       
    elif func_id == 3:
        with open('linker.xyz','r') as f:
            with open('linker_1.xyz','w') as q:
                lines = f.readlines()
                length = len(lines)
                for i in range(2):
                    q.write(str(lines[i]))
                for j in range(2,length):
                    line = lines[j].split()
                    if line[0] == 'Xx':
                        line[0] = 'Br'
                        q.write(str('         '.join(line)) + '\n')
                    else:
                        q.write(str(lines[j]))
            q.close()
        f.close()       
    
    elif func_id == 4:
        with open('linker.xyz','r') as f:
            with open('linker_1.xyz','w') as q:
                lines = f.readlines()
                length = len(lines)
                for i in range(2):
                    q.write(str(lines[i]))
                for j in range(2,length):
                    line = lines[j].split()
                    if line[0] == 'Xx':
                        line[0] = 'O'
                        q.write(str('         '.join(line)) + '\n')
                    else:
                        q.write(str(lines[j]))
            q.close()
        f.close()       
           
    elif func_id == 5:
         with open('linker.xyz','r') as f:
             lines = f.readlines()
             length = len(lines)
             for i in range(2,length):
                 line = lines[i].split()
                 if line[0] == 'Xx':
                     site_1.append(line[1])
                     site_1.append(line[2])
                     site_1.append(line[3])
                 else:
                     pass
         f.close()
         func_numer = int(len(site_1)/3)
         
         with open('linker.xyz','r') as f:
            with open('linker_1.xyz','w') as q:
                lines = f.readlines()
                length = len(lines)
                for i in range(2):
                    if i == 0:
                        line_number = lines[i].split()
                        line_number[0] = int(line_number[0]) + func_numer
                        q.write(str(line_number[0]) + '\n')
                    else:
                        q.write(str(lines[i]))
                        
                for j in range(2,length):
                    line = lines[j].split()
                    if line[0] == 'Xx':
                        line[0] = function_list[func_id]
                        q.write(str('         '.join(line)) + '\n')
                        site.append(line[1])
                        site.append(line[2])
                        site.append(line[3])
                    else:
                        q.write(str(lines[j]))
                a = 0
                for i in range(func_numer):                   
                    q.write(str('H') + '         ')
                    x = float(site[a]) - 0.544
                    x_new = round(x,5)
                    q.write(str(x_new) + '         ')
                    y = float(site[a+1]) + 0.839
                    y_new = round(y,5)
                    q.write(str(y_new) + '         ')
                    z = float(site[a+2]) + 0.482
                    z_new = round(z,5)
                    q.write(str(z_new) + '\n')
                    a = a+3
            q.close()
         f.close()                                
    
    elif func_id == 6:
         with open('linker.xyz','r') as f:
             lines = f.readlines()
             length = len(lines)
             for i in range(2,length):
                 line = lines[i].split()
                 if line[0] == 'Xx':
                     site_1.append(line[1])
                     site_1.append(line[2])
                     site_1.append(line[3])
                 else:
                     pass
         f.close()
         func_numer = int(len(site_1)/3)
         
         with open('linker.xyz','r') as f:
            with open('linker_1.xyz','w') as q:
                lines = f.readlines()
                length = len(lines)
                for i in range(2):
                    if i == 0:
                        line_number = lines[i].split()
                        line_number[0] = int(line_number[0]) + func_numer
                        q.write(str(line_number[0]) + '\n')
                    else:
                        q.write(str(lines[i]))
                        
                for j in range(2,length):
                    line = lines[j].split()
                    if line[0] == 'Xx':
                        line[0] = function_list[func_id]
                        q.write(str('         '.join(line)) + '\n')
                        site.append(line[1])
                        site.append(line[2])
                        site.append(line[3])
                    else:
                        q.write(str(lines[j]))
                a = 0
                for i in range(func_numer):                   
                    q.write(str('H') + '         ')
                    x = float(site[a]) - 0.446
                    x_new = round(x,5)
                    q.write(str(x_new) + '         ')
                    y = float(site[a+1]) + 1.009
                    y_new = round(y,5)
                    q.write(str(y_new) + '         ')
                    z = float(site[a+2]) - 0.118
                    z_new = round(z,5)
                    q.write(str(z_new) + '\n')
                    a = a+3
            q.close()
         f.close()                       
    
    elif func_id == 7:
         with open('linker.xyz','r') as f:
             lines = f.readlines()
             length = len(lines)
             for i in range(2,length):
                 line = lines[i].split()
                 if line[0] == 'Xx':
                     site_1.append(line[1])
                     site_1.append(line[2])
                     site_1.append(line[3])
                 else:
                     pass
         f.close()
         func_numer = int(len(site_1)/3)
         
         with open('linker.xyz','r') as f:
            with open('linker_1.xyz','w') as q:
                lines = f.readlines()
                length = len(lines)
                for i in range(2):
                    if i == 0:
                        line_number = lines[i].split()
                        line_number[0] = int(line_number[0]) + func_numer*2
                        q.write(str(line_number[0]) + '\n')
                    else:
                        q.write(str(lines[i]))
                        
                for j in range(2,length):
                    line = lines[j].split()
                    if line[0] == 'Xx':
                        line[0] = function_list[func_id]
                        q.write(str('         '.join(line)) + '\n')
                        site.append(line[1])
                        site.append(line[2])
                        site.append(line[3])
                    else:
                        q.write(str(lines[j]))
                a = 0
                for i in range(func_numer):                   
                    q.write(str('H') + '         ')
                    x = float(site[a]) - 0.369
                    x_new = round(x,5)
                    q.write(str(x_new) + '         ')
                    y = float(site[a+1]) + 0.27
                    y_new = round(y,5)
                    q.write(str(y_new) + '         ')
                    z = float(site[a+2]) - 1.012
                    z_new = round(z,5)
                    q.write(str(z_new) + '\n')
                    q.write(str('H') + '         ')
                    x = float(site[a]) - 0.368
                    x_new = round(x,5)
                    q.write(str(x_new) + '         ')
                    y = float(site[a+1]) + 0.742
                    y_new = round(y,5)
                    q.write(str(y_new) + '         ')
                    z = float(site[a+2]) + 0.738
                    z_new = round(z,5)
                    q.write(str(z_new) + '\n')
                    a = a+3
            q.close()
         f.close()                           
    
    
    elif func_id == 8:
         with open('linker.xyz','r') as f:
             lines = f.readlines()
             length = len(lines)
             for i in range(2,length):
                 line = lines[i].split()
                 if line[0] == 'Xx':
                     site_1.append(line[1])
                     site_1.append(line[2])
                     site_1.append(line[3])
                 else:
                     pass
         f.close()
         func_numer = int(len(site_1)/3)
         
         with open('linker.xyz','r') as f:
            with open('linker_1.xyz','w') as q:
                lines = f.readlines()
                length = len(lines)
                for i in range(2):
                    if i == 0:
                        line_number = lines[i].split()
                        line_number[0] = int(line_number[0]) + func_numer*2
                        q.write(str(line_number[0]) + '\n')
                    else:
                        q.write(str(lines[i]))
                        
                for j in range(2,length):
                    line = lines[j].split()
                    if line[0] == 'Xx':
                        line[0] = function_list[func_id]
                        q.write(str('         '.join(line)) + '\n')
                        site.append(line[1])
                        site.append(line[2])
                        site.append(line[3])
                    else:
                        q.write(str(lines[j]))
                a = 0
                for i in range(func_numer):                   
                    q.write(str('O') + '         ')
                    x = float(site[a]) - 0.369
                    x_new = round(x,5)
                    q.write(str(x_new) + '         ')
                    y = float(site[a+1]) + 0.27
                    y_new = round(y,5)
                    q.write(str(y_new) + '         ')
                    z = float(site[a+2]) - 1.012
                    z_new = round(z,5)
                    q.write(str(z_new) + '\n')
                    q.write(str('O') + '         ')
                    x = float(site[a]) - 0.368
                    x_new = round(x,5)
                    q.write(str(x_new) + '         ')
                    y = float(site[a+1]) + 0.742
                    y_new = round(y,5)
                    q.write(str(y_new) + '         ')
                    z = float(site[a+2]) + 0.738
                    z_new = round(z,5)
                    q.write(str(z_new) + '\n')
                    a = a+3
            q.close()
         f.close() 
    
    elif func_id == 9:
         with open('linker.xyz','r') as f:
             lines = f.readlines()
             length = len(lines)
             for i in range(2,length):
                 line = lines[i].split()
                 if line[0] == 'Xx':
                     site_1.append(line[1])
                     site_1.append(line[2])
                     site_1.append(line[3])
                 else:
                     pass
         f.close()
         func_numer = int(len(site_1)/3)
         
         with open('linker.xyz','r') as f:
            with open('linker_1.xyz','w') as q:
                lines = f.readlines()
                length = len(lines)
                for i in range(2):
                    if i == 0:
                        line_number = lines[i].split()
                        line_number[0] = int(line_number[0]) + func_numer
                        q.write(str(line_number[0]) + '\n')
                    else:
                        q.write(str(lines[i]))
                        
                for j in range(2,length):
                    line = lines[j].split()
                    if line[0] == 'Xx':
                        line[0] = function_list[func_id]
                        q.write(str('         '.join(line)) + '\n')
                        site.append(line[1])
                        site.append(line[2])
                        site.append(line[3])
                    else:
                        q.write(str(lines[j]))
                a = 0
                for i in range(func_numer):                   
                    q.write(str('H') + '         ')
                    x = float(site[a]) - 0.446
                    x_new = round(x,5)
                    q.write(str(x_new) + '         ')
                    y = float(site[a+1]) + 1.009
                    y_new = round(y,5)
                    q.write(str(y_new) + '         ')
                    z = float(site[a+2]) - 0.118
                    z_new = round(z,5)
                    q.write(str(z_new) + '\n')
                    a = a+3
            q.close()
         f.close()                      
         
    
                      
    os.system('rm -rf linker.xyz')
    os.system('mv linker_1.xyz linker.xyz')
    
         
   

def cof_building(a,k,t1,n1,l_1):
    

    
    pilipala = 0
    Topo_numer = t1
    Nodenumber = n1
    linkernumber = l_1
    path = os.getcwd() #当前在第N代文件夹中
    print(a)
    print(k)
    new_path = path + '/' + str(k) + '_' + str(a[k][0]) + '_' + str(a[k][1]) + '_' + str(a[k][2])+ '_' + str(a[k][3])+ '_' + str(a[k][4])
    os.mkdir(new_path)
    os.chdir(new_path) #进入到第N代第k个个体文件夹中
    for j in range(len(dongtaishuzu_id)-1):
        if (a[k] == dongtaishuzu_id[j]).all():
            if a[k][0] == 0:
                if a[k][1] == 1:
                    val1 = 'cp' + ' ' + '../../../fes.cgd' + ' ' + './'
                    val2 = 'cp' + ' ' + '../../../' +  str(a[k][2]) + '.xyz' + ' ' +  './'
                    val3 = 'cp' + ' ' + '../../../' + 'l' +  str(a[k][3]) + '.xyz' + ' ' +  './'
                    val4 = 'mv' + ' ' + str(a[k][2]) + '.xyz' + ' ' + 'node.xyz'
                    val5 = 'mv' + ' ' + 'l' + str(a[k][3]) + '.xyz' + ' ' + 'linker.xyz'
                    
                    val6 = 'cp ../../../simulation.input ./'
                    val7 = 'cp ../../../pseudo_atoms.def ./'
                    val8 = 'cp ../../../force_field_mixing_rules.def ./'
                    val9 = 'cp ../../../force_field.def ./'
                    val11 = os.system(val1)
                    val22 = os.system(val2)
                    val33 = os.system(val3)
                    val44 = os.system(val4)
                    val55 = os.system(val5)
                    val66 = os.system(val6)
                    val77 = os.system(val7)
                    val88 = os.system(val8)
                    val99 = os.system(val9)
            
                    function_add(a, k)
            
                    val = os.system('framework_builder fes.cgd 1 COF-5 node.xyz linker.xyz 10')
                    cif_make = 'network -cif COF-5_framework.cssr'
                    val_cif = os.system(cif_make)
                                              
            
        
                elif a[k][1] == 2:
                    val1 = 'cp' + ' ' + '../../../fxt.cgd' + ' ' + './'
                    val2 = 'cp' + ' ' + '../../../' +  str(a[k][2]) + '.xyz' + ' ' +  './'
                    val3 = 'cp' + ' ' + '../../../' + 'l' +  str(a[k][3]) + '.xyz' + ' ' +  './'
                    val4 = 'mv' + ' ' + str(a[k][2]) + '.xyz' + ' ' + 'node.xyz'
                    val5 = 'mv' + ' ' + 'l' + str(a[k][3]) + '.xyz' + ' ' + 'linker.xyz'
        
                    val6 = 'cp ../../../simulation.input ./'
                    val7 = 'cp ../../../pseudo_atoms.def ./'
                    val8 = 'cp ../../../force_field_mixing_rules.def ./'
                    val9 = 'cp ../../../force_field.def ./'
                    val11 = os.system(val1)
                    val22 = os.system(val2)
                    val33 = os.system(val3)
                    val44 = os.system(val4)
                    val55 = os.system(val5)
                    val66 = os.system(val6)
                    val77 = os.system(val7)
                    val88 = os.system(val8)
                    val99 = os.system(val9)
                    function_add(a, k)           
                    val = os.system('framework_builder fxt.cgd 1 COF-5 node.xyz linker.xyz 10')
                    cif_make = 'network -cif COF-5_framework.cssr'
                    val_cif = os.system(cif_make)
           
        
                elif a[k][1] == 3:
                    val1 = 'cp' + ' ' + '../../../hca.cgd' + ' ' + './'
                    val2 = 'cp' + ' ' + '../../../' +  str(a[k][2]) + '.xyz' + ' ' +  './'
                    val3 = 'cp' + ' ' + '../../../' + 'l' +  str(a[k][3]) + '.xyz' + ' ' +  './'
                    val4 = 'mv' + ' ' + str(a[k][2]) + '.xyz' + ' ' + 'node.xyz'
                    val5 = 'mv' + ' ' + 'l' + str(a[k][3]) + '.xyz' + ' ' + 'linker.xyz'
            
                    val6 = 'cp ../../../simulation.input ./'
                    val7 = 'cp ../../../pseudo_atoms.def ./'
                    val8 = 'cp ../../../force_field_mixing_rules.def ./'
                    val9 = 'cp ../../../force_field.def ./'
                    val11 = os.system(val1)
                    val22 = os.system(val2)
                    val33 = os.system(val3)
                    val44 = os.system(val4)
                    val55 = os.system(val5)
                    val66 = os.system(val6)
                    val77 = os.system(val7)
                    val88 = os.system(val8)
                    val99 = os.system(val9)
                    function_add(a, k)            
                    val = os.system('framework_builder hca.cgd 1 COF-5 node.xyz linker.xyz 10')
                    cif_make = 'network -cif COF-5_framework.cssr'
                    val_cif = os.system(cif_make)
            
        
                elif a[k][1] == 4:
                    val1 = 'cp' + ' ' + '../../../hcb.cgd' + ' ' + './'
                    val2 = 'cp' + ' ' + '../../../' +  str(a[k][2]) + '.xyz' + ' ' +  './'
                    val3 = 'cp' + ' ' + '../../../' + 'l' +  str(a[k][3]) + '.xyz' + ' ' +  './'
                    val4 = 'mv' + ' ' + str(a[k][2]) + '.xyz' + ' ' + 'node.xyz'
                    val5 = 'mv' + ' ' + 'l' + str(a[k][3]) + '.xyz' + ' ' + 'linker.xyz'            
                    val6 = 'cp ../../../simulation.input ./'
                    val7 = 'cp ../../../pseudo_atoms.def ./'
                    val8 = 'cp ../../../force_field_mixing_rules.def ./'
                    val9 = 'cp ../../../force_field.def ./'
                    val11 = os.system(val1)
                    val22 = os.system(val2)
                    val33 = os.system(val3)
                    val44 = os.system(val4)
                    val55 = os.system(val5)
                    val66 = os.system(val6)
                    val77 = os.system(val7)
                    val88 = os.system(val8)
                    val99 = os.system(val9)
                    function_add(a, k)           
                    val = os.system('framework_builder hcb.cgd 1 COF-5 node.xyz linker.xyz 10')
                    cif_make = 'network -cif COF-5_framework.cssr'
                    val_cif = os.system(cif_make)
            
            else:
                if a[k][1] == 1:
                    val1 = 'cp' + ' ' + '../../../sql.cgd' + ' ' + './'
                    val2 = 'cp' + ' ' + '../../../' +  str(a[k][2]) + '_4.xyz' + ' ' +  './'
                    val3 = 'cp' + ' ' + '../../../' + 'l' +  str(a[k][3]) + '.xyz' + ' ' +  './'
                    val4 = 'mv' + ' ' + str(a[k][2]) + '_4.xyz' + ' ' + 'node.xyz'
                    val5 = 'mv' + ' ' + 'l' + str(a[k][3]) + '.xyz' + ' ' + 'linker.xyz'            
                    val6 = 'cp ../../../simulation.input ./'
                    val7 = 'cp ../../../pseudo_atoms.def ./'
                    val8 = 'cp ../../../force_field_mixing_rules.def ./'
                    val9 = 'cp ../../../force_field.def ./'
                    val11 = os.system(val1)
                    val22 = os.system(val2)
                    val33 = os.system(val3)
                    val44 = os.system(val4)
                    val55 = os.system(val5)
                    val66 = os.system(val6)
                    val77 = os.system(val7)
                    val88 = os.system(val8)
                    val99 = os.system(val9)
                    function_add(a, k)           
                    val = os.system('framework_builder sql.cgd 1 COF-5 node.xyz linker.xyz 10')
                    cif_make = 'network -cif COF-5_framework.cssr'
                    val_cif = os.system(cif_make)            
        
                elif a[k][1] == 2:
                    val1 = 'cp' + ' ' + '../../../htb.cgd' + ' ' + './'
                    val2 = 'cp' + ' ' + '../../../' +  str(a[k][2]) + '_4.xyz' + ' ' +  './'
                    val3 = 'cp' + ' ' + '../../../' + 'l' +  str(a[k][3]) + '.xyz' + ' ' +  './'
                    val4 = 'mv' + ' ' + str(a[k][2]) + '_4.xyz' + ' ' + 'node.xyz'
                    val5 = 'mv' + ' ' + 'l' + str(a[k][3]) + '.xyz' + ' ' + 'linker.xyz'       
                    val6 = 'cp ../../../simulation.input ./'
                    val7 = 'cp ../../../pseudo_atoms.def ./'
                    val8 = 'cp ../../../force_field_mixing_rules.def ./'
                    val9 = 'cp ../../../force_field.def ./'
                    val11 = os.system(val1)
                    val22 = os.system(val2)
                    val33 = os.system(val3)
                    val44 = os.system(val4)
                    val55 = os.system(val5)
                    val66 = os.system(val6)
                    val77 = os.system(val7)
                    val88 = os.system(val8)
                    val99 = os.system(val9)
                    function_add(a, k)
                    val = os.system('framework_builder htb.cgd 1 COF-5 node.xyz linker.xyz 10')
                    cif_make = 'network -cif COF-5_framework.cssr'
                    val_cif = os.system(cif_make)
           
                elif a[k][1] == 3:
                    val1 = 'cp' + ' ' + '../../../kgm.cgd' + ' ' + './'
                    val2 = 'cp' + ' ' + '../../../' +  str(a[k][2]) + '_4.xyz' + ' ' +  './'
                    val3 = 'cp' + ' ' + '../../../' + 'l' +  str(a[k][3]) + '.xyz' + ' ' +  './'
                    val4 = 'mv' + ' ' + str(a[k][2]) + '_4.xyz' + ' ' + 'node.xyz'
                    val5 = 'mv' + ' ' + 'l' + str(a[k][3]) + '.xyz' + ' ' + 'linker.xyz'           
                    val6 = 'cp ../../../simulation.input ./'
                    val7 = 'cp ../../../pseudo_atoms.def ./'
                    val8 = 'cp ../../../force_field_mixing_rules.def ./'
                    val9 = 'cp ../../../force_field.def ./'
                    val11 = os.system(val1)
                    val22 = os.system(val2)
                    val33 = os.system(val3)
                    val44 = os.system(val4)
                    val55 = os.system(val5)
                    val66 = os.system(val6)
                    val77 = os.system(val7)
                    val88 = os.system(val8)
                    val99 = os.system(val9)
                    function_add(a, k)
                    val = os.system('framework_builder kgm.cgd 1 COF-5 node.xyz linker.xyz 10')
                    cif_make = 'network -cif COF-5_framework.cssr'
                    val_cif = os.system(cif_make)
        
                elif a[k][1] == 4:
                    val1 = 'cp' + ' ' + '../../../krr.cgd' + ' ' + './'
                    val2 = 'cp' + ' ' + '../../../' +  str(a[k][2]) + '_4.xyz' + ' ' +  './'
                    val3 = 'cp' + ' ' + '../../../' + 'l' +  str(a[k][3]) + '.xyz' + ' ' +  './'
                    val4 = 'mv' + ' ' + str(a[k][2]) + '_4.xyz' + ' ' + 'node.xyz'
                    val5 = 'mv' + ' ' + 'l' + str(a[k][3]) + '.xyz' + ' ' + 'linker.xyz'    
                    val6 = 'cp ../../../simulation.input ./'
                    val7 = 'cp ../../../pseudo_atoms.def ./'
                    val8 = 'cp ../../../force_field_mixing_rules.def ./'
                    val9 = 'cp ../../../force_field.def ./'
                    val11 = os.system(val1)
                    val22 = os.system(val2)
                    val33 = os.system(val3)
                    val44 = os.system(val4)
                    val55 = os.system(val5)
                    val66 = os.system(val6)
                    val77 = os.system(val7)
                    val88 = os.system(val8)
                    val99 = os.system(val9)
                    function_add(a, k)    
                    val = os.system('framework_builder krr.cgd 1 COF-5 node.xyz linker.xyz 10')
                    cif_make = 'network -cif COF-5_framework.cssr'
                    val_cif = os.system(cif_make)
            
    
            if os.path.exists('COF-5_framework.cif'):
                
                
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
                
                os.chdir(new_path)
                
                if len(l_id) == 0:
                    selectivity,heat_sorption,co2_capatity,h2_capatity,co2_capatity_stp,h2_capatity_stp = RASPA_simualtion_run()
                    l_id.append(a[k])
                    l_co2_capatity.append(co2_capatity)
                    l_h2_capatity.append(h2_capatity)
                    l_selectivity.append(selectivity)
                    l_co2_capatity_stp.append(co2_capatity_stp)
                    l_h2_capatity_stp.append(h2_capatity_stp)
                    l_sorption.append(heat_sorption)
        
                    os.chdir(path) #返回到第N代的文件夹中                        
                    with open('gas_number.data','a') as h:
                        h.write(str(selectivity) + '\n')
                    h.close()
    
                    with open('gas_capatity.data','a') as h:
                        h.write(str(co2_capatity) + ' ')
                        h.write(str(h2_capatity) + '\n')
                    h.close()
    
                    with open('gas_capatity_stp.data','a') as f:
                        f.write(str(co2_capatity_stp) + ' ')
                        f.write(str(h2_capatity_stp) + '\n')
                    f.close()
        
                    with open('gas_desorption.data','a') as u:            
                        u.write(str(heat_sorption) + '\n')
                    u.close()        
    
                    return(a)
                else:    
                    dashabi = 0
                    for shabi in range(len(l_id)):
                    
                        if (a[k] == l_id[shabi]).all():                                               
                            os.chdir(path) #返回到第N代的文件夹中                        
                            with open('gas_number.data','a') as h:
                                 h.write(str(l_selectivity[shabi]) + '\n')
                            h.close()
        
                            with open('gas_capatity.data','a') as h:
                                 h.write(str(l_co2_capatity[shabi]) + ' ')
                                 h.write(str(l_h2_capatity[shabi]) + '\n')
                            h.close()
        
                            with open('gas_capatity_stp.data','a') as f:
                                f.write(str(l_co2_capatity_stp[shabi]) + ' ')
                                f.write(str(l_h2_capatity_stp[shabi]) + '\n')
                            f.close()
        
                            with open('gas_desorption.data','a') as u:            
                                u.write(str(l_sorption[shabi]) + '\n')
                            u.close()
                            return(a)
                        else:
                            dashabi += 1
                            if dashabi == len(l_id):
                                selectivity,heat_sorption,co2_capatity,h2_capatity,co2_capatity_stp,h2_capatity_stp = RASPA_simualtion_run()
                                l_id.append(a[k])
                                l_co2_capatity.append(co2_capatity)
                                l_h2_capatity.append(h2_capatity)
                                l_selectivity.append(selectivity)
                                l_co2_capatity_stp.append(co2_capatity_stp)
                                l_h2_capatity_stp.append(h2_capatity_stp)
                                l_sorption.append(heat_sorption)        
                                os.chdir(path) #返回到第N代的文件夹中                        
                                with open('gas_number.data','a') as h:
                                    h.write(str(selectivity) + '\n')
                                h.close()        
                                with open('gas_capatity.data','a') as h:
                                    h.write(str(co2_capatity) + ' ')
                                    h.write(str(h2_capatity) + '\n')
                                h.close()
        
                                with open('gas_capatity_stp.data','a') as f:
                                    f.write(str(co2_capatity_stp) + ' ')
                                    f.write(str(h2_capatity_stp) + '\n')
                                f.close()
        
                                with open('gas_desorption.data','a') as u:            
                                    u.write(str(heat_sorption) + '\n')
                                u.close()                
                                return(a)
                            else:
                                pass
            else:
                os.chdir(path) #返回到第N代的文件夹中
                shanchu_lujing = 'rm -rf' + ' ' + str(k) + '_' + str(a[k][0]) + '_' + str(a[k][1]) + '_' + str(a[k][2])+ '_' + str(a[k][3])+ '_' + str(a[k][4])
                os.system(shanchu_lujing)
                change_site = random.randint(1, 4)
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
                
                return(cof_building(a,k,Topo_numer,Nodenumber,linkernumber))
        else:
            pilipala += 1
            if pilipala == len(dongtaishuzu_id)-1:
                
                os.chdir(path) #返回到第N代的文件夹中
                shanchu_lujing = 'rm -rf' + ' ' + str(k) + '_' + str(a[k][0]) + '_' + str(a[k][1]) + '_' + str(a[k][2])+ '_' + str(a[k][3])+ '_' + str(a[k][4])
                os.system(shanchu_lujing)
                change_site = random.randint(1, 4)
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
                print(a[k])
                return(cof_building(a,k,Topo_numer,Nodenumber,linkernumber))
            else:
                pass
        
      
def RASPA_simualtion_run():
    val1 = 'network -ha -vol 1.2 1.2 50000 volume.data COF-5_framework.cssr'
    
    os.system(val1)          
    with open('volume.data','r') as f:
        lines = f.readlines()
        line = lines[0].split()
        volume_acess = float(line[7])
        density = float(line[5])
        
    f.close()
    
    with open('COF-5_framework.cif','r+') as f:        
            lines = f.readlines()
            length = len(lines)
            total_number_atom_in = length - 30
            line_alph = lines[12].split()
            line_beta = lines[13].split()
            line_gamma = lines[14].split()
            line_a = lines[9].split()
            line_b = lines[10].split()
            line_c = lines[11].split()
            cell_alph  = float(line_alph[1])
            cell_beta  = float(line_beta[1])
            cell_gamma = float(line_gamma[1])
            cell_a = float(line_a[1])
            cell_b = float(line_b[1])
            cell_c = float(line_c[1])    
    f.close()
    
    with open('volume.data','r') as f:
        lines = f.readlines()
        line = lines[0].split()
        vl_fraction = float(line[9])
        with open('simulation.input','r') as p:
            with open('simulation_1.input','w') as q:
                lines_si = p.readlines()
                len_si = len(lines_si)
                for i in range(20):
                    if i == 11 and total_number_atom_in >= 950:
                        line = lines_si[i].split()
                        q.write(str(line[0]) + ' ')
                        q.write(str('CoulombShifted') + '\n')
                    if i == 19:
                        line = lines_si[i].split()
                        if total_number_atom_in >= 100 and total_number_atom_in < 200:
                            q.write(str(line[0]) + ' ')
                            q.write(str(1) + ' ')
                            q.write(str(1) + ' ')
                            q.write(str(2) + '\n')
                        elif total_number_atom_in < 100:
                            q.write(str(line[0]) + ' ')
                            q.write(str(2) + ' ')
                            q.write(str(2) + ' ')
                            q.write(str(2) + '\n')
                        elif total_number_atom_in >= 300 and total_number_atom_in < 400: 
                            q.write(str(line[0]) + ' ')
                            q.write(str(1) + ' ')
                            q.write(str(1) + ' ')
                            q.write(str(2) + '\n')
                        elif total_number_atom_in>=400 and total_number_atom_in < 500:
                            q.write(str(line[0]) + ' ')
                            q.write(str(1) + ' ')
                            q.write(str(1) + ' ')
                            q.write(str(2) + '\n')
                        else:
                            q.write(str(line[0]) + ' ')
                            q.write(str(1) + ' ')
                            q.write(str(1) + ' ')
                            q.write(str(2) + '\n')
                    else:
                        q.write(lines_si[i])
                for j in range(20,len_si):
                    if j == 20:
                        line = lines_si[j].split()
                        line[1] = vl_fraction
                        q.write(str(line[0]) + ' ')
                        q.write(str(line[1]) + '\n')
                    else:
                        q.write(lines_si[j])
            q.close()
        p.close()
    f.close()
    
    with open('COF-5_framework.cif','r') as f:
        with open('COF-5_framework_new.cif','w') as q:        
                lines = f.readlines()
                len_cof_5 = len(lines)
                for i in range(30):
                    q.write(str(lines[i]))
                for j in range(30,len_cof_5):
                    line = lines[j].split()
                    q.write(str(line[1]) + ' ')
                    q.write(str(line[1]) + ' ')
                    q.write(str(line[2]) + ' ')
                    q.write(str(line[3]) + ' ')
                    q.write(str(line[4]) + '\n')
        q.close()       
    f.close()
    
    
    val5 = 'rm -rf simulation.input'
    val6 = 'mv simulation_1.input simulation.input'
    os.system(val5)
    os.system(val6)
    os.system('mv COF-5_framework_new.cif new.cif')
    print('===============Starting Simulation Desorption===============')
    os.system('simulate')
    path = os.getcwd()
    os.chdir('Output')
    os.chdir('System_0') 
    
    os.system('grep -r "Average loading absolute" * > out_sorption.data')
    
    with open('out_sorption.data','r') as f:    
        lines = f.readlines()
        line_co2 = lines[1].split()
        line_co2_stp = lines[3].split()
        line_h2 = lines[6].split()
        line_h2_stp = lines[8].split()
        N_co2 = float(line_co2[5])
        N_stp_co2 = float(line_co2_stp[6])
        N_h2 = float(line_h2[5])
        N_stp_h2 = float(line_h2_stp[6])
        
        
    f.close()
    
    os.system('rm -rf out_sorption.data')
    os.system('grep -C 10 "Heat of desorption:" * > out_heat_sorption.data')    
    with open('out_heat_sorption.data','r') as f:
        lines = f.readlines()
        line = lines[19].split()
        print(line[3])
        heat_sorption = float(line[2])
    f.close()
    os.system('rm -rf *')
    os.chdir(path)    
         
    with open('simulation.input','r') as f:
        with open('simulation_1.input','w') as q:
            lines = f.readlines()
            len_simulation = len(lines)
            for i in range(22):
                q.write(str(lines[i]))
            for j in range(22,len_simulation):
                if j == 22:
                    line = lines[j].split()
                    q.write(str(line[0]) + ' ')
                    line[1] = 100000
                    q.write(str(line[1]) + '\n')
                else:
                    q.write(str(lines[j]))
    
        q.close()        
    f.close()
    val6 = 'mv simulation_1.input simulation.input'
    os.system(val6)
    print('===============Starting Simulation Desorption===============')
    os.system('simulate')
    path = os.getcwd()
    os.chdir('Output')
    os.chdir('System_0')
    os.system('grep -r "Average loading absolute" * > out_desorption.data')
    with open('out_desorption.data','r') as f:    
        lines = f.readlines()
        line_co2 = lines[1].split()
        line_co2_stp = lines[3].split()
        line_h2 = lines[6].split()
        line_h2_stp = lines[8].split()
        N_co2_desorption = float(line_co2[5])
        N_stp_co2_desorption = float(line_co2_stp[6])
        N_h2_desoption = float(line_h2[5])
        N_stp_h2_desorption = float(line_h2_stp[6])        
    f.close()
    co2_capatity = N_co2 - N_co2_desorption
    h2_capatity = N_h2 - N_h2_desoption
    co2_capatity_stp = N_stp_co2 - N_stp_co2_desorption
    h2_capatity_stp = N_stp_h2 - N_stp_h2_desorption
    selectivity = N_co2/N_h2
    os.system('rm -rf out_desorption.data')  
    os.chdir(path)
           
    return(selectivity,heat_sorption,co2_capatity,h2_capatity,co2_capatity_stp,h2_capatity_stp)


def cof_build(a,i,ge_ti_shu_shumu):
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
          print('============Starting Cross===========')  
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
        print('============Starting Mutation===========')
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
    
    bibili = 0
    for j in range(len(dongtaishuzu_id)-1):
        if (d[0] == dongtaishuzu_id[j]).all():
            return(d[0])
        else:
            bibili += 1
            if bibili == len(dongtaishuzu_id)-1:
                return(cof_build(a, i, ge_ti_shu_shumu))
            else:
                pass

 

    
###############################Main Process############################
generation = 21 #GA迭代次数
topo_number = 4
node_number = 8
linker_number = 29
ge_ti_shu_shumu = 100

l_id = []
l_selectivity = []
l_sorption = []
l_co2_capatity = []
l_h2_capatity = []
l_co2_capatity_stp = []
l_h2_capatity_stp = []
dongtaishuzu_id = []
dongtaishuzu_density = []
dongtaishuzu_PLD_LCD = []
dongtaishuzu_old_propertity = []
dongtaishuzu_valfaction = []

with open('work_id_all.data','r') as f:
    lines = f.read()        
    b = lines.split('\n')    
    for i in range(len(b)-1):
        b[i] = b[i].split()
        c = np.array(b[i]).astype(np.int)       
        dongtaishuzu_id.append(c)
f.close()

with open('work_density.data','r') as f:
    lines = f.readlines()
    for i in range(len(lines)):
        line = lines[i].split()
        dongtaishuzu_density.append(float(line[0]))
f.close()

with open('work_vl_fraction.data','r') as f:
    lines = f.readlines()
    for i in range(len(lines)):
        line = lines[i].split()
        dongtaishuzu_valfaction.append(float(line[0]))
f.close()

with open('work_PLD_LCD.data','r') as f:
    lines = f.read()
    b = lines.split('\n')
    for i in range(len(b)):       
        dongtaishuzu_PLD_LCD.append(b[i])
f.close()

with open('work_old_propertity.data','r') as f:
    lines = f.read()
    b = lines.split('\n')
    for i in range(len(b)):       
        dongtaishuzu_old_propertity.append(b[i])
f.close()

      

for pa in range(20):
    pa_path = os.getcwd()
    pa_new_path = pa_path + '/' + str(pa) + '_' + 'gas'
    os.mkdir(pa_new_path)
    os.chdir(pa_new_path) 
    #1=fes.cgd 2=fxt.cgd 3=hca.cgd 4=hcb.cgd
    a = np.random.randint(0,5,size=[ge_ti_shu_shumu,5])
    for i in range(ge_ti_shu_shumu):    
        a[i][0] = random.randint(0,1) #C3_C4 C3 = 0 C4 = 1    
        a[i][1] = random.randint(1, topo_number) #topo
        a[i][2] = random.randint(1, node_number) #node
        a[i][3] = random.randint(1, linker_number) #linker
        a[i][4] = random.randint(0, 9) #function id


    #print('================Father and Mother is done=================')
    for j in range(1,generation):
   
        path = os.getcwd() #获得初始文件夹路径
        newpath = path + '/' + str(j) + '_' + 'gengeration'
        os.mkdir(newpath)
        os.chdir(newpath) #进入到第N代文件夹中
        for k in range(ge_ti_shu_shumu):        
            a = cof_building(a,k,topo_number,node_number,linker_number) #在第n代文件夹中        


        with open('a.data','w') as f:
            f.write(str(a))
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
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
