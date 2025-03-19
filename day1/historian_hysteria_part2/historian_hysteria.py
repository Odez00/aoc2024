# Create arrays for locations1 and locations2, counter for reading contents
locations1 = []
locations2 = []
counter = 2
similarity = 0

# Read contents of locations.txt to arrays
with open("locations.txt", "r") as file:
    for line in file:
        for word in line.split():
            if counter % 2 == 0:
                locations1.append(int(word))
                counter += 1
            else:
                locations2.append(int(word))
                counter += 1

while len(locations1) > 0:
    index2 = 0
    counters = 0
    while index2 < len(locations2):
        if locations1[0] == locations2[index2]:
            counters += 1
            index2 += 1
        else:
            index2 += 1
    similarity += locations1[0] * counters
    locations1.pop(0)

print(similarity)