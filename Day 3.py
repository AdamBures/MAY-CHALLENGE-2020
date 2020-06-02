class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        g=0;
        for i in ransomNote:
            s=ransomNote.count(i);
            h=magazine.count(i);
            if(s>h):
                g+=1;
        if(g==0):
            return True;
        else:
            return False;
