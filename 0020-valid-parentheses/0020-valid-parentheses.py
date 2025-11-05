class Solution(object):
    def isValid(self, s):
        stk=[]
        matching={')':'(','}':'{',']':'['}
        for ch in s:
            if ch in '({[':
                stk.append(ch)
            else:
                if not stk :
                    return False 
                if stk[-1] == matching[ch]:
                    stk.pop()
                else:
                    return False
        return len(stk) == 0                    
        