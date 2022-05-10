if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().split()))
    
    arr.sort()
    i=0
    while i<n:
        if arr[-i-1]==arr[-i-2]:
            arr.pop()
        else:
            break
    print(arr[-2])
