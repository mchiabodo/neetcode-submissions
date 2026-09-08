from collections import defaultdict
from typing import List

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # 1. Utiliser defaultdict pour éviter les KeyError
        res = defaultdict(list) 
        
        for s in strs: 
            count = [0] * 26
            
            for c in s: 
                count[ord(c) - ord('a')] += 1 
            
            # 2. Sortir cette ligne de la petite boucle (indentation corrigée)
            res[tuple(count)].append(s) 

        # 3. Ajouter le "s" à values()
        return list(res.values())

                