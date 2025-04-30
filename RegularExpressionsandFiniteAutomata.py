# Regular Expressions and Finite Automata: Regular expressions, Deterministic finite automata (DFA). 

# 1. **Regular Expressions** (RE)
import re

def match_regular_expression(pattern, string):
    # This function uses regular expressions to match a string with a pattern
    return bool(re.fullmatch(pattern, string))

# Regular expression pattern for strings of 'a's followed by 'b's (a*b*)
pattern = r"a*b*"

# Test the regular expression
test_strings = ["", "a", "aa", "b", "bb", "ab", "aab", "bba", "aaabbb"]
print("Regular Expression Matches:")
for test in test_strings:
    result = match_regular_expression(pattern, test)
    print(f"'{test}': {'Match' if result else 'No Match'}")


# 2. **Deterministic Finite Automaton (DFA)**

class DFA:
    def __init__(self):
        # Define the DFA's states
        self.states = {"q0", "q1", "q2"}  # q0 (start state), q1, q2 (accept state)
        self.start_state = "q0"  # Start at q0
        self.accept_states = {"q0", "q2"}  # Accept states: q0 and q2
        self.transition_function = {
            "q0": {"a": "q1", "b": "q2"},  # q0 transitions: 'a' goes to q1, 'b' goes to q2
            "q1": {"a": "q1", "b": "q2"},  # q1 transitions: 'a' stays in q1, 'b' goes to q2
            "q2": {"b": "q2"}  # q2 transitions: 'b' stays in q2
        }

    def process(self, string):
        state = self.start_state
        for symbol in string:
            if symbol in self.transition_function[state]:
                state = self.transition_function[state][symbol]
            else:
                return False  # Invalid symbol for current state

        return state in self.accept_states  # String is accepted if we end in an accepting state


# DFA instance for the pattern a*b*
dfa = DFA()

# Test DFA on the same test strings
print("\nDFA Matches:")
for test in test_strings:
    result = dfa.process(test)
    print(f"'{test}': {'Accepted' if result else 'Rejected'}")
