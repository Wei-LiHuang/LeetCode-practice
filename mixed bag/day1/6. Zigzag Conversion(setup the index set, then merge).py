# output string will be the same length
# row: one to len(s)

# bruteforce:
# create r rows, r == numRows
# PAYPALISHI
# 0123456789

# 0   4   8
#  1 3 5 7 9
#   2   6

class Solution:    
    
    # create index set, move each index to there places, no merge
    def convert2(self, s: str, r: int) -> str:
        
        if r <= 1:
            return s
        
        indexSet = []
        for i in range(0, r):
            indexSet.append([i])
        
        cur = r - 2
        for i in range(r, r + r - 2):                        
            indexSet[cur].append(i)
            cur -= 1
            
        res = ""
        for indices in indexSet:
            stillHaveC = True
            while stillHaveC:
                stillHaveC = False
                for i in range(0, len(indices)):
                    if indices[i] < len(s):
                        res += s[indices[i]]
                        indices[i] += (2 * r - 2)
                        if indices[i] < len(s):
                            stillHaveC = True
        
            
            
        
        return res

    # create index set, get each str, merge
    def convert(self, s: str, r: int) -> str:
        
        if r <= 1:
            return s
        
        sequence = []
        for i in range(0, r):
            sequence.append(i)            
        for i in range(r - 2, 0, -1):
            sequence.append(i)
            
        arr = []
        for i in range(0, r):
            arr.append("")
        
        seq = 0
        for c in s:
            arr[sequence[seq]] += c
            seq += 1
            if seq == len(sequence):
                seq = 0
            
            
        res = ""
        for a in arr:
            res += a
            
        return res    
    
  
