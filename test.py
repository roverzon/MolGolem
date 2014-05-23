#!/usr/bin/env python
import subprocess 
import re 

file_name_2 = 'MEA_CO2_MP2_CounterPoise_AQZ.log' 

e2_energy_stack_2 = []

hf_text_2 = subprocess.check_output(['grep', 'RHF', file_name_2])
e2_text_2 = subprocess.check_output(['grep', 'EUM', file_name_2])

regex_hf_2 = 'E\(RHF\) = (.*?) A.U.'
regex_e2_2 = 'E2 =   (.*?) EUMP2'

pattern_hf_2 = re.compile(regex_hf_2)
hf_energy_2 = re.findall(pattern_hf_2,hf_text_2)

pattern_e2_2 = re.compile(regex_e2_2)
e2_energy_2 = re.findall(pattern_e2_2,e2_text_2)

for i in e2_energy_2: 
	new_i = i.split('D')
#	if new_i[1] == '+01': 
#		exp = 1 
	up_i = float(new_i[0])*10**(int(new_i[1][-1])) 
	e2_energy_stack_2.append(up_i)	

binding_energy_hf_2 = 627.5*( float(hf_energy_2[0]) - float(hf_energy_2[1]) - float(hf_energy_2[2])) 
binding_energy_e2_2 = 627.5*( e2_energy_stack_2[0] - e2_energy_stack_2[1] - e2_energy_stack_2[2] )
binding_energy_2 = binding_energy_hf_2 + binding_energy_e2_2 


print binding_energy_hf_2 
print binding_energy_e2_2  
print binding_energy_2 

#print hf_energy 
#print e2_energy 
#print e2_energy_stack 

file_name_1 = 'MEA_CO2_MP2_CounterPoise_ATZ.log'

e2_energy_stack_1 = []

hf_text_1 = subprocess.check_output(['grep', 'RHF', file_name_1])
e2_text_1 = subprocess.check_output(['grep', 'EUM', file_name_1])

regex_hf_1 = 'E\(RHF\) = (.*?) A.U.'
regex_e2_1 = 'E2 =   (.*?) EUMP2'

pattern_hf_1 = re.compile(regex_hf_1)
hf_energy_1 = re.findall(pattern_hf_1,hf_text_1)

pattern_e2_1 = re.compile(regex_e2_1)
e2_energy_1 = re.findall(pattern_e2_1,e2_text_1)

for i in e2_energy_1:
       new_i = i.split('D')
       up_i = float(new_i[0])*10**(int(new_i[1][-1]))
       e2_energy_stack_1.append(up_i)

binding_energy_hf_1 = 627.5*( float(hf_energy_1[0]) - float(hf_energy_1[1]) - float(hf_energy_1[2] ) )
binding_energy_e2_1 = 627.5*( e2_energy_stack_1[0] - e2_energy_stack_1[1] - e2_energy_stack_1[2] )
binding_energy_1 = binding_energy_hf_1 + binding_energy_e2_1

print binding_energy_hf_1
print binding_energy_e2_1
print binding_energy_1

#print hf_energy_1
#print e2_energy_1
#print e2_energy_stack_1

extraplation_energy = binding_energy_hf_2 + (binding_energy_e2_2*(4**3)-binding_energy_e2_1*(3**3))/((4**3)-(3**3))
print round(extraplation_energy,2) 


