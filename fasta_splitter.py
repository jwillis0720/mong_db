#!/usr/bin/env python2.6
import Bio.SeqIO
import sys
from optparse import OptionParser
def usage():
    '''Get parent file and records number back along witht he usage'''
    usage = "%prog [options] --help"
    parser = OptionParser(usage)
    parser.add_option("-p","--parent_file",dest="parent_file",help="FASTA file to be split.")
    parser.add_option("-d","--rec_per_file",type=int,dest="rec_per_file",default=10000,help="Number of FASTA records to send to each file. Defaults to 100000")
    (options, args)=parser.parse_args()
    # If a fasta file is input:
    if options.parent_file:
        # Print the record:
        print "Splitting", options.parent_file, "into", options.rec_per_file, "records per daughter file..."
        return options
    else: #we atleast need the parent file - should of made this an argument. but whatever
        parser.print_help()
        parser.exit()               
def write_file(options):
        #get file_counter and base name of fasta_file
        parent_file_base_name = options.parent_file.split(".")[0]
        counter = 1
         
        #our first file name
        file = parent_file_base_name + "_" + str(counter) + ".fasta"
         
        #carries all of our records to be written
        joiner = []
        #enumerate huge fasta
        for num,record in enumerate(Bio.SeqIO.parse(options.parent_file, "fasta"),start=1):
             
            #append records to our list holder
            joiner.append(">" + record.id + "\n" + str(record.seq))
             
            #if we have reached the maximum numbers to be in that file, write to a file, and then clear
            #record holder
            if num % options.rec_per_file == 0:
                joiner.append("")
                with open(file,'w') as f:
                    f.write("\n".join(joiner))    
                 
                #change file name,clear record holder, and change the file count
                counter += 1
                file = parent_file_base_name + "_" + str(counter) + ".fasta"   
                joiner = []
	if joiner:
		joiner.append("")
		with open(file,'w') as f:
	     		f.write("\n".join(joiner))
             
if __name__ == "__main__":
    options = usage()
    write_file(options)
    print "fasta_splitter.py is finished."
