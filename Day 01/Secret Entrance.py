DIAL_RANGE = range(100)
dial_start = 50

test_input = "R11"

rotation = test_input[0]
rotation_amount = int(test_input[1:])

def check_rotation(pos, rotation, amount):
    if rotation == "R":
        return (pos + amount) % 100
    else:
        return (pos - amount) % 100



