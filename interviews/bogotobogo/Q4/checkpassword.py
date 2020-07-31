"""
Write a code to check the validity of password input. Then following are the criteria for valid password:

At least 1 letter between [a-z]
At least 1 number between [0-9]
At least 1 letter between [A-Z]
At least 1 character from [$#@]
Minimum length of password: 6
Maximum length of password: 12
"""

import re
password = ["c#12Z","7@yE*","Zd12$a1","all4@9"]
valid={}.fromkeys(password,False)
print(valid)
for p in password:
    if len(p) < 6 or len(p) > 12:
        continue

    if not re.search('[abc]', p):
        continue

    if not re.search('[A-Z]', p):
        continue

    if not re.search('[0-9]', p):
        continue

    if not re.search("[$#@]",p):
        continue

    valid[p] = True

print(valid)
