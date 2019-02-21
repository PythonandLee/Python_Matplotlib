

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

    [154, 158, 171, 178, 183, 156]
    
![image](https://github.com/PythonandLee/Python_Matplotlib/blob/master/die_visual.svg)    
    


```python
import pygal
from dice import Dice

# create practice of using class 'Dice()'
dice1 = Dice()
dice2 = Dice()

#simulate roll dice 1000 times, and store results in list
results = []
for roll_num in range(1000):
    result = dice1.roll() + dice2.roll()
    results.append(result)

# count 'results' and store count results in the list 'frequencies'    
frequencies = []
max_result = dice1.num_sides + dice2.num_sides
for value in range(2, max_result+1):
    frequency = results.count(value)
    frequencies.append(frequency)
     
print(frequencies)


"""create a bar graph"""
hist = pygal.Bar()

hist.title = "Results of rolling two D6 1000 times"
hist.x_labels = ['2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12']
hist.x_title = "Result"
hist.y_title = "Frequency of Result"

# give name of label
hist.add('D6 + D6', frequencies)
hist.render_to_file('die_visual2.svg')

```
![image](https://github.com/PythonandLee/Python_Matplotlib/blob/master/die_visual2.svg)
