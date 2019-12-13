import os, sys, time
from Bio.Blast import NCBIXML
from Bio.Blast import NCBIWWW
from Bio import SeqIO
#help(NCBIWWW.qblast)

current_dir = os.getcwd()
util_path = current_dir + "/util/"
sys.path.insert(0, util_path)
from util import *

def run_BLAST_by_NCBI(input_fasta_name):
    
    record = SeqIO.read(input_fasta_name, format="fasta")
    
    time_start_of_searching = time.time()
    
    result_handle = NCBIWWW.qblast("blastp", "nr", record.format("fasta"))
    
    time_end_of_searching = time.time()
    print show_time("BLAST searching", time_start_of_searching, time_end_of_searching)
    
    input_fasta_name_wo_path = os.path.basename(input_fasta_name)
    
    output_file_name = "retrieved_from_" + str(input_fasta_name_wo_path)[:-6] + ".xml"
    
    if not os.path.exists('output'):
        os.makedirs('output')

    current_dir = os.getcwd()    
    output_folder = os.path.join(current_dir, "output")
    
    os.chdir(output_folder)
    
    output_file = open(output_file_name, "w") # since it is 'w', an existing file will be overwritten. (if this is "a", new info will be appended to an existing file)
    output_file.write(result_handle.read())
    output_file.close()
    
    result_handle.close()
######## end of def run_BLAST_by_NCBI(fasta_file_name)
    

if (__name__ == "__main__") :
    args=sys.argv[1:]
    if len(args) < 1:
        print "input format: python run_me.py <a fasta file name that NCBI BLAST will be ran against> \n"
        print "example usage: python run_me.py DGAT_target.fasta \n"
        exit(1)

fasta_file_name = args[0]
print "\nStep 1. AutoHomology searches NCBI website (blastp) with " + str(fasta_file_name) + ". Please wait."
print "\tFor example,"
print "\t\t41 amino acids tend to take 1 minute."
print "\t\t451 amino acids tend to take 2 minutes.\n"

run_BLAST_by_NCBI(fasta_file_name)

print "See retrieved results at the output folder.\n"