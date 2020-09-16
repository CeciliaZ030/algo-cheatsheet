def canJump(nums) -> bool:
    
    L = len(nums)
    T = [False] * L
    T[0] = True
    
    for i in range(1, L):
        print(i, nums[i])
        for j in range(i - 1, -1, -1):
            print(" ", j, nums[j], i - j <= nums[j], T[j])
            if T[j] and i - j <= nums[j]:
                T[i] = True
                break
        print(T)
 
    return T[L- 1]


canJump([2,3,1,1,4])