# Create needed variables
safe_counter = 0
data = []

# Read file into an list of lists
with open("data.txt", "r") as file:
    for line in file:
        inner_data = [int(elt.strip()) for elt in line.split(" ")]
        data.append(inner_data)

for i in range(len(data)):
    safe = True
    if data[i] == sorted(data[i]) or data[i] == sorted(data[i], reverse=True):
        for n in range(len(data[i]) - 1):
            if abs(data[i][n] - data[i][n + 1]) > 3 or abs(data[i][n] - data[i][n + 1]) == 0:
                safe = False
                break
        
        if safe:
            safe_counter += 1
                
            
            
print(safe_counter)