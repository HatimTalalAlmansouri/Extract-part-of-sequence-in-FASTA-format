# Extract-part-of-sequence-in-FASTA-format
Extracting part of the sequence is not an easy when you have big fasta file with 95% BLASTN match for your target sequence start from 3048 up to 3099. Regardless your operating system, here a python can be edit in all OS. 

# How to start ? 
You need the following : 

1 - Fasta file has the full sequence and your target sequence is part of it. // this is ((YOUR_FASTA_FILE.fasta)) in below python code 

mydoc =  open("YOUR_FASTA_FILE.fasta")
dnaread = mydoc.read()
seqRange = dnaread[367052:377918]
cifseqopen = open("CREATE_EMPTY_FILE.fasta","w")
cifseqopen.write(seqRange)
