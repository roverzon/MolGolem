#!/usr/bin/python
import numpy as np
import math 
import time
from src import mtool

packet_set = []
def diff_matrix(a,b,c):
    for i in np.arange(len(a)):
        for j in np.arange(len(a)):
            c[i,j] = a[i] - b[j]
    return c 
            
def packet_data(c, num_compar,no_frame,wave_length):
    info_array = []
    breaking_point = []
    judge = True 
    for i in np.arange(len(c)):
        if i <= num_compar:
            for w in np.arange(len(c[i,0:i+num_compar+1])):
                if c[i, w] >= 0.:
                    if w!=num_compar:
                        packet_set.append(i+1)
                        break 
                elif w == len(c[i,0:i+num_compar+1])-1:

                    packet_set.append(0)

        elif num_compar < i < len(c)-num_compar:  
            for w in np.arange(len(c[i,i-num_compar:i+num_compar+1])):
                if c[i, i-num_compar+w] >=0.0 :
                    if w!=num_compar:
                        packet_set.append(i+1)
                        break 
                elif w == len(c[i,i-num_compar:i+num_compar+1])-1:
                    packet_set.append(0)
        else:
            for w in np.arange(len(c[i,i-num_compar:len(c)])):
                if c[i, i-num_compar+w+1] >=0.0 :

                    if w!=num_compar:
                        packet_set.append(i+1)
                        break 
                elif w == len(c[i,i-num_compar:len(c)])-1:
                    packet_set.append(0)
                    
    info_array.append(data_pair(wave_length, no_frame))
    for i in np.arange(len(no_frame)):
        diff = no_frame[i] - packet_set[i]
        if diff != 0:
            breaking_point.append(diff)
    return ( breaking_point , info_array ) 
 

def data_pair(list_1,list_2):
    list_3 = []
    
    if len(list_1) != len(list_2):
        print "Two dimensions of list is different"
    else: 
        for i in np.arange(len(list_1)):
            list_3.append([list_1[i] ,list_2[i]])
    return list_3
 
def freq_cal(list_1 , dim ):
    num = []
    index = []
    begining = [0]
    final = [dim]
    
    list_1 = begining + list_1 + final
    for d in np.arange(len(list_1)):
        if d < len(list_1)-1:
            num.append(list_1[d+1] - list_1[d])
    index_array = np.zeros(len(num))

    for fp in np.arange(len(num)):
        index_array[fp] = sum(num[:fp+1])
    for p in index_array:
        index.append(p)
    index = [0] + index
    for j in np.arange(len(index)):
        index[j] = int(index[j])
    
    return index

def get_number_of_wanted_peaks(index_array,processed_data,data_text,peak_range,num_peaks=3):
    top_peaks  = []
    no_stake = []
    test = []
    for ai in np.arange(len(index_array)-1):
        test = processed_data[index_array[ai]:index_array[ai+1]]
        list_stake =  sorted(test)[-1*(num_peaks+1):]
        for ls in np.arange(len(list_stake)):
           no_stake.append(list_stake[ls][1])
        top_peaks.append(list_stake[-1:][0][1])
        
    sorted_no_stake = sorted(no_stake)
    return (sorted_no_stake , top_peaks)

def peak_brodening(wave_length, osc):
    wave_number = np.asarray(wave_length)
    vaiance = 300
    FWHM = 60
    sigma = np.sqrt(vaiance)
    gamma = FWHM/2.
    x = np.linspace(200,800,500)
    stack = []
    for w in range(len(wave_number)):
         dist = mtool.lorenpdf(x,wave_number[w], osc[w] , gamma)
         stack.append( dist/(1.44*10**(-10)) )
    y = []
    for j in range(500):
        y_value = 0 
        for i in np.arange(len(stack)):
            y_value += stack[i][j] 
        y.append(y_value)
    uv = zip(x,y)
    return uv 


def peak_selecting( file_stake):
    num_compar = 5
    peak_range = [300, 500]
    data = [] 

    for f in file_stake:
        no_frame = f[0]
        wave_length = f[1]
        osc_np = f[2]
        matrix = np.zeros((len(osc_np),len(osc_np)),np.float)
        matrix = diff_matrix(osc_np,osc_np,matrix)
        breaking_point , info_array = packet_data(matrix,num_compar,no_frame,wave_length)
        pair_list = data_pair(osc_np,no_frame)
        accumulated_index  = freq_cal(breaking_point,len(osc_np))
        data_text = info_array[0]
        wanted_number_index , top_peaks = get_number_of_wanted_peaks(accumulated_index,pair_list,data_text,peak_range,num_peaks=3)
        tmp =  ( wanted_number_index , top_peaks )
        data.append(tmp)
    return data 

def uv_spectrum(file_stack):
    stack = []
    for f in file_stack:
        wave_length_list = f[1]
        osc = f[2]
        uv = peak_brodening(wave_length_list, osc)
        stack.append(uv)
    return stack 


if __name__ == '__main__':
    start_1 = time.time()
    file_open = open('file_stake.txt')
    file_read = file_open.read()
    job_stake = file_read.split('\n')

    for js in job_stake:
    ##======================================================================
        info_array = []
        no_frame = []
        wave_length = []
        osc = [] 
        num = []
        packet_set = []
        top_peaks = [] 
        num_compar = 5
        peak_range = [300, 500]
        peak_critieria = 0.01
    ##======================================================================    
        print js
        
        fo = open(js,'r')
        file_head = fo.readline()
        file_head2 = fo.readline()
        file_text = fo.read()
        num_line = file_text.count('\n')
        text = file_text.split('\n')
        fo.close()
        
        start_split = time.time()
        for i in np.arange(len(text)-1):
            no_frame.append(int(file_text.split('\n')[i].split('\t')[0]))
            wave_length.append(float(file_text.split('\n')[i].split('\t')[2]))
            osc.append(float(file_text.split('\n')[i].split('\t')[3]))
        end_split = time.time()

        
        
        osc_np = np.asarray(osc,dtype=np.float)
        matrix = np.zeros((len(osc_np),len(osc_np)),np.float)
        
        start_2 = time.time()
        matrix = diff_matrix(osc_np,osc_np,matrix)
        end_2 = time.time() 
        
        start_3 = time.time()
        breaking_point = packet_data(matrix,num_compar,no_frame,wave_length,info_array)
        end_3 = time.time() 

        start_4 = time.time()
        pair_list = data_pair(osc,no_frame)
        end_4 = time.time()

        
        start_5 = time.time()
        accumulated_index  = freq_cal(num,breaking_point,len(osc_np))
        end_5 = time.time()

        data_text = info_array[0]
        
        abs_intensity = uv_spectrum(wave_length)
        
        wanted_number_index = get_number_of_wanted_peaks(accumulated_index,pair_list,top_peaks,data_text,peak_range,num_peaks=3)

        output_wanted_data(js,text,wanted_number_index,top_peaks)

        no_frame[:] = []
        wave_length[:] = []
        osc[:] = [] 
        num[:] = []
        packet_set[:] = []
        top_peaks[:] = []


