class Solution:
    def compress(self, chars: List[str]) -> int:
        cur = 0
        count = 1
        for nxt in range (1, len(chars) + 1):
            if  nxt < len(chars) and chars[nxt] == chars[nxt - 1]:
                count += 1
            else:
                chars[cur] = chars[nxt - 1]
                cur += 1
                if count > 1:
                    for i in str(count):
                        chars[cur] = i
                        cur += 1
                    count = 1
        return cur