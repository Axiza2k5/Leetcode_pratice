class Solution:
    def minimumTotal(self, triangle) -> int:
        values = []
        values.append([triangle[0][0]])
        for i in range(1,len(triangle)):
            values.append([])
            values[i].append(triangle[i][0]+ values[i-1][0])
            for j in range(1,len(triangle[i])-1):
                values[i].append(min(triangle[i][j]+values[i-1][j-1],triangle[i][j]+values[i-1][j]))
            values[i].append(triangle[i][-1] + values[i-1][-1])

        return min(values[-1])
