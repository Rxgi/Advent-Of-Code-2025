dial_pos = 50  
FILENAME = "Day 01/input_codes.txt" 
score = 0

def check_rotation(pos, code):
    rotation = code[0]
    amount = int(code[1:])

    if rotation == "R":
        return (pos + amount) % 100
    else:
        return (pos - amount) % 100

with open(FILENAME, "r") as f:
    for line in f:
        line = line.strip()  
        dial_pos = check_rotation(dial_pos, line)
        
        print(f"{line}: {dial_pos}")
        
        if dial_pos == 0:
            score += 1

print(f"score = {score}")