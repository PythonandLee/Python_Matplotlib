    import matplotlib.pyplot as plt
    from random_walk import RandomWalk

    while True:
        plt.rcParams['figure.dpi'] = 200
        rw = RandomWalk()
        rw.fill_walk()
        plt.scatter(rw.x_values, rw.y_values, s=1)
        plt.show()
    
        keep_walking = input("Make another walk?(y/n): ")
        if keep_walking == 'n':
           break

![image](https://github.com/PythonandLee/Python_Matplotlib/blob/master/random_walk.jpg)

    import matplotlib.pyplot as plt
    from random_walk import RandomWalk

    while True:
      plt.rcParams['figure.dpi'] = 100
      rw = RandomWalk()
      rw.fill_walk()
    
      point_numbers = list(range(rw.num_points))
      plt.scatter(rw.x_values, rw.y_values, c=point_numbers,
                cmap=plt.cm.YlGn, edgecolor='none', s=5)
      plt.show()

      keep_walking = input("Make another walk?(y/n): ")
      if keep_walking == 'n':
         break
         
![image](https://github.com/PythonandLee/Python_Matplotlib/blob/master/random2_walk.jpg)
