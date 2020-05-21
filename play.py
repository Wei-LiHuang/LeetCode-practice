def sort(arr):
  N = len(arr);
  for i in range(N): #outer loop
    print(i)
    for j in range(N-1, i, -1):
        print (j)
        if arr[j] < arr[j-1]:
            #swaps two elements
            arr[j], arr[j-1] = arr[j-1], arr[j]

    print (arr)

        
arr = [3, 2, 2 ,9, 4, 3, 2, 4]

sort(arr)

