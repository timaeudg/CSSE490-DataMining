__author__ = 'Devon Timaeus'

import numpy as np
import math
import matplotlib.pyplot as plt

#First, we need a place for the bear to be seeking out, that is, a location for food to be
food_location = np.random.uniform(low=-1000, high=1000, size=2)
food_x = food_location[0]
food_y = food_location[1]

bear_location = np.random.uniform(low=-100, high=100, size=2)
bear_x = bear_location[0]
bear_y = bear_location[1]

#Now that we have where the food is, let's make a logarithmic-distance, linear path to the food, the intention here is to
#half the distance to the food each time, until the bear is within a certain distance, the reason for this is that
#the bear would be pretty good (after evolution, years of learning, etc) at knowing that food is in a general direction,
#and as such, so long as the wind was still coming from that direction somewhat, no need to change direction. However,
#once the bear gets closer by probably about half the distance, it is reasonable to refine the direction, as the wind/smell
#would have changed in direction by a fairly significant amount comparatively. That being said, the bear only needs to get
#within a certain distance, from there, the bear could just see the food, and doesn't have to rely on smell

#First, find the distance to the food in each dimension
x_distance_to_food = abs(food_x - bear_x)
y_distance_to_food = abs(food_y - bear_y)

#Then calculate the number of steps needed to get basically to the food
x_log = math.log(x_distance_to_food, 2)
y_log = math.log(y_distance_to_food, 2)

#Now come up with the x and y locations the bear should go to in order to half its distance in x and y each time
x_step_size = np.logspace(x_log, 0.0, num=100, base=2.0)
y_step_size = np.logspace(y_log, 0.0, num=100, base=2.0)

#adjust the values according to whether the bear is moving east or west, and north or south, since all the values were
#positive before
if bear_x > food_x:
    x_step_size = -x_step_size
if bear_y > food_y:
    y_step_size = -y_step_size

#offset the values to start at the bear and end at the food (there will be some error due to the next part)
x_step_size = x_step_size + bear_x
y_step_size = y_step_size + bear_y

#Come up with the multipliers for each value to account for the wind misguiding the bear
x_wind_randomness = np.random.uniform(low=0.925, high=1.075, size=100)
y_wind_randomness = np.random.uniform(low=0.925, high=1.075, size=100)

#Add the wind into the bear's movement. This causes some error in the bear's starting and ending position, since they
# are technically moved as well, in this case though, it's not that important, since it's a bear
x_step_size = x_step_size * x_wind_randomness
y_step_size = y_step_size * y_wind_randomness

#The points shoudl be ready for plotting
x = x_step_size
y = y_step_size

print "Bear location: ", bear_location
print "Food Location: ", food_location
#plot the bear's path
plt.plot(x,y)
#plot the bear's starting location as a red diamond and the food's location as a green diamond
plt.plot(bear_x, bear_y, 'rD')
plt.plot(food_x, food_y, 'gD')
#show the plot
plt.show()