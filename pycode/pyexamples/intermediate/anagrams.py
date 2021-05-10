# list of anagrams from list of words

words = ['fired', 'alert', 'remain', 'alter', 'allergy', 'gallery',
         'abets', 'baste', 'fried', 'beast', 'beats']

words_dict = {w:''.join(sorted(w)) for w in words}
print(words_dict)

anagram_dict={v: [] for k,v in words_dict.items()}
print(anagram_dict)

for k,v in words_dict.items():
    anagram_dict[v].append(k)

print(anagram_dict)
