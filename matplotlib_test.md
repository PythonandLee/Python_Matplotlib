    import matplotlib.pyplot as plt

    input_values = [1, 2, 3, 4, 5]
    squares = [1, 4, 9, 16, 25]
    plt.plot(input_values, squares, linewidth=5)
    plt.title("Square Numbers", fontsize=25)
    plt.xlabel("Value", fontsize =14)
    plt.ylabel("Square or Value", fontsize=14)

    plt.tick_params(axis='both', labelsize=14)
    plt.show()
![image](https://github.com/PythonandLee/Python_Matplotlib/blob/master/test.png)


    import matplotlib.pyplot as plt
    x_values = [1, 2, 3, 4, 5]
    y_values = [1, 4, 9, 16, 25]

    plt.scatter(x_values, y_values, s=100)
    plt.xlabel('Value', fontsize=14)
    plt.ylabel('Square of Value', fontsize=14)
    plt.title('Square Numbers', fontsize=25)

    plt.tick_params(axis='both', labelsize=14)
    plt.show()
![image](https://github.com/PythonandLee/Python_Matplotlib/blob/master/test2.png)
