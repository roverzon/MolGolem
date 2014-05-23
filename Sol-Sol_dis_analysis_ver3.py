#! /usr/bin/env python 
import numpy as np 
import math 

label = [ 1, 12, 23, 34, 45, 56, 67, 78, 88, 92]
		
def distance(x,y,z):
        dis = np.sqrt(x**2 + y**2 + z**2)
        return dis

def radial_dis(data):
	
	dis_stack = []

	for i in range(len(data)-2):
                         del_x = float(data[i][1]) - float(data[-1][1])
                         del_y = float(data[i][2]) - float(data[-1][2])
                         del_z = float(data[i][3]) - float(data[-1][3]) 
 			 dis = distance( del_x , del_y, del_z )  
		 	 dis_stack.append(round(dis,3))

        for i in range(len(data)-2):
                         del_x = float(data[i][1]) - float(data[-2][1])
                         del_y = float(data[i][2]) - float(data[-2][2])
                         del_z = float(data[i][3]) - float(data[-2][3])
                         dis = distance( del_x , del_y, del_z )
                         dis_stack.append(round(dis,3))

	return  dis_stack    

def filter(data):	
	selected_data = []
	for i , element_info in enumerate(data):
		if i + 1 in label:
			selected_data.append(element_info)

	return  selected_data 
def operation(data):
	selected_data = filter(data)
	distance_info = radial_dis(selected_data)	
	return distance_info 


if __name__ == "__main__":
	frames = 0 
	count = 0 
	number_of_molecules = 8 		
	total = 0 	
	data = [] 
	file_name = "./test_jobs/MEA_8_CO2_2_NVT_BLYP-D_TotalTrajectory.xyz"
	record_file_name = "MEA_8_CO2_2_N-C_trace.txt"
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
                        	text_stack[:] = []
				for i in range(len(dis_info)):
					fp_r.write( " %f  " %( dis_info[i]))
				fp_r.write("\n")
