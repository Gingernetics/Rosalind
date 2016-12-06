#Opens source file, copies contents into string text, closes source file
source = open('rosalind_dna.txt', 'r')
text = source.read()
source.close()

#Opens output file
output = open('<CountingNTs>output.txt', 'w') 

#Strips text string of \n
text = text.strip()

#Creates an array words with each word of text an element
words = text.split(" ")

#Creates dictionary Frequency with elements of words(array) 
#as keys and frequency of word as corresponding value
Frequency = {}
for word in words:
    if word in Frequency:
        Frequency[word] = Frequency[word] + 1
    else:
        Frequency[word] = 1

#Writes content of Frequency(array) to output
for word in Frequency:
    output.write(word + " " + str(Frequency[word]) + "\n") 

output.close()

