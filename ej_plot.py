import matplotlib.pyplot as plt 

import matplotlib.pyplot as plt
import numpy as np

"""
##Colors:
'r' - Red
'g' - Green
'b' - Blue
'c' - Cyan
'm' - Magenta
'y' - Yellow
'k' - Black
'w' - White
"""
show = 1##Init
while ( show > 0 ):
    show = int(input("Show? (0 to exit): "))
    try:
        if( show == 1 ):
            xpoints = np.array([0, 6])
            ypoints = np.array([0, 250])

            plt.plot(xpoints, ypoints)

        if( show == 2 ):
            ypoints = np.array([3, 8, 1, 10])

            plt.plot(ypoints, marker = 'o')

        if( show == 3 ):
            x = np.array([80, 85, 90, 95, 100, 105, 110, 115, 120, 125])
            y = np.array([240, 250, 260, 270, 280, 290, 300, 310, 320, 330])

        if( show == 4 ):
            x = np.array([80, 85, 90, 95, 100, 105, 110, 115, 120, 125])
            y = np.array([240, 250, 260, 270, 280, 290, 300, 310, 320, 330])

            plt.title("Sports Watch Data")
            plt.xlabel("Average Pulse")
            plt.ylabel("Calorie Burnage")

            plt.plot(x, y)

            #plt.grid(axis = 'y') ##or x
            plt.grid(color = 'green', linestyle = '--', linewidth = 0.5)    

            plt.plot(x, y)

            plt.xlabel("Average Pulse")
            plt.ylabel("Calorie Burnage")

        if( show == 5 ):
            x = np.array([5,7,8,7,2,17,2,9,4,11,12,9,6])
            y = np.array([99,86,87,88,111,86,103,87,94,78,77,85,86])

            plt.scatter(x, y)
            ##plt.scatter(x, y, color = '#88c999') ##Color

        if( show == 6 ):
            ##Subset 1
            x = np.array([5,7,8,7,2,17,2,9,4,11,12,9,6])
            y = np.array([99,86,87,88,111,86,103,87,94,78,77,85,86])
            plt.scatter(x, y)

            ##Subset 2
            x = np.array([2,2,8,1,15,8,12,9,7,3,11,4,7,14,12])
            y = np.array([100,105,84,105,90,99,90,95,94,100,79,112,91,80,85])
            plt.scatter(x, y)        

        if( show == 7 ):
            x = np.array([5,7,8,7,2,17,2,9,4,11,12,9,6])
            y = np.array([99,86,87,88,111,86,103,87,94,78,77,85,86])
            colors = np.array([0, 10, 20, 30, 40, 45, 50, 55, 60, 70, 80, 90, 100])

            plt.scatter(x, y, c=colors, cmap='viridis')

            plt.colorbar()

        if( show == 8 ):
            x = np.array(["A", "B", "C", "D"])
            y = np.array([3, 8, 1, 10])

            ##plt.bar(x, y, color = "#4CAF50") ##Color
            plt.bar(x, y, width = 0.1)    

        if( show == 9 ):
            y = np.array([35, 25, 25, 15])
            mylabels = ["Apples", "Bananas", "Cherries", "Dates"]
            myexplode = [0.2, 0, 0, 0]

            plt.pie(y, labels = mylabels, explode = myexplode, shadow = True)

            """
            ##Colors
            y = np.array([35, 25, 25, 15])
            mylabels = ["Apples", "Bananas", "Cherries", "Dates"]
            myexplode = [0.2, 0, 0, 0]

            plt.pie(y, labels = mylabels, explode = myexplode, shadow = True)    
            """

        plt.show()    
    except:
        print("There was a problem")