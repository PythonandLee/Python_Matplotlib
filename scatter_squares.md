    import matplotlib.pyplot as plt

    x_values = list(range(1, 1001))
    y_values = [x**2 for x in x_values]

    plt.scatter(x_values, y_values, edgecolor='none', s=10)
    plt.title('Square Number', fontsize=25)
    plt.xlabel('Value', fontsize=15)
    plt.ylabel('Square of Value', fontsize=15)

    plt.axis([0, 1100, 0, 1100000])
    plt.savefig('square_plot.jpg')
![image](https://github.com/PythonandLee/Python_Matplotlib/blob/master/square_plot.jpg)

    import matplotlib.pyplot as plt

    x_values = list(range(1, 1001))
    y_values = [x**2 for x in x_values]

    plt.scatter(x_values, y_values, c=y_values, cmap=plt.cm.Blues, edgecolor='none', s=10)
    plt.title('Square Number', fontsize=25)
    plt.xlabel('Value', fontsize=15)
    plt.ylabel('Square of Value', fontsize=15)

    plt.axis([0, 1100, 0, 1100000])
    plt.savefig('square_plot2.jpg')
![image](https://github.com/PythonandLee/Python_Matplotlib/blob/master/square_plot2.jpg)    
