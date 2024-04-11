from typing import List
            
def twoSum(nums: List[int], target: int) -> List[int]:
    q_idx = [[]]
    q = [[[], -1]]
    while len(q)!=0:
        l, idx = q.pop(0)
        tmp = q_idx.pop(0)
        if idx+1<len(nums) and sum(l) + nums[idx+1] == target:
            tmp.append(idx+1)
            return tmp
        if idx+1 < len(nums):
            q_idx.append(tmp.copy())
            q.append([l.copy(),idx+1])
            if sum(l) + nums[idx+1] < target:
                tmp.append(idx+1)
                l.append(nums[idx+1])
                q_idx.append(tmp)
                q.append([l,idx+1])
        
            
if __name__=="__main__":
    print(twoSum([2,7,11,15],9))
    print(twoSum([3,2,4],6))
    print(twoSum([3,3],6))