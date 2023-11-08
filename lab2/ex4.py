#a function that receives as a parameters a list of musical notes (strings),
#a list of moves (integers) and a start position (integer).
#The function will return the song composed by going though the musical notes
#beginning with the start position and following the moves given as parameter.
def song(notes, moves, start_pos):
    song = []
    current_pos = start_pos
    song.append(notes[current_pos])

    for move in moves:
        current_pos = (current_pos + move) % len(notes)
        song.append(notes[current_pos])

    return song


notes = ["do", "re", "mi", "fa", "sol"]
moves = [1, -3, 4, 2]
start_pos = 2

result = song(notes, moves, start_pos)
print(result)
