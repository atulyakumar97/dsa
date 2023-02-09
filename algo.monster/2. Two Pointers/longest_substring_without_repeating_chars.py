# def longest_substring_without_repeating_characters(s: str) -> int:
#     set solution
#     seen = set()
#     i = 0
#     max_sub = 0
#
#     for j in range(len(s)):
#
#         if s[j] not in seen:
#             seen.add(s[j])
#         else:
#
#             while s[i] != s[j]:
#                 seen.remove(s[i])
#                 i += 1
#
#             if s[i] == s[j]:
#                 i += 1
#
#         max_sub = max(max_sub, j - i + 1)
#     return max_sub

def longest_substring_without_repeating_characters(s: str) -> int:
    # hm solution
    seen = set()
    i = 0
    max_sub = 0

    for j in range(len(s)):

        if s[j] not in seen:
            seen.add(s[j])
        else:

            while s[i] != s[j]:
                seen.remove(s[i])
                i += 1

            if s[i] == s[j]:
                i += 1

        max_sub = max(max_sub, j - i + 1)
    return max_sub


if __name__ == '__main__':
    s = input()
    res = longest_substring_without_repeating_characters(s)
    print(res)
