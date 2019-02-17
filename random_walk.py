from random import choice

class RandomWalk():
    """a class for creating random digits"""
    
    def __init__(self, num_points=5000):
        self.num_points = num_points
        
        # all numbers start form '0'
        self.x_values = [0]
        self.y_values = [0]
        
    def fill_walk(self):
        # all random digits
        
        while len(self.x_values) < self.num_points:
            # keep creating digits till > num_point
            # random choose directions and distances
            
            x_direction = choice([1, -1])
            x_distance = choice([0, 1, 2, 3, 4])
            x_step = x_direction * x_distance
            
            y_direction = choice([1, -1])
            y_distance = choice([0, 1, 2, 3, 4])
            y_step = y_direction * y_distance
            
            # create a 'if' boolean to avoid pick the same number
            if  x_step == 0 and y_step ==0:
                continue
            # count next 'x' and 'y'    
            next_x = self.x_values[-1] + x_step
            next_y = self.y_values[-1] + y_step
            
            self.x_values.append(next_x)
            self.y_values.append(next_y)                  
