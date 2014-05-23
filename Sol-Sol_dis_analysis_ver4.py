#! /usr/bin/env python 
import numpy as np 
import math 

label = [ 88, 89, 90, 92, 93, 94]
O_CHARGE =  0.504896 
O_CHARGE =  0.504896
C_CHARGE =  1.009792

def distance(a,b):
	diff = np.asarray(a[1:]) - np.asarray(b[1:])
        return np.sqrt(diff[0]**2 + diff[1]**2 + diff[2]**2)

def vector(a,b):
	new_a =   np.asarray(a)
	new_b =   np.asarray(b) 
	vector =  new_a - new_b   
	return  vector[1:]  

def sum_dipole(dipole_vector):
	x_part = 0 
	y_part = 0 
	z_part = 0 
	for vector in dipole_vector:
		x_part += vector[0] 
		y_part += vector[1] 
		z_part += vector[2] 
	return np.array( [x_part , y_part , z_part] )

def dipole_moment_value(vector):
		return  np.sqrt(vector[0]**2 + vector[1]**2 + vector[2]**2)

def dipole_moment(data):
	total_info = []
	for element in data:
		dipole_moment = []
		for i in element[:-1]:
			dipole_moment.append( vector(i,element[-1]) )  
		Total_dipole_moment = sum_dipole(dipole_moment)
#		print Total_dipole_moment 
		dipole_value = dipole_moment_value(Total_dipole_moment)
		total_info.append( round(dipole_value,3) )
	dis = distance(data[0][-1] , data[1][-1])   
	total_info.append( round(dis,3) ) 
	return total_info

def filter(data):	
	selected_data = []
	tmp_data = [] 
	new_tmp  = [] 
	new_data = []
 
	for i , element_info in enumerate(data):
		if i + 1 in label:
			tmp_data.append(element_info)

	for element_info in tmp_data:
		if element_info[0]   == '  C':
			element_info[0] = 6 
		elif element_info[0] == '  O':
			element_info[0] = 8
		
		element_info[1] = float(element_info[1])
		element_info[2] = float(element_info[2])
		element_info[3] = float(element_info[3])
		
	molecule1 = tmp_data[:3]
	molecule2 = tmp_data[3:]
	for mole in [molecule1, molecule2]:
		selected_data.append(sorted(mole,reverse=True))
	
	return  selected_data 
def operation(data):
	selected_data = filter(data)
	total_info  = dipole_moment(selected_data)	
	return total_info


if __name__ == "__main__":
	frames = 0 
	count = 0 
	number_of_molecules = 8 		
	total = 0 	
	data = [] 
	file_name = "./test_jobs/MEA_8_CO2_2_NVT_BLYP-D_TotalTrajectory.xyz"
	record_file_name = "test.txt"
	fp = open(file_name)
	fp_r = open(record_file_name,"w")
	text_stack = []
	while True:
		file_text = fp.readline()
		if not file_text: 
			break 
		else:
                	text_stack.append(file_text.split('\n')[0].split('     '))
                	count += 1
			breaking_line =  int(text_stack[0][1]) + 2 
                	if count % breaking_line == 0:
                        	data =  text_stack[2:]
				dis_info = operation(data)
#				print dis_info 
                        	text_stack[:] = []
				for i in range(len(dis_info)):
					fp_r.write( " %f  " %( dis_info[i]))
				fp_r.write("\n")
			 
