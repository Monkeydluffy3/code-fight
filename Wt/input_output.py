#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Feb  7 11:49:59 2018

@author: as
"""

	

import zipfile
import os
import pickle
path_list = []
for i in range(1,21):
    for file in os.listdir("/home/as/Documents/Wt/problem/"+str(i)):
        if file.endswith(".zip"):
            path_list.append(os.path.join("/home/as/Documents/Wt/problem/"+str(i), file))
            
for i in range(0,20):
    zip_ref = zipfile.ZipFile(path_list[i], 'r')
    zip_ref.extractall("/home/as/Documents/Wt/problem/"+str(i+1))
zip_ref.close()
shukla =[]
astha =[]

for i in range(1,21):
    temp1 = []
    temp2 = []
    shu = ''
    ast = ''
    for file in os.listdir("/home/as/Documents/Wt/problem/"+str(i)+"/in"):
            if file.endswith(".txt"):
                temp1.append(os.path.join("/home/as/Documents/Wt/problem/"+str(i)+"/in",file))
                temp2.append(os.path.join("/home/as/Documents/Wt/problem/"+str(i)+"/out",file))
    shu+=str(len(temp1))
    shu+="\n"
    for x in temp1:
        f = open(x,'r')
        shu+=f.read()
    #print(shu)
    #print("###############")
    
    for x in temp2:
        f = open(x,'r')
        ast+=f.read()
    #print(ast)    
    shukla.append(shu)
    astha.append(ast)      
                    
manhas = open("Input.pickle","wb")
pickle.dump(shukla,manhas)
manhas.close()

vikas = open("Output.pickle","wb")
pickle.dump(astha,vikas)
vikas.close()
