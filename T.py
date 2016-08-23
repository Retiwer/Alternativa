# -*- coding: utf-8 -*-
"""
Created on Wed Aug 17 11:00:32 2016

@author: Carlos
"""

import Libreria


def Port():  
    Min_Col     =   2
    Max_Col     =   4500
    Min_Fil     =   7
    Max_Fil     =   16
    Variable    =   4
    
        
    Tabla, N = tabla(Min_Col, Max_Col, Min_Fil, Max_Fil, Variable)  #Llama a la funcion tabla y 
    #print Tabla.shape[0]
    #print Tabla.shape[1]
    
    y = []
    w = []
    
    s1 = []
    Var = var(N, Variable)
    
    Ind, aux = np.unique(Var, return_counts=True)    #Ver cuantos elementos                                                  #unicos estan en la                                                   #lista
    for i in range(len(aux)):
        if aux[i] >= 35:
            y.append(aux[i])
            w.append(Ind[i])
    #print y
    s0 = []
    for i in range(len(w)):
        for j in range(len(Var)):
            if Var[j]==w[i]:
                s0.append(Var[j])
                s1.append(j)
    Ind, aux = np.unique(s0, return_counts=True)    #Ver cuantos elementos                                                  #unicos estan en la                                                   #lista            
    #print s0
    #print s0[aux[0]-1]
    #print s0[aux[0]+aux[1]-1]
    #print s0[aux[0]+aux[1]+aux[2]-1]
    #print s0[aux[0]+aux[1]+aux[2]+aux[3]-1]
    #print s0[aux[0]+aux[1]+aux[2]+aux[3]+aux[4]-1]
    #print s0[aux[0]+aux[1]+aux[2]+aux[3]+aux[4]+aux[5]-1]
    
    e0=[]
    e1=[]
    e2=[]
    e3=[]
    e4=[]
    e5=[]
    r0=[]
    r1=[]
    r2=[]
    r3=[]
    r4=[]
    r5=[]
    for i in range(0,aux[0]-1,1):
        e0.append(s0[i])
        r0.append(s1[i])
    for i in range(aux[0],aux[0]+aux[1]-1,1):
        e1.append(s0[i])
        r1.append(s1[i])
    for i in range(aux[0]+aux[1],aux[0]+aux[1]+aux[2]-1,1):
        e2.append(s0[i])
        r2.append(s1[i])
    for i in range(aux[0]+aux[1]+aux[2],aux[0]+aux[1]+aux[2]+aux[3]-1,1):
        e3.append(s0[i])
        r3.append(s1[i])
    for i in range(aux[0]+aux[1]+aux[2]+aux[3],aux[0]+aux[1]+aux[2]+aux[3]+aux[4]-1,1):
        e4.append(s0[i])
        r4.append(s1[i])
    for i in range(aux[0]+aux[1]+aux[2]+aux[3]+aux[4],aux[0]+aux[1]+aux[2]+aux[3]+aux[4]+aux[5]-1,1):
        e5.append(s0[i])
        r5.append(s1[i])
    
    #print e0
    #print r0
    #print '-------'
    r0=List(r0,390)
    e0=List(e0,390)
    #print len(r0)
    r1=List(r1,390)
    e1=List(e1,390)    
    #print len(r1)
    r2=List(r2,390)
    e2=List(e2,390)
    #print len(r2)
    r3=List(r3,390)
    e3=List(e3,390)
    #print len(r3)
    r4=List(r4,390)
    e4=List(e4,390)
    #print len(r4)
    r5=List(r5,390)
    e5=List(e5,390)
    #print len(r5)
    #print '-------'
    new_list=[]
    new_list=r0+r1+r2+r3+r4+r5
    new_list2=[]
    new_list2=e0+e1+e2+e3+e4+e5
    #print new_list
    #print len(new_list)
    
    
    NTabla = np.zeros((1, Max_Fil-Min_Fil))   #Crear el primer valor de un vector de 
                                        #dimensiones 1x(cantidad de variables)
    NTabla = np.delete(NTabla, 0, 0)
    
    for i in range (len(new_list)):
        g=Tabla[new_list[i]]
        NTabla = np.vstack((NTabla,g))
    Tabla = NTabla
    #print Tabla
    #print new_list2
    return Tabla,new_list2