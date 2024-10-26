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
from sklearn.ensemble import RandomForestRegressor
from sklearn import metrics
from sklearn.metrics import accuracy_score
import pandas as pd
#import seaborn as sns
#import matplotlib.pyplot as plt
import random
import tensorflow as tf
from numpy import concatenate
from sklearn.preprocessing import MinMaxScaler
from keras.models import Sequential
from keras.layers.core import Dense, Dropout, Activation
from keras import layers



def cof_building(a,k,Topo_numer,Nodenumber,linkernumber,scaled):

    pilipala = 0
    path = os.getcwd() #当前在最外层

    new_path = path + '/' + str(a[k][0]) + '_' + str(a[k][1]) + '_' + str(a[k][2])+ '_' + str(a[k][3])+ '_' + str(a[k][4])
    for j in range(len(dongtaishuzu_id)):
        if (a[k] == dongtaishuzu_id[j]).all():

            os.chdir(new_path)  # 进入到第N代第k个个体文件夹中
            l_train_id.append(j)

            val6 = 'cp ../simulation.input ./'
            val7 = 'cp ../pseudo_atoms.def ./'
            val8 = 'cp ../force_field_mixing_rules.def ./'
            val9 = 'cp ../force_field.def ./'
            val66 = os.system(val6)
            val77 = os.system(val7)
            val88 = os.system(val8)
            val99 = os.system(val9)

            os.chdir(mk_path) #进入第n代记录数据
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
                
            os.chdir(new_path) #返回k个个体文件夹

            if len(l_id) == 0:
                selectivity, heat_sorption, co2_capatity, h2_capatity, co2_capatity_stp, h2_capatity_stp = RASPA_simualtion_run()
                scaled['gas_v_stp_v'].iloc[int(j)] = selectivity
                l_id.append(a[k])
                l_co2_capatity.append(co2_capatity)
                l_h2_capatity.append(h2_capatity)
                l_selectivity.append(selectivity)
                l_co2_capatity_stp.append(co2_capatity_stp)
                l_h2_capatity_stp.append(h2_capatity_stp)
                l_sorption.append(heat_sorption)

                os.chdir(mk_path)  #进入第n代记录数据
                with open('gas_number.data', 'a') as h:
                    h.write(str(selectivity) + '\n')
                h.close()

                with open('gas_capatity.data', 'a') as h:
                    h.write(str(co2_capatity) + ' ')
                    h.write(str(h2_capatity) + '\n')
                h.close()

                with open('gas_capatity_stp.data', 'a') as f:
                    f.write(str(co2_capatity_stp) + ' ')
                    f.write(str(h2_capatity_stp) + '\n')
                f.close()

                with open('gas_desorption.data', 'a') as u:
                    u.write(str(heat_sorption) + '\n')
                u.close()
                os.chdir(path)  # 返回最外层
                return (a,scaled)
            else:
                dashabi = 0
                for shabi in range(len(l_id)):
                    if (a[k] == l_id[shabi]).all():
                        os.chdir(mk_path)  # 返回到第N代的文件夹中
                        with open('gas_number.data', 'a') as h:
                            h.write(str(l_selectivity[shabi]) + '\n')
                        h.close()

                        with open('gas_capatity.data', 'a') as h:
                            h.write(str(l_co2_capatity[shabi]) + ' ')
                            h.write(str(l_h2_capatity[shabi]) + '\n')
                        h.close()

                        with open('gas_capatity_stp.data', 'a') as f:
                            f.write(str(l_co2_capatity_stp[shabi]) + ' ')
                            f.write(str(l_h2_capatity_stp[shabi]) + '\n')
                        f.close()

                        with open('gas_desorption.data', 'a') as u:
                            u.write(str(l_sorption[shabi]) + '\n')
                        u.close()
                        os.chdir(path)  # 返回最外层
                        return (a,scaled)
                    else:
                        dashabi += 1
                        if dashabi == len(l_id):
                            selectivity, heat_sorption, co2_capatity, h2_capatity, co2_capatity_stp, h2_capatity_stp = RASPA_simualtion_run()
                            scaled['gas_v_stp_v'].iloc[int(j)] = selectivity
                            l_id.append(a[k])
                            l_co2_capatity.append(co2_capatity)
                            l_h2_capatity.append(h2_capatity)
                            l_selectivity.append(selectivity)
                            l_co2_capatity_stp.append(co2_capatity_stp)
                            l_h2_capatity_stp.append(h2_capatity_stp)
                            l_sorption.append(heat_sorption)
                            os.chdir(mk_path)  # 返回到第N代的文件夹中
                            with open('gas_number.data', 'a') as h:
                                h.write(str(selectivity) + '\n')
                            h.close()
                            with open('gas_capatity.data', 'a') as h:
                                h.write(str(co2_capatity) + ' ')
                                h.write(str(h2_capatity) + '\n')
                            h.close()

                            with open('gas_capatity_stp.data', 'a') as f:
                                f.write(str(co2_capatity_stp) + ' ')
                                f.write(str(h2_capatity_stp) + '\n')
                            f.close()

                            with open('gas_desorption.data', 'a') as u:
                                u.write(str(heat_sorption) + '\n')
                            u.close()
                            os.chdir(path)  # 返回最外层
                            return (a,scaled)
                        else:
                            pass

        else:
            pilipala += 1
            if pilipala == len(dongtaishuzu_id)-1:
                os.chdir(path) #返回到最外层
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
                return(cof_building(a,k,Topo_numer,Nodenumber,linkernumber,scaled))
            else:
                pass
        
      
def RASPA_simualtion_run():
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

def RNN(train_x_,train_y_,train_x):
    model = Sequential()
    model.add(layers.SimpleRNN(units=1000, return_sequences=True))
    model.add(Activation('relu'))
    model.add(Dropout(0.1))
    model.add(layers.SimpleRNN(units=1000, return_sequences=True))
    model.add(Activation('relu'))
    model.add(Dropout(0.1))
    model.add(layers.SimpleRNN(units=500))
    model.add(Activation('relu'))
    model.add(Dropout(0.1))
    model.add(Dense(1))
    optimizer = tf.keras.optimizers.Adam(0.0001)
    model.compile(loss='mean_squared_error', optimizer=optimizer, metrics=['mae'])
    history = model.fit(train_x_, train_y_, epochs=500, batch_size=64, verbose=0)

    '''第n次训练得到的预测值'''
    y_pred_NN = model.predict(train_x)
    y_pre_list = []
    for dashabi in range(len(y_pred_NN)):
        y_pre_list.append(float(y_pred_NN[dashabi]))
    a_y_pre = np.array(y_pre_list)

    '''排序第n次训练得到的预测值'''
    b = np.argsort(-a_y_pre)
    return(b,a_y_pre)


###############################Main Process############################
'''构建全部数据库的data'''
data = pd.read_csv('allnew.csv')
Y = data['gas_v_stp_v']
data_ID = data['ID']
data = data.drop(['ID','gas_v_stp_v'],axis =1)

values = data.values
scaler = MinMaxScaler(feature_range=(0, 1))
scaled = pd.DataFrame(scaler.fit_transform(values))
scaled = pd.concat([scaled,Y],axis=1)
data = pd.concat([data,data_ID],axis=1)
train_x = scaled.iloc[:,0:17]
train_x = np.array(train_x)
train_x = np.reshape(train_x,(train_x.shape[0],1,17))

generation = 21 #GA迭代次数
topo_number = 4
node_number = 8
linker_number = 29
ge_ti_shu_shumu = 300

l_id = []
l_train_id = []

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

with open('fina_id_all.data','r') as f:
    lines = f.read()        
    b = lines.split('\n')    
    for i in range(len(b)-1):
        b[i] = b[i].split()
        c = np.array(b[i]).astype(np.int)       
        dongtaishuzu_id.append(c)
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

      


pa_path = os.getcwd()

#1=fes.cgd 2=fxt.cgd 3=hca.cgd 4=hcb.cgd
a = np.random.randint(0,5,size=[ge_ti_shu_shumu,5])
for i in range(ge_ti_shu_shumu):
    a[i][0] = random.randint(0,1) #C3_C4 C3 = 0 C4 = 1
    a[i][1] = random.randint(1, topo_number) #topo
    a[i][2] = random.randint(1, node_number) #node
    a[i][3] = random.randint(1, linker_number) #linker
    a[i][4] = random.randint(0, 9) #function id
#print('================Father and Mother is done=================')
num_same_100 = []
num_same_10 = []
for beat in range(1,generation):


    path = os.getcwd() #获得初始文件夹路径
    mk_path = path + '/' + str(beat) + '_generation'
    os.mkdir(mk_path)
    #newpath = path + '/' + str(j) + '_' + 'gengeration'
    #os.mkdir(newpath)
    #os.chdir(newpath) #进入到第N代文件夹中
    if beat == 1:
        for k in range(ge_ti_shu_shumu):
            a,scaled  = cof_building(a,k,topo_number,node_number,linker_number,scaled)  #在第n代文件夹中

    else:
        a = np.random.randint(0, 5, size=[len(l_train_id), 5])
        for k in range(len(l_train_id)):
            a[k][0] = int(data_ID[int(l_train_id[k])].split()[0])
            a[k][1] = int(data_ID[int(l_train_id[k])].split()[1])
            a[k][2] = int(data_ID[int(l_train_id[k])].split()[2])
            a[k][3] = int(data_ID[int(l_train_id[k])].split()[3])
            a[k][4] = int(data_ID[int(l_train_id[k])].split()[4])
            a, scaled = cof_building(a, k, topo_number, node_number, linker_number,scaled)  # 在第n代文件夹中

    RNN_path = path + '/' + str(beat) + '_RNN_GA'
    os.mkdir(RNN_path)
    os.chdir(RNN_path)
    txt_GA_name_10 = str(beat) + '_RNN_GA_10.txt'
    txt_GA_name_100 = str(beat) + '_RNN_GA_100.txt'
    txt_GA_pre     = str(beat) + '_RNN_GA_pre.txt'
    txt_GA_pre_100 = str(beat) + '_RNN_GA_pre_100.txt'
    txt_GA_pre_10 = str(beat) + '_RNN_GA_pre_10.txt'
    train = pd.DataFrame()
    for i in range(len(l_train_id)):
        train = pd.concat([train, scaled.iloc[[int(l_train_id[i])]]], axis=0)
    train_x_ = train.iloc[:, 0:17]
    train_x_ = np.array(train_x_)
    train_x_ = np.reshape(train_x_, (train_x_.shape[0], 1, 17))
    train_y_ = train.iloc[:, -1]
    b ,y_pre= RNN(train_x_,train_y_,train_x)
    max_id = []
    num_same = 0
    num_same_num = 0

    with open(txt_GA_pre_10,'w') as f:
        for i in range(10):
            f.write(str(y_pre[int(b[i])]) + '\n')
    f.close()

    with open(txt_GA_pre_100,'w') as f:
        for i in range(100):
            f.write(str(y_pre[int(b[i])]) + '\n')
    f.close()

    '''记录第n次GA中预测得到的前100的COF信息'''
    with open(txt_GA_name_100, 'w') as f:
        for i in range(100):
            f.write(data['ID'].iloc[int(b[i])] + '\n')
    f.close()

    with open(txt_GA_pre,'w') as f:
        for i in range(len(y_pre)):
            f.write(str(y_pre[i]) + '\n')
    f.close()

    '''记录第n次GA中预测得到的前10的COF信息'''
    with open(txt_GA_name_10, 'w') as f:
        for i in range(10):
            f.write(data['ID'].iloc[int(b[i])] + '\n')
    f.close()

    '''预测前100的COF数目'''
    for i in range(100):
        l_train_id.append(int(b[i]))

    '''将现有的预测前100的结构加入到训练列表并排除相同ID'''
    l_train_id = list(np.unique(l_train_id))

    print("第{}次训练需要训练{}个COF结构".format(beat + 1, len(l_train_id)))

    os.chdir(path) #返回到初始路径

    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
