#Opens source file, copies contents into string text, closes source file
source = open('rosalind_rna.txt', 'r')
text = source.read()
source.close()

#Opens output file
output = open('<Transcribing>output.txt', 'w') 

#Strips text string of \n
text = text.strip()

#Runs through text, adds character to RNA(string), if "T" adds "U" instead
RNA = ""
for character in text:
    if character == "T":
        RNA = RNA + "U"
    else:
        RNA = RNA + character

#Writes RNA to output
output.write(RNA)

output.close()
