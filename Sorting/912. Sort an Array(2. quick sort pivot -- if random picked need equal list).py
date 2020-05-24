# use random -> need qeual list or it will endless recursive --> why?

class Solution:
    
    def rec(self, lst):
        
        n = len(lst)
        if n <= 1:
            return lst
        elif n == 2:
            return [min(lst[0], lst[1]), max(lst[0], lst[1])]
        else:            
            l = []
            r = []
            e = []
            pivot = random.choice(lst)
            for i in lst:
                if i > pivot:
                    r.append(i)
                elif i == pivot:
                    e.append(i)
                else:
                    l.append(i)
                    
            l = self.rec(l)
            r = self.rec(r)
            
            return l + e + r
            
            
        
    
    def sortArray(self, a: List[int]) -> List[int]:
        
        return self.rec(a)
        
        
