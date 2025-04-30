# Regular Languages: Non-deterministic Finite Automata (NFA), relationship between NFA andDFA, Transition Graphs (TG), properties of regular languages, the relationship between regularlanguages and finite automata, Kleene's Theorem.

import re
from collections import defaultdict

# 1. **Non-deterministic Finite Automaton (NFA)**

class NFA:
    def __init__(self, states, alphabet, transition_function, start_state, accept_states):
        self.states = states
        self.alphabet = alphabet
        self.transition_function = transition_function
        self.start_state = start_state
        self.accept_states = accept_states

    def epsilon_closure(self, state):
        """Returns the epsilon closure of a given state"""
        closure = {state}
        if "" in self.transition_function[state]:
            for next_state in self.transition_function[state][""]:
                closure |= self.epsilon_closure(next_state)
        return closure

    def move(self, states, symbol):
        """Returns the set of states reachable from a set of states on a given symbol"""
        next_states = set()
        for state in states:
            if symbol in self.transition_function[state]:
                next_states |= self.transition_function[state][symbol]
        return next_states

    def process(self, string):
        """Processes the input string through the NFA"""
        current_states = self.epsilon_closure(self.start_state)
        for symbol in string:
            current_states = self.epsilon_closure(self.move(current_states, symbol))
        return any(state in self.accept_states for state in current_states)

# NFA for regular expression "a*b*"
states = {"q0", "q1", "q2"}
alphabet = {"a", "b"}
transition_function = {
    "q0": {"a": {"q0", "q1"}, "b": {"q0"}, "": {"q0"}},  # Epsilon transition from q0 to q0
    "q1": {"a": {"q1"}, "b": {"q2"}},
    "q2": {"b": {"q2"}}
}
start_state = "q0"
accept_states = {"q0", "q2"}

nfa = NFA(states, alphabet, transition_function, start_state, accept_states)

# Test NFA on some strings
test_strings = ["", "a", "aa", "b", "bb", "ab", "aab", "aabb", "bba", "aaabbb"]
print("NFA Matches:")
for test in test_strings:
    result = nfa.process(test)
    print(f"'{test}': {'Accepted' if result else 'Rejected'}")


# 2. **Conversion from NFA to DFA (Subset Construction Algorithm)**
class DFA:
    def __init__(self, nfa):
        self.states = []
        self.alphabet = nfa.alphabet
        self.transition_function = {}
        self.start_state = frozenset(nfa.epsilon_closure(nfa.start_state))
        self.accept_states = set()
        self.build_dfa(nfa)

    def build_dfa(self, nfa):
        unmarked_states = [self.start_state]
        state_mapping = {self.start_state: "q0"}
        state_counter = 1
        while unmarked_states:
            current_state = unmarked_states.pop()
            if any(state in nfa.accept_states for state in current_state):
                self.accept_states.add(state_mapping[current_state])
            for symbol in self.alphabet:
                next_state = frozenset(nfa.epsilon_closure(state) for state in nfa.move(current_state, symbol))
                if next_state not in state_mapping:
                    state_mapping[next_state] = f"q{state_counter}"
                    state_counter += 1
                    unmarked_states.append(next_state)
                self.transition_function[state_mapping[current_state], symbol] = state_mapping[next_state]

    def process(self, string):
        current_state = self.start_state
        for symbol in string:
            current_state = self.transition_function.get((current_state, symbol))
            if current_state is None:
                return False
        return current_state in self.accept_states


# Convert the NFA to DFA
dfa = DFA(nfa)

# Test DFA on the same test strings
print("\nDFA Matches:")
for test in test_strings:
    result = dfa.process(test)
    print(f"'{test}': {'Accepted' if result else 'Rejected'}")


# 3. **Transition Graph (TG)**
# A simple function to visualize the transition graph
def print_transition_graph(nfa):
    print("\nTransition Graph (TG) of NFA:")
    for state in nfa.states:
        for symbol, next_states in nfa.transition_function[state].items():
            if symbol != "":
                for next_state in next_states:
                    print(f"{state} -- {symbol} --> {next_state}")

print_transition_graph(nfa)

# 4. **Kleene's Theorem (Regular Languages and Finite Automata)**
# Kleene's Theorem states that a language is regular if and only if there exists a finite automaton that recognizes it.
# This is demonstrated above where both NFA and DFA can recognize the same language.

# 5. **Properties of Regular Languages**
# - Closed under union, concatenation, intersection, and complement.
# - A regular language can be described using both a DFA and an NFA.
# - Any regular language can be described by a regular expression.
# Let's demonstrate closure under union with an example.

def union_nfa(nfa1, nfa2):
    """Creates an NFA for the union of two NFAs (NFA1 U NFA2)"""
    states = nfa1.states.union(nfa2.states)
    alphabet = nfa1.alphabet.union(nfa2.alphabet)
    transition_function = defaultdict(dict)
    
    # Add transition functions for NFA1 and NFA2
    for state in nfa1.transition_function:
        for symbol in nfa1.transition_function[state]:
            transition_function[state][symbol] = nfa1.transition_function[state][symbol]
    
    for state in nfa2.transition_function:
        for symbol in nfa2.transition_function[state]:
            transition_function[state][symbol] = nfa2.transition_function[state][symbol]

    start_state = "q0"
    accept_states = nfa1.accept_states.union(nfa2.accept_states)
    
    return NFA(states, alphabet, transition_function, start_state, accept_states)

# Create a union NFA example (combine the original NFA with a simple one for "b*")
nfa2 = NFA(
    {"q0", "q1"},
    {"b"},
    {"q0": {"b": {"q1"}}, "q1": {"b": {"q1"}}},
    "q0",
    {"q1"}
)

union_result_nfa = union_nfa(nfa, nfa2)
print("\nUnion of two NFAs (NFA1 U NFA2) Test Results:")
for test in test_strings:
    result = union_result_nfa.process(test)
    print(f"'{test}': {'Accepted' if result else 'Rejected'}")
