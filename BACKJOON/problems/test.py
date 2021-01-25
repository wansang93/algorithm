def is_han(n):
    if n < 100:
        return True
    digit_1 = n % 10
    digit_10 = (n % 100) // 10
    digit_100 = n // 100
    if (digit_100 - digit_10) == (digit_10 - digit_1):
        return True
    return False


N = int(input())
cnt = 0
for i in range(1, N+1):
    if is_han(i):
        cnt += 1
print(cnt)
