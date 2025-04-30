# Non-Regular Languages and Context Free Grammars: Pumping lemma for regulargrammars, Context-Free Grammars (CFG),

import re
from collections import defaultdict

# 1. **Pumping Lemma for Regular Languages**

def pumping_lemma_for_regular(language):
    """
    Using the pumping lemma to prove a language is not regular.
    This is a simplified version of the pumping lemma proof.
    We assume that a regular language should have a pumping length `p`.
    """
    # Let's consider a language L = {a^n b^n | n ≥ 0}, which is non-regular.
    # If L were regular, there would be a pumping length p.
    # We pick a string "a^p b^p" that belongs to L.
    
    p = 3  # let's take a small p for simplicity (normally it's large)
    string = 'a' * p + 'b' * p  # String is "aaabbb" for p=3
    
    print(f"\nPumping Lemma Test for Regular Language:")
    print(f"Consider the string '{string}' of length >= p (p={p})")

    # We attempt to divide the string into three parts: xyz
    # So, for some division of the string, where the middle part (y) can be pumped.
    x = 'a' * 2
    y = 'a' * 1
    z = 'b' * 3

    print(f"x = '{x}', y = '{y}', z = '{z}' (y should be pumped)")

    # Try pumping the middle part y (i.e., repeat y any number of times)
    pumped_strings = [x + (y * i) + z for i in range(1, 4)]
    for pumped in pumped_strings:
        print(f"Pumped string: '{pumped}'")
        # If pumped string has unequal number of a's and b's, it should not belong to the language.
        if pumped.count('a') != pumped.count('b'):
            print(f"Rejected: '{pumped}' doesn't belong to the language!")
        else:
            print(f"Accepted: '{pumped}' belongs to the language!")

# Test the Pumping Lemma for Regular Languages
pumping_lemma_for_regular("a^n b^n")


# 2. **Context-Free Grammar (CFG)**
# Example of Context-Free Grammar for palindrome generation.

class CFG:
    def __init__(self):
        self.rules = defaultdict(list)
    
    def add_rule(self, non_terminal, production):
        self.rules[non_terminal].append(production)
    
    def generate(self, start_symbol, depth=3):
        """Generates a string using the CFG rules."""
        if depth == 0:
            return ""
        production = self.rules.get(start_symbol, [])
        if not production:
            return start_symbol  # if no production, return the non-terminal itself
        rule = production[0]  # Let's take the first rule for simplicity
        result = ""
        for symbol in rule:
            result += self.generate(symbol, depth-1)
        return result

# Define a simple CFG for generating palindromes
cfg = CFG()

# Palindrome grammar: S -> aSa | bSb | ε
cfg.add_rule("S", ["a", "S", "a"])
cfg.add_rule("S", ["b", "S", "b"])
cfg.add_rule("S", [""])  # ε (empty string)

# Generate a palindrome using CFG
generated_string = cfg.generate("S", depth=4)
print("\nGenerated Palindrome using CFG:", generated_string)


# 3. **Proving Non-Regularity using Pumping Lemma**

# Let's consider the language L = {a^n b^n | n ≥ 0}, a non-regular language.
# We will use the pumping lemma to show that this language is not regular.

def is_regular_language(language):
    """This is just a placeholder. Normally we would apply the pumping lemma to prove non-regularity."""
    print("\nChecking regularity for L = {a^n b^n | n >= 0} using the Pumping Lemma:")
    # The language a^n b^n is known to be non-regular (proved using the pumping lemma)
    print("This language is **NOT** regular as shown by the pumping lemma.")
    
# Testing non-regularity using the pumping lemma
is_regular_language("a^n b^n")


# 4. **Context-Free Grammar Examples**
# A language that is **context-free** but **not regular** is L = {a^n b^n | n ≥ 0}.
# We will now define a CFG for this language.

def context_free_grammar():
    print("\nContext-Free Grammar for L = {a^n b^n | n >= 0}:")
    print("S -> aSb | ε")

context_free_grammar()

# Now let's test the CFG with strings.
test_strings = ["", "ab", "aabb", "aaabbb"]
print("\nTesting CFG for L = {a^n b^n | n >= 0}:")

def test_cfg(strings):
    for string in strings:
        # Simple check for the string format a^n b^n
        if re.match(r"^a*b*$", string) and string.count('a') == string.count('b'):
            print(f"'{string}' is a valid string for the CFG!")
        else:
            print(f"'{string}' is **not** valid for the CFG!")

test_cfg(test_strings)


