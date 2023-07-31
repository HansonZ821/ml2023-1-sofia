Python 3.11.4 (tags/v3.11.4:d2340ef, Jun  7 2023, 05:45:37) [MSC v.1934 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> def find_x_from_n(N, numbers, X):
...     for i in range(N):
...         if numbers[i] == X:
...             return i + 1
...     return -1
... 
... if __name__ == "__main__":
...     N = int(input("Enter the number of elements (N): "))
...     numbers = []
...     for i in range(N):
...         num = int(input(f"Enter number {i + 1}: "))
...         numbers.append(num)
... 
...     X = int(input("Enter the number to search (X): "))
...     index = find_x_from_n(N, numbers, X)
...     
...     if index == -1:
...         print(f"{X} was not found among the input numbers.")
...     else:
