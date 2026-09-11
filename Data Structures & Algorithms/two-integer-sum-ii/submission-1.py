class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:

        n = len(numbers)
        debut, fin = 0, n-1 

        while numbers[debut] + numbers[fin] != target : 
            if numbers[debut] + numbers[fin] > target :
                fin -= 1
            else : 
                debut += 1 

        return [debut+1, fin+1]


        
        
            
        