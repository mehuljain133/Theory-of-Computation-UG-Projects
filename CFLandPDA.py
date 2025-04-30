# Context-Free Languages (CFL) and PDA: Deterministic and non-deterministic Pushdown Automata (PDA), parse trees, leftmost derivation, pumping lemma for CFL, properties of CFL.

import re
from collections import defaultdict


# 1. **Pushdown Automata (PDA)**
# A PDA has a stack in addition to states, so it can process context-free languages (CFL).

class PDA:
    def __init__(self, states, alphabet, stack_alphabet, transition_function, start_state, start_stack_symbol, accept_states):
        self.states = states
        self.alphabet = alphabet
        self.stack_alphabet = stack_alphabet
        self.transition_function = transition_function
        self.start_state = start_state
        self.start_stack_symbol = start_stack_symbol
        self.accept_states = accept_states

    def process(self, string):
        stack = [self.start_stack_symbol]
        state = self.start_state

        for symbol in string:
            if (state, symbol, stack[-1]) in self.transition_function:
                next_state, stack_action = self.transition_function[(state, symbol, stack[-1])]
                state = next_state
                if stack_action == "pop":
                    stack.pop()
                elif stack_action != "none":
                    stack.append(stack_action)
            else:
                return False  # No valid transition

        return state in self.accept_states and not stack  # Acceptance by empty stack

# Example of a Non-Deterministic PDA for the language L = {a^n b^n | n ≥ 0}
pda = PDA(
    states={"q0", "q1", "q_accept"},
    alphabet={"a", "b"},
    stack_alphabet={"A", "B"},
    transition_function={
        ("q0", "a", "none"): ("q0", "A"),  # Push A on stack when reading 'a'
        ("q0", "a", "A"): ("q0", "A"),    # Stay in q0 while reading 'a'
        ("q0", "b", "A"): ("q1", "none"), # Pop A when reading 'b'
        ("q1", "b", "A"): ("q1", "none"), # Stay in q1 while reading 'b'
        ("q1", "none", "none"): ("q_accept", "none"),  # Accept when the stack is empty
    },
    start_state="q0",
    start_stack_symbol="none",
    accept_states={"q_accept"}
)

# Test the PDA on a few strings
test_strings = ["", "ab", "aabb", "aaabbb", "aaab"]
print("\nTesting Non-Deterministic PDA:")
for test in test_strings:
    result = pda.process(test)
    print(f"'{test}': {'Accepted' if result else 'Rejected'}")


# 2. **Deterministic Pushdown Automata (DPA)**
# A Deterministic PDA is more restrictive in its transitions.
# An example of a DPA for the language L = {a^n b^n | n ≥ 0}.

class DPA:
    def __init__(self, states, alphabet, stack_alphabet, transition_function, start_state, start_stack_symbol, accept_states):
        self.states = states
        self.alphabet = alphabet
        self.stack_alphabet = stack_alphabet
        self.transition_function = transition_function
        self.start_state = start_state
        self.start_stack_symbol = start_stack_symbol
        self.accept_states = accept_states

    def process(self, string):
        stack = [self.start_stack_symbol]
        state = self.start_state

        for symbol in string:
            if (state, symbol, stack[-1]) in self.transition_function:
                next_state, stack_action = self.transition_function[(state, symbol, stack[-1])]
                state = next_state
                if stack_action == "pop":
                    stack.pop()
                elif stack_action != "none":
                    stack.append(stack_action)
            else:
                return False  # No valid transition

        return state in self.accept_states and not stack  # Acceptance by empty stack


# Example of a Deterministic PDA for L = {a^n b^n | n ≥ 0}
dpa = DPA(
    states={"q0", "q_accept", "q_reject"},
    alphabet={"a", "b"},
    stack_alphabet={"A"},
    transition_function={
        ("q0", "a", "none"): ("q0", "A"),
        ("q0", "a", "A"): ("q0", "A"),
        ("q0", "b", "A"): ("q_accept", "none"),
        ("q_accept", "b", "A"): ("q_accept", "none"),
        ("q_accept", "none", "none"): ("q_accept", "none"),
    },
    start_state="q0",
    start_stack_symbol="none",
    accept_states={"q_accept"}
)

# Test the DPA on the same strings
print("\nTesting Deterministic PDA:")
for test in test_strings:
    result = dpa.process(test)
    print(f"'{test}': {'Accepted' if result else 'Rejected'}")


# 3. **Parse Tree and Leftmost Derivation for Context-Free Grammar (CFG)**

class CFG:
    def __init__(self):
        self.rules = defaultdict(list)
    
    def add_rule(self, non_terminal, production):
        self.rules[non_terminal].append(production)
    
    def generate(self, start_symbol, depth=3):
        """Generates a string using the CFG rules with leftmost derivation."""
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

# Defining a CFG for palindromes: S -> aSa | bSb | ε
cfg = CFG()

cfg.add_rule("S", ["a", "S", "a"])
cfg.add_rule("S", ["b", "S", "b"])
cfg.add_rule("S", [""])  # ε (empty string)

# Generate a string using CFG (Leftmost Derivation)
generated_string = cfg.generate("S", depth=4)
print("\nGenerated String using CFG (Leftmost Derivation):", generated_string)


# 4. **Pumping Lemma for Context-Free Languages (CFL)**
# CFL Pumping Lemma: This lemma proves that certain languages are not context-free.
# A simplified version of the CFL Pumping Lemma:

def pumping_lemma_for_cfl(language):
    """
    Using the pumping lemma to prove a language is not context-free.
    A common example is L = {a^n b^n c^n | n ≥ 0}, which is not context-free.
    """
    print("\nUsing the Pumping Lemma to prove non-context-freeness:")
    # Assume L = {a^n b^n c^n | n ≥ 0}, a typical non-context-free language.
    # Let p be the pumping length.

    p = 3  # Arbitrary pumping length
    string = "a" * p + "b" * p + "c" * p
    print(f"Consider the string '{string}' of length >= p (p={p})")

    # We try to divide the string into xyz where x, y, z are substrings, and y can be pumped.
    x = "a" * 1
    y = "a" * 1
    z = "b" * p + "c" * p

    # Try pumping the middle part (y)
    pumped_strings = [x + (y * i) + z for i in range(1, 4)]
    for pumped in pumped_strings:
        print(f"Pumped string: '{pumped}'")
        # The pumped string should break the condition of having equal numbers of a's, b's, and c's
        if pumped.count('a') != pumped.count('b') or pumped.count('b') != pumped.count('c'):
            print(f"Rejected: '{pumped}' doesn't belong to the language!")
        else:
            print(f"Accepted: '{pumped}' belongs to the language!")

# Proving the language L = {a^n b^n c^n | n ≥ 0} is not context-free
pumping_lemma_for_cfl("a^n b^n c^n")


# 5. **Properties of Context-Free Languages (CFL)**
# - CFLs are closed under union, concatenation, and Kleene star.
# - They are **NOT** closed under intersection and complement.
# These properties can be observed through the use of PDAs and CFGs in the code.
