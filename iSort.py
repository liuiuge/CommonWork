'''
    insert sort asc
    bubble sort asc
    select sort asc
'''
import copy
import random
import time

from commDec import tRecord


@tRecord
def InsertSort(a):
    
    for i in range(1, len(a)):
        if a[i] < a[i-1]:
            tmp = a[i]
            j = i - 1
            while j > -1 and tmp < a[j]:
                a[j+1] = a[j]
                j -= 1
            a[j+1] = tmp
    return a

@tRecord
def BubbleSort(a):
    
    for i in range(len(a)-1):
        for j in range(i+1, len(a)):
            if a[i] > a[j]:
                a[i], a[j] = a[j], a[i]
    return a

@tRecord
def SelectSort(a):
    
    for i in range(len(a) - 1):
        a_min = a[i]
        for j in range(i+1, len(a)):
            if a[j] < a_min:
                a_min = a[j]
        a[i], a[j] = a[j], a[i]
    return a

def ShellSort(a):
    step = len(a) // 2
    while step >= 1:
        for index in range(step, len(a)):
            tmp = a[index]
            j = index - step
            while j > -1 and a[j] > tmp:
                a[j+step] = a[j]
                j -= step
            a[j + step] = tmp
        step //= 2
    return a

def Partition(a, low, high):
    pivot = a[low]
    while (low < high):
        while( low < high and a[high] >= pivot):
            high -= 1
        a[low] = a[high]
        while( low < high and a[low] <= pivot):
            low += 1
        a[high] = a[low]
    a[low] = pivot
    return low

def _QuickSort(a, low, high):
    if low < high:
        pivot = Partition(a, low, high)
        _QuickSort(a, pivot + 1, high)
        _QuickSort(a, low, pivot - 1)
    

@tRecord
def QuickSort(a):
    _QuickSort(a, 0, len(a) - 1)
    return a

def AdjustDown(a, index, length):
    smallest = index
    left = 2 * index + 1
    right = 2 * (index + 1)
    if left < length and a[left] > a[index]:
        smallest = left
    if right < length and a[right] > a[smallest]:
        smallest = right
    if index != smallest:
        a[index], a[smallest] = a[smallest], a[index]
        AdjustDown(a, smallest, length)

@tRecord
def HeapSort(a):
    index = len(a) // 2
    while index > -1:
        AdjustDown(a, index, len(a))
        index -= 1
    index = len(a) - 1
    while index > -1:
        a[index], a[0] = a[0], a[index]
        AdjustDown(a, 0, index)
        index -= 1

def merge(a, low, mid, high):
    b = []
    for i in a[low:high+1]:
        b.append(i)
    m, n, l = low, mid + 1, 0
    while m <= mid and n <= high:
        if b[n-low] > b[m-low]:
            a[low+l] = b[m-low]
            m += 1
        else:
            a[low+l] = b[n-low]
            n += 1    
        l += 1
    while(m<=mid):
        a[low+l] = b[m-low]
        l += 1
        m += 1
    while(n<=high):
        a[low+l] = b[n-low]
        l += 1
        n += 1

def _mergeSort(a, low, high):
    if low < high:
        mid = (high - low) // 2 + low
        _mergeSort(a, low, mid)
        _mergeSort(a, mid + 1, high)
        merge(a, low, mid, high)

@tRecord
def MergeSort(a):
    #print(a)
    _mergeSort(a, 0, len(a) - 1)
    #print(a)

def sqrt(x):
    i = 0
    while i * i < x:
        i += 1
    return i

@tRecord
def BucketSort(a):
    k = sqrt(len(a))
    dict1 = {}
    for num in a:
        index = num // k
        tmpdict = dict1.get(index, [])
        tmpdict += [num,]
        dict1[index] = tmpdict
    for _, v in dict1.items():
        ShellSort(v)
        cnt = 0
    #print(dict1)
    for i in range(k+1):
        for num in dict1.get(i, {}):
            a[cnt] = num
            cnt += 1
    #print(a)
            
if __name__ == '__main__':
    
    
    num_sist = [6, 8, 5, 4, 3, 1, 2, 9, 7]
    formal_list = [i for i in range(30000000)]
    num_list = [random.choice(formal_list) for _ in range(1000000)]
    # n_l_i = copy.deepcopy(num_list)
    # InsertSort(n_l_i)
    # n_l_bl = copy.deepcopy(num_list)
    # BubbleSort(n_l_bl)
    # n_l_sl = copy.deepcopy(num_list)
    # SelectSort(n_l_sl)
    # n_l_sh = copy.deepcopy(num_list)
    # ShellSort(n_l_sh)
    n_l_q = copy.deepcopy(num_list)
    QuickSort(n_l_q)                # @tRecord:QuickSort  took 0:00:20.247678
    n_l_h = copy.deepcopy(num_list)
    HeapSort(n_l_h)                 # @tRecord:HeapSort  took 0:01:50.828532
    n_l_m = copy.deepcopy(num_list)
    MergeSort(n_l_m)                # @tRecord:MergeSort  took 0:01:03.437422
    n_l_bc = copy.deepcopy(num_list)
    BucketSort(n_l_bc)              # @tRecord:BucketSort  took 0:00:10.135110

