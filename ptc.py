import math
import os
import random
import re
import sys
# Complete the 'organizingContainers' function below.
# The function is expected to return a STRING.
# The function accepts 2D_INTEGER_ARRAY container as parameter.
def organizingContainers(container):
    # Write your code here
    arr1 = []
    arr2 = []
    for i in range(len(container)):
        arr1.append(sum(container[i]))
    for i in range(len(container)):
        sm = 0
        for j in range(len(container)):
            sm += container[j][i]
        arr2.append(sm)
    if(sorted(arr1) == sorted(arr2)):
        return 'Possible'
    else:
        return 'Impossible'   
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')
    q = int(input().strip())
    for q_itr in range(q):
        n = int(input().strip())
        container = []
        for _ in range(n):
            container.append(list(map(int, input().rstrip().split())))
        result = organizingContainers(container)
        fptr.write(result + '\n')
    fptr.close()
