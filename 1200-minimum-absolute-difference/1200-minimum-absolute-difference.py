class Solution(object):
    def minimumAbsDifference(self, arr):
        arr.sort()
        result=float('inf')
        for i in range(1,len(arr)):
            
            result=min(result,arr[i]-arr[i-1])
        res=[]
        for i in range(len(arr)):
            if arr[i]-arr[i-1]==result:
                res.append([arr[i-1],arr[i]])

        return res
        