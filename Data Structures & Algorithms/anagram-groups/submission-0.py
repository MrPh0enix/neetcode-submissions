class Solution:

    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        groups = {}

        for str1 in strs:

            sortedstr1 = ''.join(sorted(str1))

            if sortedstr1 in groups:

                groups[sortedstr1] += [str1]
            
            else:

                groups[sortedstr1] = [str1]

        return list(groups.values())
