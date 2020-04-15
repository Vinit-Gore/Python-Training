import numpy as np

myNumpy_ID = np.arange(15)

myNumpy_ID[myNumpy_ID % 2 == 0] = myNumpy_ID[myNumpy_ID %
                                             17 == 0]*10    # allowed
myNumpy_ID[myNumpy_ID % 2 == 0] = myNumpy_ID[myNumpy_ID %
                                             4 == 0]*10  # Not allowed
myNumpy_ID[myNumpy_ID % 4 == 0] = myNumpy_ID[myNumpy_ID %
                                             2 == 0]*10  # Not allowed
print(myNumpy_ID)
