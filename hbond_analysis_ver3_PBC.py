#! /usr/bin/env python 
import numpy as np 
import math 
import threading 

PBC_x = 11.86
PBC_y = 9.88
PBC_z = 9.16

def convert_symbol_to_number(data_array):
        for d in data_array:
                s = d[0].strip()
                if s  == "H":
                        d[0] = 1
                elif s == "C":
                        d[0] = 6
                elif s == "N":
                        d[0] = 7
                elif s == "O":
                        d[0] = 8
                d[1] = float(d[1])
                d[2] = float(d[2])
                d[3] = float(d[3])
        return  data_array

def distance(x,y,z):
	dis = np.sqrt(x**2 + y**2 + z**2)
	return dis 

def organized_data(data):
	packet = [ ] 
	dim = len(data)
	for di in range(dim):
		 if data[di][0] > 6:
			test = [] 
			test.append(data[di])
			for i in range(dim):
				vector = [0.0,0.0,0.0] 
				if  data[i][0] ==  1 :
                                        delta_x =  data[di][1] -  data[i][1] 
					delta_y =  data[di][2] -  data[i][2]
					delta_z =  data[di][3] -  data[i][3] 		
					dis = distance(delta_x,delta_y,delta_z)
					if dis < 1.2:
						vector[0] , vector[1], vector[2] = delta_x, delta_y, delta_z   	
						test.append(vector)
				else:
					continue
			 
		 	packet.append(test)
    	
	return ( packet , len(packet)/27 )

def vector_length(vector):
	total = 0 
	for i in vector:
		total += i**2 
	length = np.sqrt(total)
	return length 

def inner_product(vect_1,vect_2):
	total = 0 
	dim = len(vect_1)
	for i in range(dim):
		total += vect_1[i] * vect_2[i] 
	return total 

def get_angle(vect_1_len, vect_2_len, dot_product):
	cosine = dot_product * ( (vect_1_len*vect_2_len)**(-1))
	angle_in_radian = math.acos(cosine)
	angle_in_degree = math.degrees(angle_in_radian)
	return angle_in_degree 

def count_hydrogen_bond(data , unit_set): 
	state = [0.0, 0.0, 0.0, 0.0]
        orient_vector = [0.0, 0.0, 0.0]
	dim = len(data) 
	counter = 0
	for di in range(dim):
		for i in range(dim):
			if di == i:
				continue 
			else:
				delta_x = data[di][0][1] -  data[i][0][1] 
                                delta_y = data[di][0][2] -  data[i][0][2]
                                delta_z = data[di][0][3] -  data[i][0][3] 
				dis = distance(delta_x, delta_y, delta_z)
				if dis < 3.5:
                                	orient_vector[0], orient_vector[1], orient_vector[2] = delta_x, delta_y, delta_z
					orient_vector_length = vector_length(orient_vector)
					for h_vector in  data[di][1:]:
						dot_product = inner_product(orient_vector,h_vector)
                                                orient_vector_length = vector_length(orient_vector)
						h_vector_length = vector_length(h_vector)
						angle = get_angle(orient_vector_length,h_vector_length,dot_product)
						if angle < 15:
                                                        if   (data[di][0][0] == 7) & (data[i][0][0] == 8):
                                                                state[0] += 1
                                                        elif (data[di][0][0] == 8) & (data[i][0][0] == 7):
                                                                state[1] += 1
                                                        elif (data[di][0][0] == 8) & (data[i][0][0] == 8):
                                                                state[2] += 1
                                                        elif (data[di][0][0] == 7) & (data[i][0][0] == 7):
                                                                state[3] += 1
							
		counter += 1 
		if counter == 24:
			break 
	return  state 
								
def average_count(num_of_hydrogen_bond,number_of_molecules):
	num = num_of_hydrogen_bond * ( number_of_molecules **(-1) ) 
	return num

def pbc_expansion(data, cond_x, cond_y, cond_z):
	real = []
	tmp = [] 
   	geom_stack = []
    	pbc_model = []
	PBC  = [ PBC_x, PBC_y, PBC_z]
    	
	for i in range(len(PBC)):
        	for j in range(len(PBC)):
            		for k in range(len(PBC)):
                		for line in data:
                    			new_x = float(line[1]) + (i-1.) * PBC[0]
                    			new_y = float(line[2]) + (j-1.) * PBC[1]
                    			new_z = float(line[3]) + (k-1.) * PBC[2]
                    			if i  == 1 & j == 1& k == 1:
                        			geom_stack.append([line[0],new_x, new_y, new_z])
                    			else:
                        			pbc_model.append([line[0],new_x, new_y, new_z])
	

	new_geom = geom_stack + pbc_model
	return new_geom

def pbc_organized_data(data):
	total_data_set = []
	count = 0 
	for data_set in data:
		new_data_set = organized_data(data_set)		 
		total_data_set.append(new_data_set)

	return total_data_set
 	
def operation(data):
	data = convert_symbol_to_number(data)
	pbc_data = pbc_expansion(data, PBC_x, PBC_y, PBC_z)
	data , unit_lines = organized_data(pbc_data)
	num_of_hydrogen_bond = count_hydrogen_bond(data , unit_lines)
	return  num_of_hydrogen_bond

def output_file( text ):
	fp_write.write( text  + "\n")
	fp_write.close()

if __name__ == "__main__":
	frames = 0 
	count = 0 
	number_of_molecules = 8 		
	total = 0 	
	data = [] 
	file_name = "./test_jobs/MEA_8_CO2_4_NVT_400K_BLYP-D_RDF_20K-120K.xyz"
	record_file_name = "text.xyz"
	fp = open(file_name)
	fp_r = open(record_file_name,"w")
	text_stack = []
	fp_r.write("Hello World")
	while True:
		file_text = fp.readline()
		if not file_text: 
			break 
		else:
                	text_stack.append(file_text.split('\n')[0].split('      '))
                	count += 1
#		#	print text_stack[0][1] 
			breaking_line =  int(text_stack[0][0]) + 2 
                	if count % breaking_line == 0:
                        	data =  text_stack[2:]
				total = operation(data)
#				output_file( str(total) )
				print total 
                        	text_stack[:] = []
                     #   	fp_r.write(  str(total)  + "\n" )
				 
	fp_r.close()						 
