from Tape import TuringMachine

initial_state = 'q1',
accepting_states = [
                       "qA", "qR"
                   ],
# transition_function = {
#     ('q1', "0"): ('q2', '_', "R"),
#     ('q1', '_'): ('qR', '_', "R"),
#     ('q1', "x"): ('qR', "x", "N"),
#
#     ('q2', "0"): ('q3', "x", "R"),
#     ('q2', '_'): ('qA', '_', "N"),
#     ('q2', "x"): ("q2", "x", "R"),
#
#     ('q3', "0"): ('q4', "0", "R"),
#     ('q3', '_'): ('q5', '_', "L"),
#     ('q3', "x"): ("q3", "x", "R"),
#
#     ('q4', "0"): ('q3', "x", "R"),
#     ('q4', '_'): ('qR', '_', "R"),
#     ('q4', "x"): ("q4", "x", "R"),
#
#     ('q5', "0"): ('q5', "0", "L"),
#     ('q5', '_'): ('q2', '_', "R"),
#     ('q5', "x"): ("q5", "x", "L"),
# }

transition_function = {
    ('q1', "0"): ('q2', '0', "R"),
    ('q1', '1'): ('q1', '1', "R"),
    ('q1', '_'): ('qA', '1', "R"),

    ('q2', "0"): ('q2', "0", "R"),
    ('q2', '1'): ('q3', '1', "R"),
    ('q2', '_'): ('q2', '_', "L"),

    ('q3', "0"): ('qR', "0", "R"),
    ('q3', '1'): ('qR', '0', "R"),
    ('q3', '_'): ('qR', '_', "R")
}
final_states = [
    "qR", 'qA'
]

files = [
    'inputReject.txt', 'inputEnd.txt', 'inputLoop.txt'
]

for i in files:
    file1 = open(i, 'r')
    file2 = open('{}Out.txt'.format(i), 'w')
    lines = file1.read()

    t = TuringMachine(
        lines,
        initial_state='q1',
        final_states=final_states,
        transition_function=transition_function,
        blank_symbol="_"
    )

    print("Input on Tape:\n" + t.get_tape())

    while not t.final():
        t.step()

    print("Result of the Turing machine calculation:")
    print(t.get_state())
    file2.write(t.get_state())
    file2.write('\n')

    file1.close()
    file2.close()

