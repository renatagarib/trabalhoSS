import wfdb

fileName = 'mit-bih-malignant-ventricular-ectopy-database-1.0.0/'
folderName = 'malignant/'

with open( fileName + 'RECORDS') as f:
    lines = f.readlines()

for i in range(len(lines)):
    lines[i] = lines[i][:-1]

count = 0

for line in lines:
    count = count + 1
    signals, fields = wfdb.rdsamp(fileName + line)
    with open(folderName + str(count), 'w') as file:
        for point in signals:
            file.write(str(point[0]) + ' ' + str(point[1]) + '\n')