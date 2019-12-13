import os, sys, time
from Bio.Blast import NCBIXML
from Bio.Blast import NCBIWWW
from Bio import SeqIO
#help(NCBIWWW.qblast)

current_dir = os.getcwd()
util_path = current_dir + "/util/"
sys.path.insert(0, util_path)
from util import *

def analyze_BLAST_result(result_handle):
    print "\nStep 2. Analyze the BLAST result."
    blast_records = NCBIXML.parse(result_handle)
    
    blast_records_list = list(blast_records) # once blast_records becomes a list, blast_records is no longer accessible
    print "len(blast_records_list): ", len(blast_records_list)
    
    #E_VALUE_THRESH = 0.04
    
    for blast_record in blast_records:
        for alignment in blast_record.alignments:
            for hsp in alignment.hsps:
                print ("****Alignment****")
                print ("sequence:", alignment.title)
                print ("length:", alignment.length)
                print ("e value:", hsp.expect)
                print (hsp.query[0:75] + "...")
                print (hsp.match[0:75] + "...")
                print (hsp.sbjct[0:75] + "...")
    
    '''
    output_file = open(output_file_name, "w") # since it is 'w', an existing file will be overwritten. (if this is "a", new info will be appended to an existing file)
    output_file.write(result_handle.read())
    output_file.close()
    '''
    
######## end of def analyze_BLAST_result(blast_records)


def run_BLAST_by_NCBI(input_fasta_name):
    print "\nStep 1. AutoHomology is searching NCBI website (blastp) with " + str(fasta_file_name) + ". Please wait."
    print "\tAs references,"
    print "\t\t41 amino acids tend to take 1 minute."
    print "\t\t451 amino acids tend to take 2 minutes."

    record = SeqIO.read(input_fasta_name, format="fasta")
    
    time_start_of_searching = time.time()    
    
    result_handle = NCBIWWW.qblast("blastp", "nr", record.format("fasta"))
    # "nr" means "Non-redundant protein sequences"
    
    time_end_of_searching = time.time()
    print show_time("\tBLAST searching", time_start_of_searching, time_end_of_searching)
    
    input_fasta_name_wo_path = os.path.basename(input_fasta_name)
    
    output_file_name = "retrieved_from_" + str(input_fasta_name_wo_path)[:-6] + ".xml"
    
    if not os.path.exists('output'):
        os.makedirs('output')

    current_dir = os.getcwd()    
    output_folder = os.path.join(current_dir, "output")
    
    os.chdir(output_folder)
                    
    return result_handle
######## end of def run_BLAST_by_NCBI(fasta_file_name)
    

if (__name__ == "__main__") :
    args=sys.argv[1:]
    if len(args) < 1:
        print "Input format: python run_me.py <a fasta file name that NCBI BLAST will be ran against> \n"
        print "Example usage: python run_me.py DGAT_target.fasta \n"
        exit(1)

fasta_file_name = args[0]

result_handle = run_BLAST_by_NCBI(fasta_file_name)
#print "\tSee retrieved results at the output folder.\n"

analyze_BLAST_result(result_handle)