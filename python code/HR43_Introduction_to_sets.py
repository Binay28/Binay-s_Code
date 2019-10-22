from __future__ import division

def average(array):
    # your code goes here
    #sum=0
    #for i in range(len(arr)):
     #   sum+=arr[i]
    #return (sum/len(arr))
    return (sum(set(array))/len(set(array)))
if __name__ == '__main__':
    n = int(raw_input())
    arr = map(int, raw_input().split())
    result = average(arr)
    print result
#the set function takes out the distinct elements from a list and returns a new list containing the ddistinct elements
