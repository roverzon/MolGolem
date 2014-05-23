#!/usr/bin/env python
import os 
import subprocess 

keyword_list = [ 'counterpoise=2',  ]
comment = 'functionals Test'
basis_set = 'aug-cc-pVTZ'
Geoms_List = ['Geom' ]
functionals_List=['MP2','B3LYPD', 'BLYPD', 'wB97','wB97X', 'wB97XD', 'M062X', 'M06HF']
nodes = '1'
cores = '8'


for g in Geoms_List:	
	if   g == 'TS1':
		keyword_list[0] = 'freq'
	elif g == 'TS2':
		keyword_list[0] == 'freq'
	else: 
		keyword_list[0] == 'opt'

	for f in functionals_List: 
		file_name =  'MEA_TriPath_' + g + '_' + f + '_' + keyword_list[0] + '_PCM-EtOH'
		Input_file_name = file_name + '.com' 

		Coord_read_file = g + '.xyz'
	#	print Input_file_name 
		file = subprocess.check_output( ['touch', Input_file_name] )
		
   	       
		file = open(Input_file_name,"wb+")
		file.write( '%chk=' + file_name + '\n' )
		file.write( '%mem=16GB' + '\n' )
		file.write( '%nprocshared=8' + '\n' )

		for k in keyword_list:
			if   f == 'B3LYPD':
				keywords = ' '.join(keyword_list) + ' EmpericalDispersion=GD2 '
			elif f == 'BLYPD': 
                                keywords = ' '.join(keyword_list) + ' EmpericalDispersion=GD2 '
			else:
				keywords = ' '.join(keyword_list)
		file.write( '#P ' + f + '/' + basis_set + '\t' + keywords  + '\n' )
               	file.write( '\n' )
               	file.write( comment + '\n' )
               	file.write( '\n' )
               	file.write( '0 1' + '\n' )
               	Coord = subprocess.check_output( ['less', Coord_read_file] )
      		file.write( Coord )
		file.close()


for g in Geoms_List:
	if   g == 'TS1':
             keyword_list[0] = 'freq'
	elif g == 'TS2':
	     keyword_list[0] = 'freq'	
        else:
             keyword_list[0] = 'opt'

	for f in functionals_List:
                file_name =  'MEA_TriPath_' + g + '_' + f + '_' + keyword_list[0] + '_PCM-EtOH'
                Qsub_file_name = file_name + '.qsub'
		file = subprocess.check_output(['touch', Qsub_file_name])
		file = open(Qsub_file_name, "wb+") 
		file.write('#!/bin/csh' +  '\n' + 
			   '#PBS -N ' + file_name + '\n' + 
			   '#PBS -o $PBS_JOBNAME.job.out' +'\n'+ 
			   '#PBS -e $PBS_JOBNAME.job.err' + '\n' + 
			   '#PBS -q workq' +'\n' + 
			   '#PBS -l nodes='+ nodes + ':ppn=' + cores + '\n')
		file.write(' ' + '\n')		
		file.write('module load intel_poe' + '\n')
		file.write(' ' + '\n')
		file.write('echo \'=======================================================\'' + '\n' +
			   'echo "Working directory is /lustre/lwork/mktsai/scratch/00_$PBS_JOBNAME"' + '\n'
			   'echo "Starting on `hostname` at `date`"' + '\n' )
		file.write(' ' + '\n')
		file.write('cd $PBS_O_WORKDIR' + '\n' +
			   'set path = ( /home/software $path )' + '\n' +
			   'setenv g09root "/home/software"' + '\n' + 
			   'setenv GAUSS_SCRDIR "/tmp" ' + '\n' + 
			   'alias g09exe \'$g09root/g09/g09\'' + '\n' + 
			   'source $g09root/g09/bsd/g09.login')
		file.write(' '+'\n')
		file.write('rm -fr $GAUSS_SCRDIR/*' + '\n'
			   'mkdir $GAUSS_SCRDIR/00_$PBS_JOBNAME' + '\n' + 
			   'cd $GAUSS_SCRDIR/00_$PBS_JOBNAME' + '\n' + 
			   'cp $PBS_O_WORKDIR/$PBS_JOBNAME.com . ' + '\n' + 
			   'cp $PBS_O_WORKDIR/$PBS_JOBNAME.fchk .' + '\n' + 
			   'mv $PBS_O_WORKDIR/$PBS_JOBNAME.fchk $PBS_O_WORKDIR/$PBS_JOBNAME.fchk_old' + '\n')
		file.write(' '+'\n' )
		file.write('$g09root/g09/unfchk $GAUSS_SCRDIR/00_$PBS_JOBNAME/$PBS_JOBNAME.fchk' + '\n'
			   'g09exe < $GAUSS_SCRDIR/00_$PBS_JOBNAME/$PBS_JOBNAME.com > $GAUSS_SCRDIR/00_$PBS_JOBNAME/$PBS_JOBNAME.log'+ '\n')
		file.write(' '+ '\n')
		file.write('echo "Job Ended at `date`" ' + '\n' +
			   'echo \'=======================================================\''+'\n' )
		file.write(' ' + '\n')
		file.write('$g09root/g09/formchk $GAUSS_SCRDIR/00_$PBS_JOBNAME/$PBS_JOBNAME.chk' + '\n' + 
			   'mv $GAUSS_SCRDIR/00_$PBS_JOBNAME/$PBS_JOBNAME.log $PBS_O_WORKDIR' + '\n' + 
			   'mv $GAUSS_SCRDIR/00_$PBS_JOBNAME/$PBS_JOBNAME.fchk $PBS_O_WORKDIR' + '\n' + 
			   'mv $GAUSS_SCRDIR/$PBS_JOBNAME.job.out $GAUSS_SCRDIR/$PBS_JOBNAME.job.err $PBS_O_WORKDIR' + '\n' + 
			   'rm -fr $GAUSS_SCRDIR/00_$PBS_JOBNAME')

