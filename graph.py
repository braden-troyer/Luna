import matplotlib.pyplot as plt
import csv
from os.path import exists

filename = 'statistics.csv'

if exists(filename):
    x=[]
    y=[]

    with open(filename, 'r') as csvfile:
        plots= csv.reader(csvfile, delimiter=',')
        counter = 0
        for row in plots:
            if counter == 0:
                counter += 1
            else:
                x.append(int(row[1]))
                y.append(int(row[2]))

    print(x)
    plt.plot(x,y, marker='o')

    plt.title('Data from the CSV File: Typing')

    plt.xlabel('Time(In Minutes)')
    plt.ylabel('Characters Typed')

    plt.show()
else:
    print("File Does Not Exist")