def maxArea(height):
        answer = min(height)
        for c, i in enumerate(height):
            for d, j in enumerate(height[c+1:]):
                if min(i, j) * (d+1) > answer:
                    answer = min(i, j) * (d+1)
        return answer
