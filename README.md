# Extract-part-of-sequence-in-FASTA-format
Extracting part of the sequence is not an easy when you have big fasta file with 95% BLASTN match for your target sequence start from 6052 up to 7916. Regardless your operating system, here a python code can be edit and run in all OS. 

# How to start ? 
You need the following : 

1 - Fasta file has the full sequence and your target sequence is part of it. 

// This is ((YOUR_FASTA_FILE.fasta)) in below python code 

2 - Get the range of your target sequence start from xxxx and end to xxxx.

//Thia is example (([6052:7916]) replace it with your range in below python code 

3 - Create new file results.fasta in order to get your target sequence.

// This is ((CREATE_EMPTY_FILE.fasta)) in below python code 

4 - Ensure all the above files in same folder then run your python code. 


# Python Code for extract part of sequence into fasta format

mydoc =  open("YOUR_FASTA_FILE.fasta")

dnaread = mydoc.read()

seqRange = dnaread[6052:7916]

cifseqopen = open("CREATE_EMPTY_FILE.fasta","w")

cifseqopen.write(seqRange)

