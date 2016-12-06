#Opens source file, copies contents into string text, closes source file
source = open('rosalind_dna.txt', 'r')
text = source.read()
source.close()

#Opens output file
output = open('<CountingNTs>output.txt', 'w') 

#Strips text string of \n
text = text.strip()

#Counts the frequency of each base
A = text.count("A")
C = text.count("C")
G = text.count("G")
T = text.count("T")

#Writes frequencies to output
output.write(str(A) + " " + str(C) + " " + str(G) + " " + str(T))

output.close()
