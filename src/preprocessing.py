import numpy as np
import re 

def GauSun_file_split( file_stack ):
    no_frame = []
    wave_length = []
    osc = [] 
    detail = [] 
    detail_stack = []
    text_stack = []
    stack = []
    for file_ in file_stack:
        fp = open(file_)
        heading  = fp.readline() 
        info = fp.readline() 
        text = fp.read()
        new_text =  text.split('\n')
        for t in range(len(new_text)):
            if not new_text[t]:
                new_text.pop(t)
        
        text_stack.append(new_text)
        fp.close()

    for fp in text_stack:
        # stack = [ file 1 content, file 2 content, ....]
        for i in fp:
             #split a row text by '\n' '\t', Number is 0 column 
             no_frame.append(i.split('\n')[0].split('\t')[0])
             #split a row text by '\n' '\t', Wave Length is 2 column 
             wave_length.append(i.split('\n')[0].split('\t')[2])
             #split a row text by '\n' '\t', Oscillation Number is 3 column 
             osc.append(i.split('\n')[0].split('\t')[3])
             # detail information of electron exciting 
             detail.append(i.split('\n')[0].split('\t')[5:])
        # convert to np array 
        no_len   = np.asarray(no_frame,dtype=np.int)
        wave_len = np.asarray(wave_length, dtype=np.float)
        osc_np   = np.asarray(osc,dtype=np.float)

        # list of Number, list of wave length, list of oscilation
        # output a tuple 
        tmp = (no_len , wave_len , osc_np)
        # Use a list to collect fracterize
        # ["A file content "(list of Number,list of wave length,list of oscilation ) ...]
        stack.append(tmp)
        detail_stack.append(tuple(detail))
        # clean list
        no_frame[:] = []
        wave_length[:] = []
        osc[:] = [] 
        detail[:] = []
    return stack , detail_stack 


def Gaussian_file_split(file_stack):

    info_regex = 'eV\s\s(.*?) nm  f=(.*?)\s'
    electron_regex = '\s(.*?) alpha electrons      (.*?) beta electrons\s'

    info_pattern = re.compile(info_regex)
    e_pattern = re.compile(electron_regex)

    transistion_detail  = []
    count_stack = []
    electron_detail = []
    text_stack = []

    for file_ in file_stack:
        print file_
        tmp_data = []
        tmp_count = [] 
        count   = 0 
        f_count = 0 
        transi_detail = []
        text = []
        fp_1 = open(file_)
        while True:
            text_1 = fp_1.readline()
            if not text_1:
                break
            else:
                e_result = re.findall(e_pattern,text_1)
                info_result = re.findall(info_pattern,text_1)
                if info_result:
                    tmp_data.append(info_result)
                    tmp_count.append(count)
                    f_count += 1 
                text.append(text_1)
            count +=1

        transistion_detail.append(tuple(tmp_data))
        count_stack.append(tuple(tmp_count))
        electron_detail.append(tuple(e_result))
        text_stack.append(tuple(text))

        tmp_data[:]      = []
        tmp_count[:]     = []
        transi_detail[:] = []


    print count_stack
        
