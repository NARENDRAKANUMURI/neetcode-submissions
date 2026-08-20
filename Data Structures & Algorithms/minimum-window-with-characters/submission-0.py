class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if not t or not s:
            return ""
        need={}

        for char in t:
            need[char]=need.get(char,0)+1

        window={}
        left=0
        have=0
        need_count=len(need)

        result=""
        result_length=float("inf")

        for right in range(len(s)):
            char=s[right]
            window[char]=window.get(char,0)+1

            if char in need and window[char]==need[char]:
                have+=1

            while have==need_count:
                current_length=right-left+1

                if current_length<result_length:
                    result=s[left:right+1]
                    result_length=current_length

                left_char=s[left]

                window[left_char]-=1

                if left_char in need and window[left_char]<need[left_char]:
                    have-=1
                left+=1

        return result