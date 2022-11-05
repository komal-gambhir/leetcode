class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        
        countoccurence = Counter(nums)
        
        majorityoccurence= int(len(nums)/2)
        
        maxkey = 0 
        
    # n is the key in the counter and countoccurence[n] will be the value of n      
        
        for n in countoccurence:
            
            if countoccurence[n] > majorityoccurence:
                
                majorityoccurence = countoccurence[n]
                
                maxkey = n 
                
                
        return maxkey
            
            
            
            
            
        
       
        