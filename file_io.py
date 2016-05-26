s = ""

frd = open('input_file_name', 'r')
for block in iter(lambda: frd.read(4), ""):
        s += str(block)
print(s)
frd.close()

fwt = open('output_file_name','w')
fwt.write(s)
fwt.write('\n')
words = s.split(' ')
print(len(words))
for wd in words:
        fwt.write("%s\n" % wd)
fwt.close()

