class Solution(object):
   def lengthOfLongestSubstring(self, s):
      i, j, d, ans = 0, 0, {}, 0

      while j < len(s):
         if s[j] not in d or i > d[s[j]]:
            ans = max(ans,(j-i+1))
            d[s[j]] = j
         else:
            i = d[s[j]]+1
            ans = max(ans,(j-i+1))
            j-=1

         #print(ans)
         j+=1
      return ans

obj = Solution()
print(obj.lengthOfLongestSubstring("ABCABCBB"))
#print(obj.lengthOfLongestSubstring("BBB"))
