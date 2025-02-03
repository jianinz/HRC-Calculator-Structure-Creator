import re
import json

# Input string, copy your own string from PokerCraft on GG
data = """1	
OupsTuPerds
$418.77
2	
Windraker
$332.26
3	
uglytight
$263.65
4	
A Ivashchenkov
$209.21
5	
LinkouChampion
$166.02
6	
BrassMonkie
$131.74
7	
1Ingvar
$104.53
8	
cointoss
$82.95
9	
rehuperuna
$65.82
10	
BillNickolson
$52.23
11	
Yunghill1
$49.62
"""

# Define a dictionary to store prizes
prizes = {}

# Split the input data into lines
lines = data.split("\n")

# Iterate through lines to find the required information
for i in range(len(lines)):
    # Match lines that start with a number followed by a tab or newline
    match = re.match(r"^(\d+)\s*$", lines[i])
    if match:
        key = match.group(1)
        next_line = lines[i + 2]  # Line containing the prize information

        if "Finished" in next_line:
            # Extract the Yen or Dollar value if "Finished" is present
            prize_match = re.search(r"[\u00a5$]([\d,.]+)", next_line)
            if prize_match:
                prizes[key] = prize_match.group(1)
        else:
            # Extract the second Yen or Dollar value before the plus sign if present, otherwise take the first value
            prize_match = re.findall(r"[\u00a5$]([\d,.]+)", next_line)
            if len(prize_match) > 1:
                prizes[key] = prize_match[1]
            elif len(prize_match) == 1:
                prizes[key] = prize_match[0]

# Convert prizes dictionary to JSON
prizes_json = json.dumps({"prizes": prizes}, indent=4)

# Print the JSON object
print(prizes_json)
