#two sum
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen={}
        for i in range(len(nums)):
            needed =target-nums[i]
            if needed in seen:
                return [seen[needed],i]
            seen[nums[i]]=i    


#koko eating banana
class Solution:
    def minEatingSpeed(self, piles: list[int], h: int) -> int:
        low = 1
        high = max(piles)
        best_speed = high
        while low <= high:
            speed = (low + high) // 2
            totalHours = 0
            for pile in piles:
                totalHours += (pile + speed - 1) // speed 
            if totalHours <= h:
                best_speed = speed
                high = speed - 1    
            else:
                low = speed + 1    
        return best_speed            