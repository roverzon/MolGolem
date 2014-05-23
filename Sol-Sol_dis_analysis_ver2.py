#! /usr/bin/env python 
import numpy as np 
import math 

mea_8_co2_4_table = [
		[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11],
		[12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22],
		[23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33],
		[34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44],
		[45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55],
		[56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66],
		[67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77],
		[78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 100],
		[88, 94, 95],
		[89, 92, 93],
		[90, 98, 99],
		[91, 96, 97]
	]

mpa_8_co2_4_table = [
		[1,  2,  3,  4,  5,  6,  7,  8,  9,  88,  89,  90,  110, 111],
		[10, 11, 12, 13, 14, 15, 16, 17, 18, 100, 101, 102, 114, 115],
		[19, 20, 21, 22, 23, 24, 25, 26, 27, 85,  86,  87,  112, 113],
		[28, 29, 30, 31, 32, 33, 34, 35, 36, 120, 121, 122, 123, 124],
		[37, 38, 39, 40, 41, 42, 43, 44, 45, 97,  98,  99,  116, 117],
		[46, 47, 48, 49, 50, 51, 52, 53, 54, 91,  92,  93,  108, 109],
		[55, 56, 57, 58, 59, 60, 61, 62, 63, 94,  95,  96,  106, 107],
		[64, 65, 66, 67, 68, 69, 70, 71, 72, 103, 104, 105, 118, 119],
		[73, 79, 80],
		[74, 77, 78],
		[75, 83, 84],
		[76, 81, 82]	
	]

table = mea_8_co2_4_table 

def convert_symbol_to_number(data_array):
	count = 1 
        for d in data_array:
                s = d[0].strip()
                if s  == "H":
                        d[0] =  1.01
                elif s == "C":
                        d[0] = 12.01
                elif s == "N":
                        d[0] = 14.01
                elif s == "O":
                        d[0] = 16.00
                d[1] = float(d[1])
                d[2] = float(d[2])
                d[3] = float(d[3])
		d.append( count )
		count += 1 

        return  data_array

def distance(x,y,z):
	dis = np.sqrt(x**2 + y**2 + z**2)
	return dis 

def indentify_molecules(molecule_table,array):
	data_set = [] 
	molecule_stack  = [] 
	for m_id in range(len(molecule_table)):
		for elements in array:	
			e_id = elements[-1] 
			if e_id in molecule_table[m_id]:
				molecule_stack.append(elements[:-1])  
		data_set.append(molecule_stack)
		molecule_stack = []
	return data_set  

def sum_operation(array,total_mass):
	x_sum = 0 
	y_sum = 0 
	z_sum = 0 
	for i in np.arange(len(array)):
		x_sum  +=  array[i][0] 
		y_sum  +=  array[i][1]
		z_sum  +=  array[i][2]
	return  [ x_sum/total_mass , y_sum/total_mass , z_sum/total_mass ] 

def mass_center(molecule_set):
	count = 1 
	mass_record = [] 
	center_of_mass_stack = [] 
	for molecule in molecule_set: 
		test = [] 
		total_mass = 0 
		for atoms in molecule:
			tmp = [ 0, 0, 0] 
			tmp[0],tmp[1],tmp[2] = atoms[0]*atoms[1],atoms[0]*atoms[2],atoms[0]*atoms[3]
			total_mass += atoms[0] 
			test.append(tmp)
		mass_record.append(total_mass)
		center_of_mass = sum_operation( test , total_mass )  
		new_center_of_mass = [center_of_mass,round(total_mass,2)]
		center_of_mass_stack.append( center_of_mass) 
	return  center_of_mass_stack  

def count_dis(center_of_mass):
	distance_stack = []
	for i in  range(8):
		total = 0 
		count = 0 
		for  j in range(4):
			 del_x = center_of_mass[i][0] - center_of_mass[8 + j][0] 
                         del_y = center_of_mass[i][1] - center_of_mass[8 + j][1]
                         del_z = center_of_mass[i][2] - center_of_mass[8 + j][2]
			 dis = distance(del_x,del_y,del_z)
			 total +=  dis 
			 count += 1 
		average = total / count 
		distance_stack.append(round(average,3))
	return  distance_stack 

def operation(data):
	data = convert_symbol_to_number(data)
	molecule_set = indentify_molecules(table,data)
	center_of_mass = mass_center(molecule_set)	
	distances = count_dis(center_of_mass)	 
	return  distances

if __name__ == "__main__":
	frames = 0 
	count = 0 
	number_of_molecules = 8 		
	total = 0 	
	data = [] 
	file_name = "./test_jobs/MEA_8_CO2_4_NVT_400K_BLYP-D_RDF_20K-120K.xyz"
	record_file_name = "MEA_rada_distance.txt"
	fp = open(file_name)
	fp_r = open(record_file_name,"w")
	text_stack = []
	fp_r.write("( MEA 1 )  ( MEA 2 )  ( MEA 3 )  ( MEA 4 )  ( MEA 5 )  ( MEA 6 )  ( MEA 7 )  ( MEA 8 )\n")
	while True:
		file_text = fp.readline()
		if not file_text: 
			break 
		else:
                	text_stack.append(file_text.split('\n')[0].split('      '))
                	count += 1
			breaking_line =  int(text_stack[0][0]) + 2 
                	if count % breaking_line == 0:
                        	data =  text_stack[2:]
				avg_dis = operation(data)
                        	text_stack[:] = []
				fp_r.write( " %f   %f   %f   %f   %f   %f   %f   %f \n" %( avg_dis[0] , avg_dis[1] , avg_dis[2], avg_dis[3], avg_dis[4], avg_dis[5], avg_dis[6], avg_dis[7]) )
	
				 
