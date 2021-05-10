astro_jokes = """
1. A Higgs boson goes into a church and the priest says,
"We don't allow Higgs bosons here." And the Higgs boson says, "But without me there is no mass."

2. A photon walks into a bar and orders a drink.
The bartender says, "Do you want a double?"
And the photon says, "No I'm traveling light."

3. I was up all night wondering where the sun had gone ... then it dawned on me.

4. Never trust an atom because they make up everything.

5. Two atoms bump into each other. One says "I've lost an electron."
"Are you sure?"
"Yes, I'm positive."

6. How does the man in the moon cut his hair?
Eclipse it.

7. A neutron goes into a bar and asks the bartender,
"How much for a beer?"
The bartender replies,
"For you, no charge."

8. The speed of time is one second per second.
"""

import collections

def wcount(n=5):
    words = astro_jokes.split()
    word_count = collections.Counter(words)
    print("Top {0} words".format(n))
    for word, count in word_count.most_common(n):
        print("{0}:{1}".format(word,count))

if __name__ == "__main__":
    n = input("type in # of top items to print : ")
    wcount(int(n))
