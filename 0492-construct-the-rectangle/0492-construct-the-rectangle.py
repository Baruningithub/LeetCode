class Solution:
    def constructRectangle(self, area: int) -> List[int]:
        sqrt = math.sqrt(area)

        w = int(sqrt)
        while (area % w):
            w-=1                
        return [area//w, w]

