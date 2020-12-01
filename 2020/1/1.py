

def part_one(vals):
    i = 1
    for v in vals:
        while(v + vals[-i] > 2020):
            i += 1

        if v + vals[-i] == 2020:
            print("{}".format(v*vals[-i]))
            return

def part_two(vals):
    i = 0
    j = 0
    first_j = 0
    for v in vals:
        first_j += 1
        j = first_j
        while(v + vals[j] + vals[-i] > 2020):
            i += 1

        while(v + vals[j] + vals[-i] < 2020):
            j += 1

        if v + vals[j] + vals[-i] == 2020:
            print("{}".format(v*vals[j]*vals[-i]))
            return


if __name__ == "__main__":
    vals = []
    with open("input", 'r') as f:
        for line in f:
            vals.append(int(line))
    vals.sort()
    part_one(vals)
    part_two(vals)
