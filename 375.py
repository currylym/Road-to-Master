def getMoneyAmount(n: int) -> int:
        
    if n == 1:
        return 0
    if n == 2:
        return 1
    if n == 3:
        return 3
        
    start = 1
    end = n
    res = 0
    while start < end:
        mid = (start+end) // 2
        res += mid
        start = mid + 1
        print(start,end)
    print(res)
    return res

if __name__ == '__main__':
    getMoneyAmount(n=3)