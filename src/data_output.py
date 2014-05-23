#!/usr/bin/python 
import numpy as np 
import matplotlib.pyplot as plt 
from xlwt import *

def data_intergrat(file_names,f_stack,selected_data):
    data = []
    number_of_file = len(file_names)
    dim_detail = len(f_stack)
    dim_selected_data = len(selected_data)
    try:
        if number_of_file == dim_detail & dim_detail == dim_selected_data:
            for f_id in range(number_of_file):
                    tmp = (file_names[f_id] , selected_data[f_id],  f_stack[f_id]) 
                    data.append(tmp)
        return data 
    except:
        print "Error" 

def output_wanted_data_in_text(job_name,job_text,wanted_job_index,top_peaks):
    job_name = job_name.split('.')[0]
    stored_formate = '.txt'
    stored_job_fullname = job_name + '_Data_Analysis_Date' + stored_formate
    wp = open(stored_job_fullname, "w")
    wp.write("The No. of peak you want: \n")
    for i in np.arange(len(wanted_job_index)):
            wp.write(str(wanted_job_index[i]) + ' ')
    wp.write('\n')
    wp.write('Top Peaks in packets:\n')
    for tp in np.arange(len(top_peaks)):
            wp.write(str(top_peaks[tp]) + ' ')
    wp.write('\n') 
    wp.write("==========================================================================================================================================================================")
    wp.write('\n')
    wp.write('The Detail of Peaks:\n')
    wp.write('\n')
    for i in wanted_job_index:
        wp.write( str([i-1]) + '\n' ) 
    wp.write('\n')
    wp.close()

def excel_sheet( output_number, mrg_logic, data):
   filted_data = []
   dim_data = len(data)
   book = Workbook()
   for f_id in range(dim_data):
        file_total_name = data[f_id][0]
        job_name = file_total_name.split('.')[0] 
        sheet1 = book.add_sheet(job_name)
        head = ['Top Peaks', 'Peaks Candidates', 'Details']
        al = Alignment()
        al.horz = Alignment.HORZ_CENTER
        al.vert = Alignment.VERT_CENTER
        borders = Borders()
        borders.bottom = Borders.THICK
        style = XFStyle()
        style.alignment = al
        style.borders = borders
        row0 = sheet1.row(0)
        for i , h in enumerate(head):
            row0.write( i, h, style=style)

        for i , value in enumerate(data[f_id][1][1]):
            sheet1.write( i + 1, 0 , value )

        for i , value in enumerate(data[f_id][1][0]):
            sheet1.write( i + 1, 1 , value )

        for t in range(len(data[f_id][2])):
            if t + 1 in data[f_id][1][0]:
                filted_data.append(data[f_id][2][t])

        for i , t  in enumerate(filted_data):
            # if i + 1 in data[f_id][1][0]:
            # sheet1.write(i+1, 2 , i + 1)
            for j, e in enumerate(t):
                sheet1.write( i + 1 , j + 2 , e)
                sheet1.col( j + 2 ).width = 35000 
        for c in range(2):
            sheet1.col(c).width = 4500
        sheet1.row(0).height_mismatch = 1 
        sheet1.row(0).height = 1000 
        filted_data[:] = []
        book.save("trial.xls")


def image(data):
    x = []
    y = []
    dim = len(data)
    for f in range(dim):
        for x_value , y_value in data[f]:
            x.append(x_value)
            y.append(y_value)
        plt.plot(x,y)
        file_save_name = 'trial_pict' + str(f) + '.png'
        plt.savefig(file_save_name)
        x[:] = []
        y[:] = []
        plt.clf()

