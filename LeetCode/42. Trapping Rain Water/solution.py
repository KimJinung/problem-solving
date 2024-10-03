class Solution:
    def trap(self, height: List[int]) -> int:
        stack = []
        check_point = height[0]
        trapped_rain_water = 0

        for wall in height:
            stack.append(wall)

            if wall >= check_point:
                trapped_rain_water += Solution.calcul_trapped_water(stack)
                stack = [wall]
                check_point = wall
        
        
        if len(stack) > 2:
            stack.reverse()
            trapped_rain_water += self.trap(stack)
        
        return trapped_rain_water

    @staticmethod
    def calcul_trapped_water(stack: list):
        if len(stack) <= 2:
            return 0
        
        ref = min(stack[0], stack[-1])
        water = 0
        
        for wall in stack[1:-1]:
            water += ref - wall

        return water    