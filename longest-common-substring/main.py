import sys

def lcs(s1, s2, depth=0):
    print('%s[%s] vs [%s]' % ('\t'*depth, s1, s2))
    if s1 == '' or s2 == '':
        return 0
    if s1[0] == s2[0]:
        return 1 + lcs(s1[1:], s2[1:], depth+1)
    return max(lcs(s1[1:], s2, depth+1), lcs(s1, s2[1:], depth+1))

def fast_lcs(s1, s2):
    def fast_lcs_helper(s1, s2, memo):
        if (s1, s2) in memo:
            return memo[(s1, s2)]

        if s1 == '' or s2 == '':
            result = 0
        elif s1[0] == s2[0]:
            result = 1 + fast_lcs_helper(s1[1:], s2[1:], memo)
        else:
            result = max(fast_lcs_helper(s1[1:], s2, memo), fast_lcs_helper(s1, s2[1:], memo))
        memo[(s1, s2)] = result
        return result

    return fast_lcs_helper(s1, s2, {})

def fast_lcs_values(s1, s2):
    def fast_lcs_helper(s1, s2, memo):
        if (s1, s2) in memo:
            return memo[(s1, s2)]

        if s1 == '' or s2 == '':
            result = ''
        elif s1[0] == s2[0]:
            result = s1[0] + fast_lcs_helper(s1[1:], s2[1:], memo)
        else:
            l = fast_lcs_helper(s1[1:], s2, memo)
            r = fast_lcs_helper(s1, s2[1:], memo)
            result = l if len(l) > len(r) else r
        memo[(s1, s2)] = result
        return result

    result = fast_lcs_helper(s1, s2, {})
    return (len(result), result)

def fast_lcs_increasing(s1, s2):
    def fast_lcs_helper(s1, s2, memo, c = '\0'):
        if (s1, s2) in memo:
            return memo[(s1, s2)]

        if s1 == '' or s2 == '':
            result = ''
        elif s1[0] == s2[0] and ord(s1[0]) > ord(c):
            result = s1[0] + fast_lcs_helper(s1[1:], s2[1:], memo, s1[0])
        else:
            l = fast_lcs_helper(s1[1:], s2, memo, c)
            r = fast_lcs_helper(s1, s2[1:], memo, c)
            result = l if len(l) > len(r) else r
        memo[(s1, s2)] = result
        return result

    result = fast_lcs_helper(s1, s2, {})
    return (len(result), result)

def increasing_chars(s, c = '\0'):
    if s == '':
        return ''
    if ord(s[0]) >= ord(c):
        return s[0] + increasing_chars(s[1:], s[0])
    return increasing_chars(s[1:], c)

#print(lcs('typewriter', 'typerwipe'))
print(fast_lcs_increasing('typewriter', 'typerwipe'))
print(increasing_chars('abxzyced'))
