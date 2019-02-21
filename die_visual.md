

```python
import pygal
from dice import Dice

# create practice of using class 'Dice()'
dice = Dice()

#simulate roll dice 1000 times, and store results in list
results = []
for roll_num in range(1000):
    result = dice.roll()
    results.append(result)

# count 'results' and store count results in the list 'frequencies'    
frequencies = []
for value in range(1, dice.num_sides+1):
    frequency = results.count(value)
    frequencies.append(frequency)
     
print(frequencies)


"""create a bar graph"""
hist = pygal.Bar()

hist.title = "Results of rolling one D6 1000 times"
hist.x_labels = ['1', '2', '3', '4', '5', '6']
hist.x_title = "Result"
hist.y_title = "Frequency of Result"

hist.add('D6', frequencies)
hist.render_to_file('die_visual.svg')
```

    [157, 174, 185, 164, 163, 157]
    
![image](https://github.com/PythonandLee/Python_Matplotlib/blob/master/die_visual2.svg)    
    


```python

```
