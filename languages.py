# Languages: Alphabets, string, language, basic operations on language, concatenation, union,Kleene star

from itertools import product

# 1. **Alphabet**
# An alphabet is a finite set of symbols.
alphabet = {'a', 'b'}

# 2. **String**
# A string is a finite sequence of symbols from an alphabet.
string1 = "a"
string2 = "ab"
string3 = "ba"

# 3. **Language**
# A language is a set of strings formed over an alphabet.
language1 = {"a", "ab", "ba", "b"}
language2 = {"bb", "a", "aa"}

# 4. **Basic Operations on Languages**
# ---------------------------------------------

# **Union**: Union of two languages L1 and L2
def union(L1, L2):
    return L1.union(L2)

# **Concatenation**: Concatenate each string in L1 with each string in L2
def concatenate(L1, L2):
    return {s1 + s2 for s1 in L1 for s2 in L2}

# **Kleene Star**: Forms a new language by zero or more concatenations of strings from L
def kleene_star(L):
    star_result = {""}  # Start with the empty string
    for _ in range(5):  # Limiting to 5 repetitions for simplicity
        star_result.update({s + t for s in star_result for t in L})
    return star_result

# ---------------------------------------------

# 5. **Demonstration of Operations on Languages**
# Union of L1 and L2
union_L1_L2 = union(language1, language2)
print("Union of L1 and L2:", union_L1_L2)

# Concatenation of L1 and L2
concat_L1_L2 = concatenate(language1, language2)
print("Concatenation of L1 and L2:", concat_L1_L2)

# Kleene Star on L1
kleene_L1 = kleene_star(language1)
print("Kleene Star of L1:", kleene_L1)

# 6. **Other Operations**

# Check if a string is in a language (membership test)
def is_member(language, string):
    return string in language

print("Is 'ab' in L1?", is_member(language1, "ab"))
print("Is 'bb' in L1?", is_member(language1, "bb"))

# Check if a string is over the given alphabet
def is_valid_string(string, alphabet):
    return all(symbol in alphabet for symbol in string)

print("Is 'ab' a valid string over the alphabet?", is_valid_string("ab", alphabet))
print("Is 'abc' a valid string over the alphabet?", is_valid_string("abc", alphabet))

