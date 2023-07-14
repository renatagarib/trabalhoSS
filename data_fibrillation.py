import wfdb

fileName = 'mit-bih-atrial-fibrillation-database-1.0.0/'
folderName = 'fibrillation/'

with open( fileName + 'RECORDS') as f:
    lines = f.readlines()

for i in range(len(lines)):
    lines[i] = lines[i][:-1]


count = 1
print("TOTAL LINES: {}".format(len(lines)))

write_current = 0
write_total = 0

for line in lines:
    try:
        print("CURRENT LINE: {}".format(count))

        start = 0
        sub_count = 1


        annotation = wfdb.rdann(fileName + line, 'qrsc')  # Assuming '100' is the record name and 'atr' is the annotation extension
        sample_indices = annotation.sample
        symbols = annotation.symbol
        for i in range(len(sample_indices)):
            print("Sample: {}, Symbol: {}".format(sample_indices[i], symbols[i]))
            if symbols[i] == 'N':
                end = sample_indices[i]
                signals, fields = wfdb.rdsamp(fileName + line, sampfrom=start, sampto=end)
                with open(folderName + str(count) + '-' + str(sub_count), 'w') as file:
                    for point in signals:
                        file.write(str(point[0]) + ' ' + str(point[1]) + '\n')
                        write_current = write_current + 1
                start = end + 1
                sub_count = sub_count + 1
        write_total = write_total + write_current
        write_current = 0
        print("FILES: {}".format(write_total))
        

        count = count + 1
    except ValueError:
        print("No ECG")
    except:
        print("No annotations")