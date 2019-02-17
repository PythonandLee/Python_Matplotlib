    import matplotlib.pyplot as plt
    from random_walk import RandomWalk

    while True:
        plt.rcParams['figure.dpi'] = 100
        rw = RandomWalk()
        rw.fill_walk()
        plt.scatter(rw.x_values, rw.y_values, s=1)
        plt.show()
    
        keep_walking = input("Make another walk?(y/n): ")
        if keep_walking == 'n':
           break

![image](https://github.com/PythonandLee/Python_Matplotlib/blob/master/random_walk.jpg)

