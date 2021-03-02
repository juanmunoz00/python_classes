from datetime import datetime

now = datetime.now()
dt_string = now.strftime("%d/%m/%Y %H:%M:%S")

try:
    with open("test.txt",'w') as f:
        f.write("my first file - "+ dt_string +"\n")
        f.write("This file\n\n")
        f.write("contains three lines\n")
except:
    print("Ya existe ese archivo")

try:
    xfile = open("test.txt")
    for ln in xfile:
        print(ln)
except:
    print("No se creo o no existe el archivo")
    quit()

"""
Try it!
longStr = (r"C:\Users\jrwaller\Documents\Automated Eve\NewTest.txt")

with open(longStr) as old_file:
    with open(r"C:\Users\jrwaller\Documents\Automated Eve\NewTestEdited.txt", "w") as new_file:
        for line in old_file:
            if "This" in line:
                line=line.replace(line,line+"added\n")
            new_file.write(line)
"""

"""
To CSV
import csv

with open('log.txt', 'r') as in_file:
    stripped = (line.strip() for line in in_file)
    lines = (line.split(",") for line in stripped if line)
    with open('log.csv', 'w') as out_file:
        writer = csv.writer(out_file)
        writer.writerow(('title', 'intro'))
        writer.writerows(lines)
"""