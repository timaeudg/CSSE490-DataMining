# grades.py

import numpy as np
import pandas as pd
from pandas import Series, DataFrame

col1 = ['Q1','Q2','Q3','Q4']
idx1 = ['Bob','Jim','Kim','Sue','Tom']
F1 = [[60,64,69,65],[52,57,59,55],[70,75,77,73],[90,93,97,95],[81,82,84,88]]
quizzes = DataFrame(F1,index=idx1,columns=col1)
print 'quizzes'
print quizzes
print

col1 = ['L1','L2','L3','L4']
idx1 = ['Bob','Jim','Kim','Sue','Tom']
F1 = [[61,67,68,62],[56,54,52,53],[71,76,72,78],[91,92,93,97],[80,89,87,89]]
lessons = DataFrame(F1,index=idx1,columns=col1)
print 'lessons'
print lessons
print

col1 = ['T1','T2','T3']
idx1 = ['Bob','Jim','Kim','Sue','Tom']
F1 = [[67,63,65],[52,51,58],[70,74,73],[98,97,92],[81,86,83]]
tests = DataFrame(F1,index=idx1,columns=col1)
print 'tests'
print tests
print

weights = Series({'quizzes':0.3,'lessons':0.3,'tests':0.4})
print 'weights'
print weights
print

ID = Series({4915:'Bob',6518:'Jim',1290:'Kim',5567:'Sue',3331:'Tom'})
print 'ID'
print ID
print

year = Series({4915:'sophomore',6518:'freshman',1290:'sophomore',5567:'sophomore',3331:'freshman'})
print 'year'
print year
print

major = Series({4915:'computer science',6518:'mathematics',1290:'computer science',5567:'mathematics',3331:'computer science'})
print 'major'
print major
print

