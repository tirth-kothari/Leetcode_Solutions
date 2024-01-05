class Solution:
	def lengthOfLIS(self, nums: List[int]) -> int:
		result = [1]
		for i in range(1, len(nums)):
			current_length = 1
			for j in range(i):
				if nums[i] > nums[j]:
					current_length = max(current_length, 1 + result[j])
			result.insert(i, current_length)
		return max(result)
