n = int(input("ピラミッドの段数を入力してください。"))
for i in range(1, n + 1):
    print(" " * (n - i) + "*" * (2 * i - 1))
