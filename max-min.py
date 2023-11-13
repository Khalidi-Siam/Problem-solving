## https://practice.geeksforgeeks.org/problems/max-min/1?utm_source=gfg&utm_medium=article&utm_campaign=bottom_sticky_on_article
class Solution:
    def findSum(self,A,N): 
        #code here
        min = 0
        max = 0
        for i in range(1, N):
            if(A[i] < A[min]):
                min = i
            if(A[i] > A[max]):
                max = i
                
        return A[min] + A[max]
