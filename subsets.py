class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        set_size = len(nums)
        size = int(math.pow(2,set_size))
        res = []
        for i in range(size):
            temp = []
            for j in range(set_size):
                if i & (1<<j):
                    # print(nums[j])
                    temp.append(nums[j])
            res.append(temp)
            # print("\n")
        return res
        
