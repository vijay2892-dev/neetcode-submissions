class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        s = s.strip()
        s = s.split(" ")
        print(s)
        a = []
        for i in s:
            if i.isalpha():
                a.append(i)
        return len(a[-1])