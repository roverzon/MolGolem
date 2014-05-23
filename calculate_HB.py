#! /usr/bin/env python 
import hbond_analysis_ver3_PBC as hb_PBC

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
                breaking_line =  int(text_stack[0][0]) + 2
                if count % breaking_line == 0:
                	data =  text_stack[2:]
                        total = hb_PBC.operation(data)
                        text_stack[:] = []
                        fp_r.write(   str(total)  + "\n" )

