#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Feb  6 13:17:19 2018

@author: as
"""

import bs4 as bs
import os
import pickle

path_list = []

for i in range(1,21):
    for file in os.listdir("/home/as/Documents/Wt/problem/"+str(i)):
        if file.endswith(".html"):
            path_list.append(os.path.join("/home/as/Documents/Wt/problem/"+str(i), file))
            
#print(path_list)        
coloum_name = ['Problem Statement','Constraints','Input','Output','Sample Input 1 Copy','Sample Output 1 Copy']
astha = {'Problem Statement' : [],'Constraints' :[],'Input':[],'Output':[],'Sample Input':[],'Sample Output':[]}             
data = []
for i in range(0,20):
    sou = open(path_list[i]).read()
    soup = bs.BeautifulSoup(sou,'lxml')     
    soup = soup.find('span',{'class' : 'lang-en'})
    
    for div in soup.find_all('div',{'class' : 'part'}):
            coloum = div.find('h3').text
            text = ''
            #print(coloum)
            if coloum in coloum_name: 
               if coloum == 'Problem Statement':
                   for paragraph in  div.find_all('p'):   
                           text+=paragraph.text
                           for x in paragraph.find_all('math'):
                               var = x.text
                               var1 =''
                               var1+=var
                               var1+=var
                               text = text.replace(var1,'')            
                   text = text.replace('\leq','≤')
                   astha[coloum].append(text)
                   #print(text)
               elif coloum == 'Constraints':
                   for span in div.find_all('script'):
                       text+=span.text
                       text+='\n'
                   text = text.replace('\leq','≤')
                   astha[coloum].append(text)
                   #print(text)
               elif coloum == 'Input':
                   text+=div.text
                   for x in div.find_all('math'):
                       var = x.text
                       var1 = ''
                       var1+=var
                       var1+=var
                       text = text.replace(var1,'')
                   astha[coloum].append(text)
                   #print(text)
               elif coloum == 'Output':
                   text+=div.find('p').text
                   for x in div.find_all('script'):
                       var = x.text
                       var1 = ''
                       var1+=var
                       var1+=var
                       text = text.replace(var1,'')
                   astha[coloum].append(text)
                   #print(text)
               elif coloum == 'Sample Input 1 Copy':
                   text+=div.find('pre').text
                   astha['Sample Input'].append(text)
               elif coloum == 'Sample Output 1 Copy':
                   text+=div.find('pre').text
                   astha['Sample Output'].append(text)
#for i in range(0,20):                   
#  print(ashta['Output'][i]) 
#  print('###########################')           
shukla = open("Problem.pickle","wb")
pickle.dump(astha,shukla)
shukla.close()            
