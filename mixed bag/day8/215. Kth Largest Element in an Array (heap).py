class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        
        heapq.heapify(nums)
        
        for i in range(0, len(nums) - k):
            heapq.heappop(nums)
            
        return nums[0]
