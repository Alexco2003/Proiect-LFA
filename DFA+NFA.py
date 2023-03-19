#Function to read the DFA/NFA from the file and return it as a tuple

def build_automata(file_name):
    with open(file_name) as f:
        n = int(f.readline().strip()) #total number of states
        sigma = f.readline().strip().split() #the alphabet
        q0 = int(f.readline().strip()) #start state
        final_states = set(int(state) for state in f.readline().strip().split()) #set of final states
        delta = {} #transition function (it will be a dictionary of dictionaries)
        for line in f:
            aux = line.strip().split()
            state = int(aux[0])
            symbol = aux[1]
            next_state = int(aux[2])
            if state in delta:
                if symbol in delta[state]:
                    delta[state][symbol].add(next_state)
                else:
                    delta[state][symbol] = set([next_state])
            else:
                delta[state] = {symbol: set([next_state])}
    return n, sigma, q0, final_states, delta

#Function to check if a given word is accepted by the DFA/NFA

def accepts(q0, final_states, delta, word):
    current_states = {q0}
    for symbol in word:
        next_states = set()
        for state in current_states:
            if state in delta and symbol in delta[state]:
                next_states = next_states | delta[state][symbol]
        current_states = next_states
    if current_states & final_states:
        return True
    else:
        return False

#Function to find all paths of a given word in the DFA/NFA

def all_paths(n, sigma, q0, final_states, delta, word, current_path=None):
    if current_path is None:
        current_path = [q0]

    if len(word) == 0: #if the entire word has been checked (no more symbols to check), check if the last state in the path is a final state
        if current_path[-1] in final_states:
            return [current_path]
        else:
            return []
    else:
        state = current_path[-1]
        symbol = word[0]

        if state in delta and symbol in delta[state]: #if there is a transition on the first symbol of the word, follow it recursively
            next_states = delta[state][symbol]
            paths = []
            for next_state in next_states:
                for path in all_paths(n, sigma, q0, final_states, delta, word[1:], current_path + [next_state]):
                    paths.append(path)
            return paths
        else:
            return []

#Read the DFA/NFA from the file
file_name=input("Enter the DFA/NFA file name : ").strip()
n, sigma, q0, final_states, delta = build_automata(file_name)

#The input word that we want to check
word = input("Enter a word : ").strip()

#Check if the input word is accepted by the DFA/NFA
accepted = accepts(q0, final_states, delta, word)

if accepted is True:
    print(f"Word {word} is accepted by the automata!")
    print("Paths :")
    for path in all_paths(n, sigma, q0, final_states, delta, word, [q0]):
        print(" ".join(str(state) for state in path))
else:
    print(f"Word {word} is not accepted by the automata!")
