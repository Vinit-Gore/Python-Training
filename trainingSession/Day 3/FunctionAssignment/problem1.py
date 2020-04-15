import inspect


def get_num_args(f):
    return len(inspect.getargspec(f)[0])


List = {}
m = 10
for i in range(1, m+1):
    List[i] = [[i, i+1, i+2]]


def summation(List):
    print(List)
    outputlist = []
    for count in range(1, m+1):
        for (i, _) in enumerate(List[count]):
            print("List count:", List[count])
            print("List i :", List[count][i])
            listsum = []
            for (index, _) in enumerate(List[count][i]):
                sum = List[count][i][index] + \
                    List[count][i][index]+List[count][i][index]
                listsum.append(sum)
                print(listsum)
            outputlist.append(listsum)
        return outputlist


print(summation(List))
