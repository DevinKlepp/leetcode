class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if(len(s) < len(t) or len(t) == 0):
            return ""
        
        ht = Counter(t)
        req = len(ht)
        
        filt = [] # Filtered list of items
        for i, char in enumerate(s):
            if(char in ht):
                filt.append([i, char])
                
        l, r = 0, 0
        formed = 0
        window = {}
        
        # Tuple containing info
        ans = float("inf"), None, None
        
        while(r < len(filt)):
            c = filt[r][1]
            window[c] = window.get(c, 0) + 1 # Adds one if exists, else adds 0 and 1
            
            if(window[c] == ht[c]): # If we have matched the ammount of said character required in t
                formed += 1
            
            while(l <= r and formed == req): # While t is in current window
                c = filt[l][1] # Gets first element
                
                # Save if smallest
                if(filt[r][0] - filt[l][0] + 1 < ans[0]): # If current length is less than answer
                    ans = (filt[r][0] - filt[l][0] + 1, filt[l][0], filt[r][0])
                    
                window[c] -= 1 # Moving left index right
                if(window[c] < ht[c]): # If number of specific char in window is less than needed,
                    formed -= 1        # Take one from formed
                l += 1
            r += 1
        return "" if ans[0] == float("inf") else s[ans[1]: ans[2] + 1]
            