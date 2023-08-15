class palindrome:
    def solution(nums):
        start = 0
        end = len(nums) -1
        while start < end:
            if nums[start] == nums[end]:
                start += 1
                end -= 1
            else:
                return False
        return True

print(palindrome.solution("abc"))