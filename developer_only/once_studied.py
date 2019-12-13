print ("len(blast_qresult):", len(blast_qresult))
print (blast_qresult)


print ("%s %s" %(blast_qresult.program, blast_qresult.version)) # blastp 2.10.0+
print "blast_qresult.param_evalue_threshold:", blast_qresult.param_evalue_threshold # 10.0

for hit in blast_qresult[:5]:
    print ("%s %i" % (hit.id, hit.seq_len))
    
blast_records = NCBIXML.parse(result_handle)
blast_records_list = list(blast_records)
# "result_handle.read()" is done -> "raise ValueError("Your XML file was empty")"

for hit in blast_qresult[:5]:
    print ("%s %i" % (hit.id, hit.seq_len))
        
sort_key = lambda hit: hit.seq_len
sorted_qresult = blast_qresult.sort(key=sort_key, reverse=True, in_place=False)
for hit in sorted_qresult[:5]:
    print ("%s %s" %(hit.id, hit.seq_len))

filter_func = lambda hit: len(hit.hsps) > 1
print "len(blast_qresult):", len(blast_qresult)

filtered_qresult = blast_qresult.hit_filter(filter_func)
print "len(filtered_qresult):", len(filtered_qresult)

for hit in filtered_qresult[:5]:
    print ("%s %i" % (hit.id, len(hit.hsps)))

def map_func(hit):
    #hit.id = hit.id.split("|")[3]
    splited_hit_id = hit.id.split("|")
    hit.id = splited_hit_id[len(splited_hit_id)-1]
    return hit

mapped_qresult = blast_qresult.hit_map(map_func)
for hit in mapped_qresult[:5]:
    print ("hit.id:", hit.id)
    print "hit.id:", hit.id
    
for blast_record_list in blast_records_list:
    for alignment in blast_record_list.alignments:
        for hsp in alignment.hsps:
            print ("****Alignment****")
            print ("sequence:", alignment.title)
            print ("length:", alignment.length)
            print ("e value:", hsp.expect)
            #print (hsp.query[0:75] + "...")
            #print (hsp.match[0:75] + "...")
            #print (hsp.sbjct[0:75] + "...")
