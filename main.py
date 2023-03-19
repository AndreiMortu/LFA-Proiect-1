import copy

# Read the automata file
automata_file_name = input("Introduceti denumirea fisierului ce contine automata: ").strip()
with open(automata_file_name) as automata_input_file:
    nr_states = int(automata_input_file.readline())
    sigma = automata_input_file.readline().split()
    initial_state = int(automata_input_file.readline().strip())
    final_states = [int(x) for x in automata_input_file.readline().split()]
    alphabet_dict = {sigma[i]: i for i in range(len(sigma))}
    next_state_delta = [[[] for i in range(len(sigma))] for j in range(nr_states)]
    line = automata_input_file.readline()
    while line:
        state1, transition, state2 = map(str.strip, line.split())
        state1 = int(state1)
        state2 = int(state2)
        next_state_delta[state1][alphabet_dict[transition]].append(state2)
        line = automata_input_file.readline()

# Read the words file
words_file_name = input("Introduceti denumirea fisierului ce contine cuvinte: ").strip()
with open(words_file_name) as words_input_file:
    line = words_input_file.readline()
    while line:
        word = line.strip()[1:-1]
        initial_word = word
        current_path = [[initial_state]]
        while word:
            current_symbol = word[0]
            word = word[1:]
            new_current_path = copy.deepcopy(current_path)
            if not current_path:
                break
            cnt = 0
            index = 0
            while index < len(current_path):
                current_state = current_path[index][-1]
                next_possible_states = next_state_delta[current_state][alphabet_dict[current_symbol]]
                if len(next_possible_states) == 1:
                    new_current_path[index].append(next_possible_states[0])
                elif len(next_possible_states) > 1:
                    cnt += 1
                    for next_state in next_possible_states:
                        new_current_path.append(current_path[index] + [next_state])
                index += 1
            index = 0
            while index < len(new_current_path):
                if not new_current_path[index]:
                    new_current_path.pop(index)
                    index -= 1
                index += 1
            current_path = copy.deepcopy(new_current_path)
            for _ in range(cnt):
                current_path.pop(0)
        if not initial_word:
            initial_word = "λ"
        accepted = False
        if not word:
            for path in current_path:
                if path[-1] in final_states:
                    accepted = True
                    break
            if accepted:
                print(f"\nCuvantul {initial_word} este acceptat de automata ._ .")
                print("Drumurile: ")
            for path in current_path:
                if path[-1] in final_states:
                    print(*path, end="\n")
        if not accepted:
            print(f"\nCuvantul {initial_word} nu este acceptat de automata . _.", end="\n")
        line = words_input_file.readline()