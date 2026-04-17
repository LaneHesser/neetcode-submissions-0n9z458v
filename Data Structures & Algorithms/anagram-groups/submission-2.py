from collections import defaultdict


class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagram_dict = defaultdict(list)
        for word in strs:
            anagram_dict[str(sorted(word))].append(word)

        return [
            anagrams
            for anagrams in anagram_dict.values()
        ]