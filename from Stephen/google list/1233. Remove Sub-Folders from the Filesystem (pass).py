class Solution:
    def removeSubfolders(self, folder: List[str]) -> List[str]:
        
        folder.sort()        
        #print(folder)        
        s = set()
        for f in folder:            
            isSub = False
            for i in range(0, len(f)):
                if f[i] != '/':                           
                    if i == len(f) - 1 or f[i + 1] == '/':                    
                        if f[0:i + 1] in s:
                            isSub = True
                            break
            if isSub == False:
                s.add(f)
                
        return list(s)
                        
