MAX=20
from classifyDT import *
from classifyRF import *
from classifySVM import *

accuracy=0
for x in range(MAX):
    accuracy = accuracy + SVM()
accuracy/=MAX
print "SVM = ",accuracy
accuracy=0
for x in range(MAX):
    accuracy = accuracy + DT()
accuracy/=MAX
print "DT = ",accuracy
accuracy=0
for x in range(MAX):
    accuracy = accuracy + RF()
accuracy/=MAX
print "RF = ",accuracy
print "I conclude that SVM can work perfectly for smaller training sets while Random Forest"
" and Decision Tree do not"
