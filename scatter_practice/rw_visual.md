

```python
import matplotlib.pyplot as plt
from random_walk import RandomWalk

while True:
    rw = RandomWalk(5000)
    rw.fill_walk()
    
    point_numbers = list(range(rw.num_points))
    plt.scatter(rw.x_values, rw.y_values, edgecolor='none', 
                c=point_numbers, s=5)
    
    plt.scatter(0, 0, c='green', edgecolor='none', s=50)
    plt.scatter(rw.x_values[-1], rw.y_values[-1], c='red', 
                   edgecolor='none', s=50)
    
    plt.axes().get_xaxis().set_visible(False)
    plt.axes().get_yaxis().set_visible(False)
    plt.figure(dpi=100)
    plt.show()
    
    keep_running = input("Make another walk?(y/n): ")
    if keep_running == 'n':
        break
```


![png](https://github.com/PythonandLee/Python_Matplotlib/blob/master/scatter_practice/rw_output_1.png)



    <Figure size 600x400 with 0 Axes>


    Make another walk?(y/n): y
    


![png](https://github.com/PythonandLee/Python_Matplotlib/blob/master/scatter_practice/rw_output_2.png)



    <Figure size 600x400 with 0 Axes>


    Make another walk?(y/n): y
    


![png](https://github.com/PythonandLee/Python_Matplotlib/blob/master/scatter_practice/rw_output_3.png)



    <Figure size 600x400 with 0 Axes>


    Make another walk?(y/n): n
    
