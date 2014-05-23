#! /usr/bin/env python 
import numpy as np 
import math 

def convert_symbol_to_number(data_array):
	record_type = np.dtype({
        'names':['atom_number','x_coord','y_coord','z_coord'],
        'formats':['i','Float64','Float64','Float64']}, align = True)
	tmp = [] 
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
	        tmp.append( tuple(d) )
        data_array = np.asarray(tmp, dtype=record_type)
        return  data_array

def distance(x,y,z):
	dis = np.sqrt(x**2 + y**2 + z**2)
	return dis 

def organized_data(data):
	packet = [ ] 
	dim = len(data)
	for di in np.arange(dim):
		 if data[di][0] > 6:
			test = [] 
			test.append(data[di])
			for i in np.arange(dim):
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
	    
	return packet   

def vector_length(vector):
	total = 0 
	for i in vector:
		total += i**2 
	length = np.sqrt(total)
	return length 

def inner_product(vect_1,vect_2):
	total = 0 
	dim = len(vect_1)
	for i in np.arange(dim):
		total += vect_1[i] * vect_2[i] 
	return total 

def get_angle(vect_1_len, vect_2_len, dot_product):
	cosine = dot_product * ( (vect_1_len*vect_2_len)**(-1))
	angle_in_radian = math.acos(cosine)
	angle_in_degree = math.degrees(angle_in_radian)
	return angle_in_degree 

def count_hydrogen_bond(data):
	count = 0 
        orient_vector = [0.0, 0.0, 0.0]
	dim = len(data) 
	for di in np.arange(dim):
		for i in np.arange(dim):
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
							count += 1 
	return  count 
							
					
def average_count(num_of_hydrogen_bond,number_of_molecules):
	num = num_of_hydrogen_bond * ( number_of_molecules **(-1) ) 
	return num

def operation(data):
	data = convert_symbol_to_number(data)
	data = organized_data(data)
	num_of_hydrogen_bond = count_hydrogen_bond(data)
#	avg_number_of_hydrogen_bond = average_count(num_of_hydrogen_bond,number_of_molecules)
	return  num_of_hydrogen_bond

if __name__ == "__main__":
	count = 0 
	number_of_molecules = 8 		
	total = 0 	
	data = [] 
	file_name = "./test_jobs/MPA_8_CO2_1_NVT_BLYP-D_400K-pos-1.xyz"
	fp = open(file_name)
	text_stack = []
	while True:
		file_text = fp.readline()
		if not file_text: 
			break 
		else:
                	text_stack.append(file_text.split('\n')[0].split('       '))
                	count += 1
			breaking_line =  int(text_stack[0][0]) + 2 
                	if count % breaking_line == 0:
                        	data =  text_stack[2:]
				total += operation(data)
                        	text_stack[:] = []

	num = count / breaking_line
#	print total , num  , total*(num**(-1)) 		
