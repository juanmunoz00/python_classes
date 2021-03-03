##Step 1: import libraries
from numpy import random
import matplotlib.pyplot as plt
import numpy as np

##Setp 2: get the data to plot. It shall be an even list.
x=random.randint(100, size=(5))
y=random.randint(100, size=(5))

##Optional: print the data to plot
print(x)
print(y)

show = 1 ##Init
while( show > 0 ):
    flagPlot = True

    plt.title("Temp/RH")
    plt.xlabel("Num Partes")
    plt.ylabel("Temp")

    show = int(input("Show? (0 to exit): "))

    if( show == 1 ):
        plt.plot(y, marker = 'o')

    if( show == 2 ):
        print("Option disabled...")

    if( show == 3 ):
        plt.grid(color = 'green', linestyle = '--', linewidth = 0.5)

    if( show == 4 ):
        plt.scatter(x, y)
        flagPlot = False

    if( show == 5 ):
        colors = np.array([0, 10, 20, 30, 40])
        plt.scatter(x, y, c=colors, cmap='viridis')
        plt.colorbar()
        flagPlot = False

    if( show == 6 ):
        plt.bar(x, y)
        flagPlot = False

    if( show == 7 ):
        mylables = ["Ford", "Dodge", "Nissan", "Seat", "VW"]
        myexplode = [0.2, 0, 0, 0, 0]

        plt.pie(y, labels = mylables, explode = myexplode, shadow = True)
        flagPlot = False

    ##Display/show the graph
    if( flagPlot ):
         plt.plot(y)

    plt.show()
