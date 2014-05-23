#! /usr/bin/env python 
import numpy as np 
import math 

def average(array,total_num):
        total = 0
        for i in np.arange(len(array)):
                total += array[i]
        avg = float(total) / total_num
        return avg

def distance(x,y,z):
	dis = np.sqrt(x**2 + y**2 + z**2)
	return dis 

def determine(vector_stack):
	comp_1 = vector_stack[0][0]*(vector_stack[1][1]*vector_stack[2][2] - vector_stack[1][2]*vector_stack[2][1]) 
	comp_2 = vector_stack[0][1]*(vector_stack[1][0]*vector_stack[2][2] - vector_stack[1][2]*vector_stack[2][0]) 
	comp_3 = vector_stack[0][2]*(vector_stack[1][0]*vector_stack[2][1] - vector_stack[1][1]*vector_stack[2][0]) 
	deter = comp_1 - comp_2 + comp_3 
	return abs(deter)  

def organized_data(data):
	dis_stack = []  
#	print data[72:76] 
	for carbon_e in data[72:76]:
		for i in data[72:76]:
			delta_x =  float(i[1]) - float(carbon_e[1])  
	 		delta_y =  float(i[2]) - float(carbon_e[2])
			delta_z =  float(i[3]) - float(carbon_e[3]) 
			dis = distance(delta_x,delta_y,delta_z)
			dis_stack.append(dis)	
	 
	avg = average(dis_stack,12)   
	return avg      

def operation(data):
#	data = convert_symbol_to_number(data)
	avg_distance =  organized_data(data)
#	num_of_hydrogen_bond = count_hydrogen_bond(data)
#	avg_number_of_hydrogen_bond = average_count(num_of_hydrogen_bond,number_of_molecules)
	return  avg_distance

if __name__ == "__main__":
	frames = 0 
	count = 0 
	number_of_molecules = 8 		
	total = 0 	
	data = [] 
	file_name = "./test_jobs/MPA_8_CO2_4_NVT_400K_BLYP-D_RDF_20K-120K.xyz"
	record_file_name = "tmp.txt"
	fp = open(file_name)
	fp_r = open(record_file_name,"w")
	text_stack = []
	fp_r.write("i , CO2-CO2 Distance(Ang) \n")
	while True:
		file_text = fp.readline()
		if not file_text: 
			break 
		else:
                	text_stack.append(file_text.split('\n')[0].split('      '))
                	count += 1
		#	print text_stack[0] 
			breaking_line =  int(text_stack[0][0]) + 2 
                	if count % breaking_line == 0:
                        	data =  text_stack[2:]
				avg_distance = operation(data)
                        	text_stack[:] = [] 
                        	fp_r.write( str( count / breaking_line ) +  " , " + str(round(avg_distance,4))  + "\n" )
#				break 		 	 

	num = count / breaking_line
#	print total , num  , total*(num**(-1)) 		
