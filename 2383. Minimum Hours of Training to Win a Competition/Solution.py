class Solution:
    def minNumberOfHours(self, initialEnergy: int, initialExperience: int, energy: List[int], experience: List[int]) -> int:
        req_energy = sum(energy) + 1
        ans = 0
        temp = 0
        if req_energy >= initialEnergy:
            ans = ans + req_energy - initialEnergy
        for i in experience:
            if initialExperience <= i:
                temp = i - initialExperience + 1
                initialExperience = initialExperience + temp
                ans = ans + temp
                initialExperience = initialExperience + i
                temp = 0
            else:
                initialExperience+=i
        return ans
