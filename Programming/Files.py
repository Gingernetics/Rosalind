source = open('rosalind_ini5.txt', 'r')
text = source.read()
source.close()

f = open('<Files>output.txt', 'w')

lines = text.splitlines()
answer = ""
T = 0

for i in lines:
    T = T + 1
    if T % 2 == 0:
        f.write(str(i) + '\n')     



f.close()
