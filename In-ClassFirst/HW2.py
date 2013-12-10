__author__ = 'Devon Timaeus'

import pandas as pd
from numpy import nan

#part A

maxScores = pd.read_csv("grades/MaxScore.csv", index_col=0, header=None, names=None)

lessonsA = (pd.read_csv("grades/lessonsA.csv", index_col=0).astype(float) / maxScores.ix['L1':'L6'][1]).fillna(0.0)
lessonsB = (pd.read_csv("grades/lessonsB.csv", index_col=0).astype(float) / maxScores.ix['L1':'L6'][1]).fillna(0.0)

meanLessonsA = pd.DataFrame(lessonsA.mean(axis=1))
meanLessonsB = pd.DataFrame(lessonsB.mean(axis=1))

homeworkA = (pd.read_csv("grades/homeworkA.csv", index_col=0).astype(float) / maxScores.ix['H1':'H15'][1]).fillna(0.0)
homeworkB = (pd.read_csv("grades/homeworkB.csv", index_col=0).astype(float) / maxScores.ix['H1':'H15'][1]).fillna(0.0)

meanHomeworkA = pd.DataFrame(homeworkA.mean(axis=1))
meanHomeworkB = pd.DataFrame(homeworkB.mean(axis=1))

quizzesA = (pd.read_csv("grades/quizzesA2.csv", index_col=0).astype(float) / maxScores.ix['Q1':'Q6'][1]).fillna(0.0)
quizzesB = (pd.read_csv("grades/quizzesB2.csv", index_col=0).astype(float) / maxScores.ix['Q1':'Q6'][1]).fillna(0.0)

meanQuizzesA = pd.DataFrame(quizzesA.mean(axis=1))
meanQuizzesB = pd.DataFrame(quizzesB.mean(axis=1))

testsA = (pd.read_csv("grades/testsA.csv", index_col=0).astype(float) / maxScores.ix['T1':'T3'][1]).fillna(0.0)
testsB = (pd.read_csv("grades/testsB.csv", index_col=0).astype(float) / maxScores.ix['T1':'T3'][1]).fillna(0.0)

meanTestsA = pd.DataFrame(testsA.mean(axis=1))
meanTestsB = pd.DataFrame(testsB.mean(axis=1))

finalA = (pd.read_csv("grades/finalA.csv", index_col=0).astype(float) / maxScores.ix['F1':'F2'][1]).fillna(0.0)
finalB = (pd.read_csv("grades/finalB.csv", index_col=0).astype(float) / maxScores.ix['F1':'F2'][1]).fillna(0.0)

meanFinalA = pd.DataFrame(finalA.mean(axis=1))
meanFinalB = pd.DataFrame(finalB.mean(axis=1))

weights = pd.read_csv("grades/weights.csv", index_col=0, header=None, names=None)
homeworkWeight = weights.ix['homework'][1]
lessonWeight = weights.ix['lessons'][1]
quizWeight = weights.ix['quizzes'][1]
testWeight = weights.ix['tests'][1]
finalWeight = weights.ix['final'][1]

course_grade_A = meanLessonsA*lessonWeight + meanHomeworkA*homeworkWeight + meanQuizzesA*quizWeight \
                 + meanTestsA*testWeight + meanFinalA*finalWeight

course_grade_B = meanLessonsB*lessonWeight + meanHomeworkB*homeworkWeight + meanQuizzesB*quizWeight \
                 + meanTestsB*testWeight + meanFinalB*finalWeight

course_grade_A.columns = ['Final Grade']
course_grade_B.columns = ['Final Grade']

meanFinalA.columns = ['Finals']
meanFinalB.columns = ['Finals']
meanTestsA.columns = ['Tests']
meanTestsB.columns = ['Tests']
meanQuizzesA.columns = ['Quizzes']
meanQuizzesB.columns = ['Quizzes']
meanHomeworkA.columns = ['Homeworks']
meanHomeworkB.columns = ['Homeworks']
meanLessonsA.columns = ['Lessons']
meanLessonsB.columns = ['Lessons']

averages_A = pd.concat([meanLessonsA, meanHomeworkA, meanQuizzesA, meanTestsA, meanFinalA, course_grade_A], axis=1)
averages_B = pd.concat([meanLessonsB, meanHomeworkB, meanQuizzesB, meanTestsB, meanFinalB, course_grade_B], axis=1)

#while looking at the data, the first section appears to be mostly floating around 75% with another section around 80%
#with only a very few bumping into the 90%+ range. For Section B there seemed to be many more that were around the B/B+
#grade area, but fewer numbers of A's. Overall Section B had the higher class average

#part B

def remove_lowest(row):
    #First, get the series that should hold the lowest grade
    lowest = row.rank(method='min')[row.rank(method='min')==1]
    #There may be ties, in which case, the rank is 1.* so we need to account for that and get a series for values
    #1.0<x<2.0 so that we get any tied values
    lowestTie = row.rank(method='min')[row.rank(method='min')<2]
    indexToNaN = None
    if lowest.size == 0:
    #    We don't have a single lowest element, so we need to just pick one of the elements that tied
        indexToNaN = lowestTie.index[0]
    else:
        #We have a single element, so just get the index so we can NaN it so it's ignored in calculation
        indexToNaN = lowest.index[0]
    #NaN out the value so now it's replaced in the table
    row[indexToNaN] = nan
    #for good measure, return the row as well
    return row

homeworkADropped = homeworkA.apply(remove_lowest, axis=1)
homeworkBDropped = homeworkB.apply(remove_lowest, axis=1)

meanDroppedHomeworkA = pd.DataFrame(homeworkADropped.mean(axis=1))
meanDroppedHomeworkB = pd.DataFrame(homeworkBDropped.mean(axis=1))

lessonsADropped = lessonsA.apply(remove_lowest, axis=1)
lessonsBDropped = lessonsB.apply(remove_lowest, axis=1)

meanDroppedLessonsA = pd.DataFrame(lessonsADropped.mean(axis=1))
meanDroppedLessonsB = pd.DataFrame(lessonsBDropped.mean(axis=1))

quizzesADropped = quizzesA.apply(remove_lowest, axis=1)
quizzesBDropped = quizzesB.apply(remove_lowest, axis=1)

meanDroppedQuizzesA = pd.DataFrame(quizzesADropped.mean(axis=1))
meanDroppedQuizzesB = pd.DataFrame(quizzesBDropped.mean(axis=1))

testsADropped = testsA.apply(remove_lowest, axis=1)
testsBDropped = testsB.apply(remove_lowest, axis=1)

meanDroppedTestsA = pd.DataFrame(testsADropped.mean(axis=1))
meanDroppedTestsB = pd.DataFrame(testsBDropped.mean(axis=1))

finalADropped = finalA.apply(remove_lowest, axis=1)
finalBDropped = finalB.apply(remove_lowest, axis=1)

meanDroppedFinalA = pd.DataFrame(finalADropped.mean(axis=1))
meanDroppedFinalB = pd.DataFrame(finalBDropped.mean(axis=1))

course_grade_Dropped_A = meanDroppedLessonsA*lessonWeight + meanDroppedHomeworkA*homeworkWeight + meanDroppedQuizzesA*quizWeight \
                 + meanDroppedTestsA*testWeight + meanDroppedFinalA*finalWeight

course_grade_Dropped_B = meanDroppedLessonsB*lessonWeight + meanDroppedHomeworkB*homeworkWeight + meanDroppedQuizzesB*quizWeight \
                 + meanDroppedTestsB*testWeight + meanDroppedFinalB*finalWeight

course_grade_Dropped_A.columns = ['Final Grade']
course_grade_Dropped_B.columns = ['Final Grade']

meanDroppedFinalA.columns = ['Finals']
meanDroppedFinalB.columns = ['Finals']
meanDroppedTestsA.columns = ['Tests']
meanDroppedTestsB.columns = ['Tests']
meanDroppedQuizzesA.columns = ['Quizzes']
meanDroppedQuizzesB.columns = ['Quizzes']
meanDroppedHomeworkA.columns = ['Homeworks']
meanDroppedHomeworkB.columns = ['Homeworks']
meanDroppedLessonsA.columns = ['Lessons']
meanDroppedLessonsB.columns = ['Lessons']

dropped_averages_A = pd.concat([meanDroppedLessonsA, meanDroppedHomeworkA, meanDroppedQuizzesA, meanDroppedTestsA, meanDroppedFinalA, course_grade_Dropped_A], axis=1)
dropped_averages_B = pd.concat([meanDroppedLessonsB, meanDroppedHomeworkB, meanDroppedQuizzesB, meanDroppedTestsB, meanDroppedFinalB, course_grade_Dropped_B], axis=1)

print 'A section mean grades'
print averages_A.mean()
print '\n\nA section mean grades with dropped grades for each category'
print dropped_averages_A.mean()

print '\n\nB section mean grades'
print averages_B.mean()
print '\n\nB section mean grades with dropped grades for each category'
print dropped_averages_B.mean()

print '\n\nA section grades'
print averages_A
print '\n\nA section grades with dropped grades for each category'
print dropped_averages_A

print '\n\nB section grades'
print averages_B
print '\n\nB section grades with dropped grades for each category'
print dropped_averages_B
#Dropping the lowest grade in each category for each student seemed to result in about a 5-7 point increase in the final
# grade of each student, as well as an approximate 3-5 point increase for the whole class


#part C
'''
In general, the data from the student grade implied that there was generally about 3 or 4 levels of understanding.
    1) The student understood everything very well, and got A's on virtually every assignment
    2) The student understood everything for the most part, but often acheived B's on any given assignment
    3) The student barely managed to scrape by, and might not have understood the topics completely, earning C's on most assignments
    4) The student failed, often receiving failing grades, or simply not turning in assignments

    This is actually pretty interesting, as it seems that the way the students did on any given assignment seemed to have
    a fairly strong association to how they did in the class overall, with a few exceptions (i.e. a student bunking one
    assignment, etc.) That being said, this would imply that the way the assignments are structured, at least, in terms
    of difficulty are actually ideal, granted, this speaks nothing to how well the assignments actually help the students
    learn the material. For all we know, they were in a Literature class and did Calculus of well-measured rigor.
'''