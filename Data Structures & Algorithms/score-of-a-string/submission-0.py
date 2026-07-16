class Solution:
    def scoreOfString(self, s: str) -> int:
        Asc_l = []
        s_l=[]
        for i in s:
            Asc_l.append(ord(i))
        length = len(Asc_l)
        cnt = 0
        while cnt<=length-2:
            s_l.append(abs(Asc_l[cnt] - Asc_l[cnt+1]))
            cnt+=1
        return sum(s_l)


            



        