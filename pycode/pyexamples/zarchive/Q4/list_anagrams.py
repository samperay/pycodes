words = ['fired', 'alert', 'remain', 'alter', 'allergy', 'gallery',
         'abets', 'baste', 'fried', 'beast', 'beats']

# Make dictionary, element of list as keys and sort values
words_dict = {w: ''.join(sorted(w)) for w in words}
print("Word Dict:",words_dict)

anagram_dict={v:[] for k,v in words_dict.items()}
print("Anagram Dict List",anagram_dict)

for k,v in words_dict.items():
    anagram_dict[v].append(k)
print("Final Anagram Dict",anagram_dict)
