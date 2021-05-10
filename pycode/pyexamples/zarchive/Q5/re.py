# For example with the following string:
# We want to split the string with three delimiters: '?', '!', and '.'
S = '''Is life a joke? Does it not make you cry? Life is not a joke! My be or may be not at all.'''

def solution(S):
    import re
    sentences = re.split(r'[.!?]', S)
    print(sentences)

    mx = 0
    for sn in sentences:
        mx = max (mx, len(sn.split()))
    return mx


print(solution(S))
