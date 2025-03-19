# Create arrays for locations1 and locations2, counter for reading contents and current smallest number for both arrays
locations1 = []
locations2 = []
counter = 2
sum_of_smallest = 0


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

# Find smallest number in both arrays and add the difference to sum_of_smallest, then pop them out of the arrays
while len(locations1) and len(locations2) > 0:
    smallest_1 = min(locations1)
    smallest_2 = min(locations2)

    sum_of_smallest += abs(smallest_1 - smallest_2)

    smallest_1_index = locations1.index(smallest_1)
    smallest_2_index = locations2.index(smallest_2)

    locations1.pop(smallest_1_index)
    locations2.pop(smallest_2_index)

print(sum_of_smallest)