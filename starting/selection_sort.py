class Solution: 
    def select(self, arr, i):
        # code here
        return arr[i]
    
    def selectionSort(self, arr,n):
        #code here
        for i in range (len(arr)):
            min = i
            for j in range (i+1, len(arr)):
                if arr[min]>arr[j]:
                    min = j
            arr[i], arr[min] = arr[min], arr[i]
