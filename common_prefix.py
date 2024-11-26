class Solution:
    def longestCommonPrefix(self, strs: list[str]) -> str:

        strs.sort()
        first = strs[0]
        last = strs[-1]
        common_prefix = []
        if not strs:
            return ""
        for i in range(min(len(first), len(last))):
            if first[i] == last[i]:
                common_prefix.append(first[i])
            else:
                break
        return ''.join(common_prefix)


x = Solution()
y = ["flower", "flow", "flight"]

print(x.longestCommonPrefix(y))
