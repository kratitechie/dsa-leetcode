class Solution:
    def dailyTemperatures(self, temperatures):
        stack = []
        result = [0] * len(temperatures)

        for i in range(len(temperatures)):
            while stack and temperatures[i] > temperatures[stack[-1]]:
                prev_index = stack.pop()
                result[prev_index] = i - prev_index

            stack.append(i)

        return result


# 👇 THIS PART RUNS YOUR FUNCTION
temps = [73, 74, 75, 71, 69, 72, 76, 73]

sol = Solution()
answer = sol.dailyTemperatures(temps)

print(answer)
