# Proiect LFA DFA & NFA

 DFA &amp; NFA

 Implemented a Python algorithm that gets as input a DFA/NFA and a word from the user and determines if the word is accepted or not. If the word is accepted every path that reaches a final state will be displayed.
 
 The automata input file needs to have the following layout:
 
n (total number of states)
sigma (alphabet)
index of the initial state
list of all the final states
state symbol next_state (this represents the delta function, from state with symbol we get to next_state)
