class Solution(object):
    def removeKdigits(self, num, k):
        stack = []
        for digit in num:
            while stack and k > 0 and stack[-1] > digit:
                stack.pop()
                k -= 1
            stack.append(digit)
        
        # Remove remaining digits from end if needed
        stack = stack[:-k] if k else stack
        
        # Remove leading zeros
        result = ''.join(stack).lstrip('0')
        
        return result if result else "0"
