class Solution:
    def missingNumber(self, nums: List[int]) -> int:
       # Take the sum of array and substract it from the total of the natural numbers from 1 to #array length + 1 because length takes less than the last number so we did +! 
        total=sum(nums)
        print(total)
        #sum of first natural postive numner 1,2,3,4.....
        sumofn=0
        for i in range(1,len(nums)+1):
            sumofn+=i
            output= sumofn-total
            #index = nums.index(0)
           # print(index)
        return output
            
                
                
        
        