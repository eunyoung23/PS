class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        dict=defaultdict()
        result=0
        left=0
        right=0
        
        for num in nums:
            if num in dict:
                pass
            else:
                if num-1 in dict:
                    left=dict[num-1]
                else:
                    left=0
                
                if num+1 in dict:
                    right=dict[num+1]
                else:
                    right=0
                
                sum=left+right+1
                result=max(result,sum)
                
                dict[num]=sum
                dict[num-left]=sum
                dict[num+right]=sum
                
        return result
