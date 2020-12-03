import os


def part1(values):
    for value in values:
        if value in values:
            print(f"Values found: {value} + {2020-value} = 2020")
            print(f"Multiplied: {value*(2020-value)}")
            exit(0)
        values.add(2020 - value)
        print(f"value: 2020 `- {value}")
    


def part2(setValues):
    values = list(setValues)
    for i, value in enumerate(values):
        for value2 in values[i+1:]:
            for value3 in values[i+2:]:
                if(value + value2 + value3 == 2020):
                    print(f"values: {value} + {value2} + {value3} = 2020")
                    print(f"multiplied: {value * value2 * value3}")


def read_file():
    file = os.path.join(os.path.dirname(__file__), 'input.txt')
    lines = ''
    values = set()
    with open(file, 'r') as file:
        lines = file.readlines()
    for line in lines:
        values.add(int(line))
    
    #part1(values)
    part2(values)
    
    


# clean this up later
read_file()