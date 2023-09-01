def printOrder(arr,n) :
    # sorting the array
    arr.sort()
  
    # printing first half in ascending
    # order
    i = 0
    while (i< n/ 2 ) :
        print(arr[i], end=" ")
        i = i + 1
         
    # printing second half in descending
    # order
    j = n - 1
    while j >= n / 2 :
        print (arr[j], end=" ")
        j = j - 1

if __name__ == "__main__" :
    n= int(input())
    arr = list(map(int,input().strip().split()))[:n]

    printOrder(arr, n)