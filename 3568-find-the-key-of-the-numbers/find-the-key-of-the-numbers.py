class Solution:
    def generateKey(self, num1: int, num2: int, num3: int) -> int:
        numbers = [num1, num2, num3]
        formatted_numbers = [str(num).zfill(4) for num in numbers]
        result = [] 

        for i in range(4):
            result.append(min(formatted_numbers[0][i], formatted_numbers[1][i], formatted_numbers[2][i]))
        return int("".join(result))