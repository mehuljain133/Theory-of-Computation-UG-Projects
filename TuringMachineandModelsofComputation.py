# Turing Machines and Models of Computations: Turing machine as a model of computation,configuration of simple Turing machine, Church Turing Thesis, Universal Turing Machine,decidability, halting problem.

class TuringMachine:
    def __init__(self, states, alphabet, tape_alphabet, transition_function, start_state, halt_states, blank_symbol="B"):
        """
        Initializes the Turing Machine.
        """
        self.states = states  # Set of states
        self.alphabet = alphabet  # Input alphabet
        self.tape_alphabet = tape_alphabet  # Tape alphabet (includes blank symbol)
        self.transition_function = transition_function  # Transition function
        self.start_state = start_state  # Start state
        self.halt_states = halt_states  # Halting states
        self.blank_symbol = blank_symbol  # Blank symbol used on tape
        self.tape = [self.blank_symbol] * 1000  # Initialize the tape with blank symbols
        self.head_position = 500  # Initialize the tape head at position 500 (middle)
        self.current_state = self.start_state  # Initialize the state to the start state
    
    def step(self):
        """
        Perform one step of the Turing Machine computation.
        """
        current_symbol = self.tape[self.head_position]
        if (self.current_state, current_symbol) in self.transition_function:
            next_state, write_symbol, move = self.transition_function[(self.current_state, current_symbol)]
            self.tape[self.head_position] = write_symbol  # Write symbol on the tape
            self.current_state = next_state  # Update the current state
            if move == "R":
                self.head_position += 1  # Move head right
            elif move == "L":
                self.head_position -= 1  # Move head left
        else:
            print("No transition found. Halting.")
            self.current_state = "HALT"  # If no transition is found, halt the machine

    def run(self, input_string):
        """
        Run the Turing Machine with the given input string.
        """
        # Initialize the tape with the input string
        for i, symbol in enumerate(input_string):
            self.tape[500 + i] = symbol
        
        while self.current_state not in self.halt_states:
            self.step()

    def get_tape_string(self):
        """
        Get the string on the tape.
        """
        return ''.join(self.tape).strip(self.blank_symbol)

    def get_state(self):
        """
        Get the current state of the Turing Machine.
        """
        return self.current_state


# 1. **Example of a Turing Machine**
# A simple Turing Machine that checks if a string has an even number of 1s.
states = {"q0", "q1", "HALT"}
alphabet = {"0", "1"}
tape_alphabet = {"0", "1", "B"}
transition_function = {
    ("q0", "0"): ("q0", "0", "R"),
    ("q0", "1"): ("q1", "1", "R"),
    ("q1", "0"): ("q1", "0", "R"),
    ("q1", "1"): ("q0", "1", "R"),
    ("q0", "B"): ("HALT", "B", "R"),
    ("q1", "B"): ("HALT", "B", "R"),
}
start_state = "q0"
halt_states = {"HALT"}

# Test the Turing Machine
tm = TuringMachine(states, alphabet, tape_alphabet, transition_function, start_state, halt_states)
input_string = "1101"
tm.run(input_string)
print(f"Turing Machine Output for '{input_string}': {tm.get_tape_string()} (State: {tm.get_state()})")


# 2. **Church-Turing Thesis**
# This part demonstrates the Church-Turing Thesis: A Turing Machine can compute anything computable by any computational model.
# We will implement a **Universal Turing Machine** (UTM) next, which simulates any given Turing machine.

class UniversalTuringMachine:
    def __init__(self, machine, input_string):
        """
        Simulate a Universal Turing Machine that can simulate any Turing Machine.
        """
        self.machine = machine  # Turing machine to simulate
        self.input_string = input_string  # Input string to simulate
        self.tm = TuringMachine(machine.states, machine.alphabet, machine.tape_alphabet,
                                machine.transition_function, machine.start_state, machine.halt_states)
    
    def run(self):
        """
        Run the Universal Turing Machine, which simulates the given Turing Machine.
        """
        print(f"Simulating the given Turing Machine on input '{self.input_string}':")
        self.tm.run(self.input_string)
        return self.tm.get_tape_string()


# 3. **Decidability and the Halting Problem**
# The Halting Problem is an example of an undecidable problem.
# Let's define a Turing Machine that simulates the Halting Problem.

def halting_problem_simulation():
    """
    A simulation that demonstrates the undecidability of the Halting Problem.
    A Turing Machine that cannot decide if any given Turing Machine halts.
    """
    print("\nSimulating the Halting Problem:")
    # Given a Turing Machine and input, we cannot decide whether it halts or not in general.
    # For example, here we create a machine that loops indefinitely and show that it is undecidable.
    tm_loop = TuringMachine(
        states={"q0", "HALT"},
        alphabet={"1"},
        tape_alphabet={"1", "B"},
        transition_function={("q0", "1"): ("q0", "1", "R")},
        start_state="q0",
        halt_states={"HALT"}
    )
    try:
        tm_loop.run("1")
        print("The Turing Machine halted.")
    except Exception as e:
        print(f"Error: {str(e)}")


# 4. **Decidability and the Halting Problem Test**
halting_problem_simulation()


# 5. **Turing Machine Configuration and Visualization**
# Visualizing the configuration of a Turing machine at each step

def visualize_turing_machine(tm, input_string):
    """
    Visualize the Turing machine at each step during its computation.
    """
    print(f"\nInitial configuration for input '{input_string}':")
    print(f"State: {tm.get_state()} | Tape: {''.join(tm.tape).strip(tm.blank_symbol)} | Head: {tm.head_position}")
    tm.run(input_string)
    print(f"Final configuration:")
    print(f"State: {tm.get_state()} | Tape: {''.join(tm.tape).strip(tm.blank_symbol)} | Head: {tm.head_position}")


# Test the Turing Machine visualization
visualize_turing_machine(tm, "1101")


# 6. **Summary of Turing Machine, Universal Turing Machine, and Halting Problem**

def summarize_turing_machines():
    """
    Print summary of Turing Machines, Universal Turing Machines, and the Halting Problem.
    """
    print("\nSummary:")
    print("1. Turing Machine (TM) is a model of computation used to simulate any algorithmic process.")
    print("2. The Church-Turing Thesis states that anything computable by an algorithm can be computed by a Turing Machine.")
    print("3. A Universal Turing Machine (UTM) can simulate any Turing machine by reading its description and input.")
    print("4. The Halting Problem is undecidable. It is impossible to create a general algorithm that can decide whether any given Turing Machine will halt on an input.")
    print("5. Turing Machines and the Halting Problem lead to fundamental limits on computation.")
    print("\nTuring Machine model demonstrates the power and limitations of algorithmic processes.")


# Print the summary
summarize_turing_machines()

