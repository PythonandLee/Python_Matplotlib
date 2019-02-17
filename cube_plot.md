    import matplotlib.pyplot as plt
    """create a plot of cube number of number 1-5"""

    x_values = [1, 2, 3, 4, 5]
    y_values = [1, 8, 27, 64, 125]

    plt.scatter(x_values, y_values, s=10)
    plt.title('Cube Number', fontsize=25)
    plt.xlabel('Value', fontsize=15)
    plt.ylabel('Cube of Value', fontsize=15)

    plt.tick_params(axis='x', which='major', labelsize=13)
    plt.savefig('cube_plot.jpg')
![image](https://github.com/PythonandLee/Python_Matplotlib/blob/master/cube_plot.jpg)

    import matplotlib.pyplot as plt
    """create a plot of cube number of number 1-5000"""

    x_values = list(range(1, 5000))
    y_values = [x**3 for x in x_values]

    plt.scatter(x_values, y_values, c=y_values, cmap=plt.cm.viridis, edgecolor='none', s=10)
    plt.title('Cube Number', fontsize=25)
    plt.xlabel('Value', fontsize=15)
    plt.ylabel('Cube of Value', fontsize=15)

    plt.savefig('cube_plot2.jpg')
![image](https://github.com/PythonandLee/Python_Matplotlib/blob/master/cube_plot2.jpg)
