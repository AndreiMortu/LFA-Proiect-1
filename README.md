# LFA-Proiect-1
The program is a Python script that reads an automata file and a words file and checks if each word from the words file is accepted by the automata.

The program starts by importing the copy module, which provides the deepcopy() function used later in the program.

Then, the program prompts the user to input the name of the file that contains the automata and reads the file. The automata is represented by a set of states, an alphabet, an initial state, a set of final states, and a transition function. The program creates a dictionary to map each symbol of the alphabet to its index, and a nested list to store the transition function.

Next, the program prompts the user to input the name of the file that contains the words and reads the file. Each word is processed by simulating the automata. The program initializes a list with the initial state and a variable to store the current word. Then, it iterates over the current word and for each symbol, it creates a new copy of the current path using the deepcopy() function, and updates the copy with the next possible states according to the transition function. If there are multiple possible next states, the program creates a new copy of the current path for each possible state. The program then removes any empty paths and updates the current path with the new copy.

After processing the entire word, the program checks if the final state is reached and prints the word and the accepted paths if it is accepted, or prints the word and a rejection message if it is not accepted.

In summary, the program reads an automata file and a words file, and for each word in the words file, it simulates the automata and prints whether the word is accepted or rejected by the automata. The deepcopy() function from the copy module is used to create deep copies of the current path to avoid modifying the original path.
