__author__ = 'Devon Timaeus'

import pandas as pd
from numpy import nan

'''
Essentially all of the data can be summed up and found via the value_counts method for each series we care about
So I'm just going to go through, grab those, store them, and then print them, with my answers/comments here in the code
'''

csv_info = pd.read_csv("Towed_Vehicles.csv")
#A
print "States Vehicles were towed from"
towed_states = csv_info['State'].value_counts()
print towed_states
'''
Most vehicles that were towed were from Illinois, which makes sense, seeing as the information is from Chicago, which is
the largest city in Illinois. Thus, since most of the vehicles there are likely owned by residents, it is reasonable most
vehicles are from Illinois
'''

#B
print "\n\nDates Vehicles were towed on"
towed_dates = csv_info['Tow Date'].value_counts()
print  csv_info['Tow Date'].value_counts().describe(), " \n\n"
print towed_dates
'''
It seems that there are actually quite a few dates that have more than a normal number of towings. The mean is right at
60 and the median is at 55, with the std_dev sitting at about 30, which means that any tows over about 90 (1 std), or
even 120 (2 std) would be considered a very far outlier, and we have 4 values that exceed this by a decent amount, 3 of
them by almost another full standard deviation. As far as lower than normal, if we consider the same boundaries, then we
would need to consider dates with less than or equal to NO tows, since 60-2*30 = 0. There are no days that fall in this
range, though there are some days that have far less tows, sitting at right around 1.5 std below the mean.
'''

#C
print "\n\nVehicles Towed"
towed_plates = csv_info['Plate'].value_counts()
print "\n\n", csv_info['Plate'].describe(), "\n\n"
print towed_plates
'''
There were actually 10 vehicles that were towed more than once, with 5 of them being towed more than 2 times! The vehicle
that was towed the most was towed 11 times, and is Plate number K729542.
'''