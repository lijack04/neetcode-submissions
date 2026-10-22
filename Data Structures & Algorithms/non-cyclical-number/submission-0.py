class Solution:
    def isHappy(self, n: int) -> bool:
        checked = set()

        while n != 1:
            stringn = str(n)
            n = 0
            for c in stringn:
                n += int(c)**2
            print(n)
            print(checked)
            if n in checked:
                return False
            checked.add(n)
        
        return True