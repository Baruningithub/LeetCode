# class Solution:
#     def distanceTraveled(self, mainTank: int, additionalTank: int) -> int:
#         # additional = min(additionalTank, mainTank // 5)
#         # ans = (mainTank + additional) * 10
#         # return ans
#         total = 0
#         while additionalTank > 0 and mainTank >= 5:
#             mainTank -= 4
#             additionalTank -= 1
#             total += 5

#         total += mainTank
#         return total*10

class Solution:
    def distanceTraveled(self, mainTank: int, additionalTank: int) -> int:
        distance = mainTank*10
        maxRefils = (mainTank-1)//4
        distance += min(maxRefils,additionalTank)*10
        return distance
