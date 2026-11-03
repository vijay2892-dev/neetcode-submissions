class Solution:
    def isPalindrome(self, s: str) -> bool:
        sws = s.replace(" ", "")
        onlystring = ''
        for i in sws:
            if i.isalnum():
                i = i.lower()
                onlystring = onlystring + i

        rs = ''
        for s in onlystring: 
            rs = s+rs
        if onlystring == rs:
            return True
        else:
             return False