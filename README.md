# Proiect LFA -> DFA & NFA

 DFA &amp; NFA

 Implemented a Python algorithm that gets as input a DFA/NFA and a word from the user and determines if the word is accepted or not. If the word is accepted every path that reaches a final state will be displayed.
 
 The automata input file needs to have the following layout :
 
n (total number of states) \
sigma (alphabet) \
initial state \
list of all the final states \
state symbol next_state (this represents the delta function, from state with symbol we get to next_state)

Example of input file :

6\
a b\
0\
4 5\
0 a 1\
0 a 2\
1 b 3\
1 b 1\
1 a 4\
2 b 1\
3 b 5\
4 a 3\
4 b 5

Example of outputs :

Enter the DFA/NFA file name : input.txt\
Enter a word : abbaaba\
Word abbaaba is not accepted by the automata!

Enter the DFA/NFA file name : input.txt\
Enter a word : aba\
Word aba is accepted by the automata!\
Paths :\
0 1 1 4\
0 2 1 4
