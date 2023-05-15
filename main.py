import Memoization
import Tabulation

matrix = [[4], [1, 3], [1, 2, 1], [8, 4, 5, 1]]

print("Memoization: ")
print(Memoization.execute(matrix))
print("****************************************************")
print("Tabulation: ")
print(Tabulation.execute(matrix))
