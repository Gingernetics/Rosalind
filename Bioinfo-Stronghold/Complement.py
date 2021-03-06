#Opens source file, copies contents into string text, closes source file
source = open('rosalind_revc.txt', 'r')
text = source.read()
source.close()

#Opens output file
output = open('<Complement>output.txt', 'w') 

#Strips text string of \n
text = text.strip()

#Creates dictionary Pairs that has opposite keys/values
Pairs = {'A':'T', 'C':'G', 'G':'C', 'T':'A'}

#Creates string DNA by iterating through text(string) and adding 
#counterpart to the beginning
DNA = ""
for character in text:
    DNA = Pairs[character] + DNA

#Writes DNA to output
output.write(DNA)

output.close()
