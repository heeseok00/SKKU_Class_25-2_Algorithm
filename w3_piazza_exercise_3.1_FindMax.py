
def find_max(nums):
    max_val = 0
    for n in nums:
        if n > max_val:
            max_val = n
            return max_val