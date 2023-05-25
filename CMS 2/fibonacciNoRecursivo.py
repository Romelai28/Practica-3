import sys


def fibonacciNoRecursivo(n: int) -> int:
    # Implementar esta funcion
    # Requiere: n >= 0
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        res = [0, 1]
        for i in range(2, n+1):
            res.append(res[i-2] + res[i-1])
        # return res  # Visualizar la succesión.
        return res[n]


if __name__ == '__main__':
  x = int(input())
  print(fibonacciNoRecursivo(x))