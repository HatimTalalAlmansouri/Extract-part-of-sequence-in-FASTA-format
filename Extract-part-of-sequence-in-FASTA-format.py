mydoc = open("YOUR_FASTA_FILE.fasta")

dnaread = mydoc.read()

seqRange = dnaread[6052:7916]

myseqopen = open("CREATE_EMPTY_FILE.fasta","w")

myseqopen.write(seqRange)
