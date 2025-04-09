class Solution:
    def digitCount(self, num: str) -> bool:
        result = True

        for i in range(len(num)):
            cnt = 0
            for char in num:
                if int(char) == i:
                    cnt += 1
            
            if cnt != int(num[i]):
                result = False
                break
        
        return result
    
# More pythonic

# from collections import Counter

# class Solution:
#     def digitCount(self, num: str) -> bool:
#         counter = Counter(num)
#         for i, digit in enumerate(num):
#             if counter[str(i)] != int(digit):
#                 return False
#         return True

        
# 문제: https://leetcode.com/problems/check-if-number-has-equal-digit-count-and-digit-value/