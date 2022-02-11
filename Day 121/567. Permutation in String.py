class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        nums, nums2 = [0]*26, [0]*26
        for i in s1:
            nums[ord(i)-ord('a')] += 1
        for i in range(len(s2)):
            nums2[ord(s2[i]) - ord('a')] += 1
            if i >= len(s1)-1:
                if nums == nums2: 
                    return True
                nums2[ord(s2[i-len(s1)+1])-ord('a')] -= 1
        return False
