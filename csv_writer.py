import csv

cntMp = dict()
with open('/Path/To/readTxtfile') as fileobject:
        for line in fileobject:
                kv = line.split('\t')
                if kv[0] in cntMp:
                        cntMp[kv[0]] += int(kv[1])
                else:
                        cntMp[kv[0]] = int(kv[1])

print cntMp

with open('/Path/To/writeTxtfile','w') as filewriter:
        for key in cntMp:
                filewriter.write(key+'\t'+str(cntMp[key])+'\n')

with open('/Path/To/csvfile','wb') as csvfile:
        csvwriter = csv.writer(csvfile, delimiter=',', quotechar='|', quoting=csv.QUOTE_MINIMAL)
        for key in cntMp:
                csvwriter.writerow([key, str(cntMp[key])])
