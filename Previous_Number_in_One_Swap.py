def solve(s):
    n= len(s)
    arr = list(s)
    flag = False
    for i in range(n-1):
        if arr[i] <= arr[i+1]:
            continue
        else:
            Flag = True
            break
    if flag:
        return -1
    idx = None
    for i in range(n-1,0,-1):
        if arr[i-1] > arr[i]:
            idx = i-1
            break
    if idx == None:
        return -1
    temp = '-999999'
    for j in range(n-1,idx,-1):
        if arr[j] < arr[idx]:
            if arr[j] >= temp:
                idx2 = j
                temp = arr[idx2]
    arr[idx],arr[idx2] = arr[idx2],arr[idx]
    ans = ''.join(arr)
    if ans[0] == '0':
        return -1
    return ans  
s=input()
print(solve(s)) 