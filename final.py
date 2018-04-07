#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Mar 28 14:31:12 2018

@author: SD
"""
from flask import Flask as manhas,render_template,request
import urllib.request
import json
import random
import pickle
from sphere_engine import CompilersClientV3
from sphere_engine.exceptions import SphereEngineException
import time
import bs4 as bs
import urllib.request as req

T = True
F = False
# define access parameters
accessToken = 'd5549293157f874363dd97c218f73272'
endpoint = '59e166d8.compilers.sphere-engine.com'

# initialization
client = CompilersClientV3(accessToken, endpoint)
    
    
app = manhas(__name__)
CONNECTION_LIST = []
connection_dict = {}
p_match_dict = {}
done = {}
problem = open('/home/as/Desktop/Code Royal/Wt/Problem.pickle','rb')
problem_list = pickle.load(problem)
problem.close()

input_file = open('/home/as/Desktop/Code Royal/Wt/Input.pickle','rb')
sari_input = pickle.load(input_file)
input_file.close()

output_file = open('/home/as/Desktop/Code Royal/Wt/Output.pickle','rb')
sari_output = pickle.load(output_file)
output_file.close()

language_compiler = {'C++' : 44 , 'Java' : 10 , 'Python3' : 116}

def idgen(code,lan,inp):
	source = code
	compiler = language_compiler[lan]
	input_val = inp
	
	try:
		response = client.submissions.create(code, compiler, input_val)
		z = response['id']
		z = int(z)
		
		#print(z)
		return z
		
	except SphereEngineException as e:
		return -1   
		
def outget(ID):
		#out = client.submissions.get(z,F,T,T,F,F)
		#print(out)
		#time.sleep(20)
		#str_out = client.submissions.getStream(ID, 'output')
		#print(type(ID))
		link = 'http://59e166d8.compilers.sphere-engine.com/api/v3/submissions/'+str(ID)+'/output?access_token=d5549293157f874363dd97c218f73272'
		time.sleep(5)
		#time.sleep(8)
		sou = req.urlopen(link).read()
		soup = bs.BeautifulSoup(sou,'lxml')
		#print(soup.text)
		return soup.text
		#str_out = soup.text()
		#print(str_out)
		#return str_out
		
			 

def problem_get(problem_detail,num):
	
	problem_statment = problem_list['Problem Statement'][num]
	problem_Constraints = problem_list['Constraints'][num]
	problem_input = problem_list['Input'][num]
	problem_input = problem_input[7:]
	problem_output = problem_list['Output'][num]
	problem_sample_input = problem_list['Sample Input'][num]
	problem_sample_output = problem_list['Sample Output'][num]
	
	problem_detail.append(problem_statment)
	problem_detail.append(problem_Constraints)
	problem_detail.append(problem_input)
	problem_detail.append(problem_output)
	problem_detail.append(problem_sample_input)
	problem_detail.append(problem_sample_output)
	
	return

    
@app.route('/')
def start():
	ip = request.environ['REMOTE_ADDR']
	if ip not in CONNECTION_LIST:
		CONNECTION_LIST.append(ip)
	#z = len(CONNECTION_LIST)
	#print(z)
	return render_template("sdl.html") 
	
   
@app.route('/compete',methods=['POST'])
def compete():
	#print("hello")
	z = len(CONNECTION_LIST)
	print(z)
	ip = request.environ['REMOTE_ADDR']
		
	if z % 2 == 0:
		print(CONNECTION_LIST)
		connection_dict[CONNECTION_LIST[z-1]] = CONNECTION_LIST[z-2]
		connection_dict[CONNECTION_LIST[z-2]] = CONNECTION_LIST[z-1]
		#num = random.randint(0,19)
		num = 0
		p_match_dict[CONNECTION_LIST[z-1]] = num
		p_match_dict[CONNECTION_LIST[z-2]] = num
		done[CONNECTION_LIST[z-1]] = 0
		done[CONNECTION_LIST[z-2]] = 0
		
		
	else:
		z = z
		return render_template("sdl.html") 

	print(request.environ['REMOTE_ADDR'])
	n1 = p_match_dict[ip]
	problem_detail = []
	problem_get(problem_detail,n1)
	#print(len(problem_detail))
	return render_template("main.html",problem = problem_detail)

@app.route('/check',methods=['POST','GET'])
def check1():
	ip = request.environ['REMOTE_ADDR']
	n1 = p_match_dict[ip]
	problem_detail = []
	problem_get(problem_detail,n1)
	lan = request.form['language']
	code = request.form['message']
	inp = request.form['input1']
	#print(lan + code + inp)
	id_gen = idgen(code,lan,inp)
	#id_gen = 67853084
	if id_gen != -1 : 
		output = outget(id_gen)
	else :
		output = "Error generated"	
	print(output)	
	#output = '3'
	return render_template("test.html",problem = problem_detail,out = output,code = code,lan = lan,inp = inp)

@app.route('/final_submit',methods=['POST'])
def submit1():
	ip = request.environ['REMOTE_ADDR']
	n1 = p_match_dict[ip]
	#problem_detail = []
	#problem_get(problem_detail,n1)
	lan = request.form['language']
	code = request.form['message']
	
	num = n1
	inp = sari_input[num]
	#print(inp)
	
	#print("yoo")
	
	exp_out = sari_output[num]
	#print(exp_out)
	
	id_gen = idgen(code,lan,inp)
	
	output = ''
	if id_gen != -1 : 
		output = outget(id_gen)
	else :
		output = "Error generated" 
	
	#print(output)
	status = 'Hello'
	color = 'blue'
	if output == exp_out:
		done[ip] = 1
		if done[connection_dict[ip]] == 0:
			status = "U Won"
			color = "green"
		else:
			status = "Your Solution Is Corret But sadly u lose"
			color = "purple"	
	else:
	    status = "Wrong Answer"	
	    color = "red"
	
	print(status)    
	
	return render_template("final.html",status = status,col = color)
	
	
    
if __name__ == "__main__":                  #checking the which file to run 
    app.run(host='0.0.0.0',debug=False,port=9600)
                      
