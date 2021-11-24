
# script uses the conda installation of Trimmomatic
# this means that you don't have to do all the 'java -jar' stuff


import os
seq_dir = 'test_dataset'
trim_out = 'trim_out'
standard1 =' SE -phred33 ' 
standard2 = ' ILLUMINACLIP:TruSeq3-SE:2:30:10 LEADING:3 TRAILING:3 SLIDINGWINDOW:4:15 MINLEN:36'


file_list = os.listdir(seq_dir)
print('# got list of files in: ' + seq_dir)

os.mkdir(trim_out)
print('# created subdir: ' + trim_out)

for seq in file_list:
   command_trim = 'trimmomatic' + standard1 + seq_dir + '/' + seq +' ' + trim_out + '/' + seq +'.trimmed' + standard2
   print(command_trim)
   os.system(command_trim)


# in case you have trimmomatic installed as the java file, replace the start of the string command_trim 
# above with the following
#
# command_trim = 'java -jar /home/ag/sw/Trimmomatic-0.38/trimmomatic-0.38.jar ' + standard1 etc.
#
# note: this is configured for my file system - you'll need to change it to where you have installed
# trimmomatic

