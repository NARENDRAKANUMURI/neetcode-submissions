class Solution:
    def isValid(self, s: str) -> bool:
        brace_map={')':'(','}':'{',']':'['}
        push_map={'(','{','['}
        stack=[]
        for char in s:
            if char in push_map:
                stack.append(char)
            if char in brace_map.keys():
                if stack:
                    pop_char=stack.pop()
                    if pop_char==brace_map[char]:
                        continue
                    elif pop_char!=brace_map[char]:
                        return False
                if not stack:
                    return False
        return not stack