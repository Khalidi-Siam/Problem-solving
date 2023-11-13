# https://www.geeksforgeeks.org/sort-an-array-of-0s-1s-and-2s/
class Solution:
    def sort012(self,arr,n):
        # code here
        new_arr = [0,0,0]
        pos = 0
        for i in range(n):
            new_arr[arr[i]] += 1
            
        for i in range(3):
            for j in range(new_arr[i]):
                arr[pos] = i
                pos += 1
                
        return arr
