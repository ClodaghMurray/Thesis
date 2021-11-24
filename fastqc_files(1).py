import os # set up directory variables
seq_dir ='test_dataset'
fastqc_dir ='fastqc_out'# create output directory
os.mkdir(fastqc_dir)
print ('# created subdir: ' + fastqc_dir)

# get list of FASTQ files
file_list = os.listdir(seq_dir)
print ('# got list of files in: ' + seq_dir)
# create the command string for each sequence
# & implement it 
for seq in file_list:
    command = 'fastqc ' + seq_dir + '/' + seq 
    print(command)
    os.system(command)
    
# mv html & zip files out of sequence directory 
# into FASTQC directory
command1 = 'mv ' + seq_dir + '/' + '*.html ' + fastqc_dir
print (command1)
os.system(command1)
command2 = 'mv ' + seq_dir + '/' + '*.zip ' + fastqc_dir
print (command2)
os.system(command2)

print ('#done')    
