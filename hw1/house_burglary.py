def house_burglary(n: int, P: list[int], F: list[int]) -> int:
    dp = [0] * (n+1)

    for i in range(n-1, -1, -1):
        addendum = dp[i + F[i] + 1] if (i + F[i] + 1 <= n) else 0
        dp[i] = max(dp[i+1], P[i] + addendum)

    return dp[0]


if __name__ == "__main__":
    n = 4
    P = [50, 90, 30, 20]
    F = [1, 2, 1, 0]
    assert(house_burglary(n, P, F) == 90)
    print(house_burglary(n, P, F))

    n = 5
    P = [30, 20, 20, 10, 30]
    F = [2, 0, 1, 1, 0]
    assert(house_burglary(n, P, F) == 70)
    print(house_burglary(n, P, F))
