import wfdb

with open('mit-bih-normal-sinus-rhythm-database-1.0.0/RECORDS') as f:
    lines = f.readlines()

for i in range(len(lines)):
    lines[i] = lines[i][:-1]

count = 1

for line in lines:
    
    start = 0
    sub_count = 1
    
    annotation = wfdb.rdann('mit-bih-normal-sinus-rhythm-database-1.0.0/' + line, 'atr') 

    sample_indices = annotation.sample
    symbols = annotation.symbol

    for i in range(len(sample_indices)):
        if symbols[i] == 'N':
            end = sample_indices[i]
            signals, fields = wfdb.rdsamp('mit-bih-normal-sinus-rhythm-database-1.0.0/' + line, sampfrom=start, sampto=end)
            with open('normal/' + str(count) + '-' + str(sub_count), 'w') as file:
                for point in signals:
                    file.write(str(point[0]) + ' ' + str(point[1]) + '\n')

            start = end + 1
            sub_count = sub_count + 1
            

    count = count + 1