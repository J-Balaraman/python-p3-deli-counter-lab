def line(list):
    final_statement = "The line is currently:"
    initial_num = 1
    if len(list) == 0:
        print("The line is currently empty.")
        return None
    else:
        for person in list:
            final_statement = final_statement + f" {initial_num}. {person}"
            initial_num += 1
    print(f"{final_statement}")

def take_a_number(line, name):
    line.append(name)
    print(f"Welcome, {name}. You are number {len(line)} in line.")

def now_serving(line):
    if len(line) == 0:
        print("There is nobody waiting to be served!")
    else:
        print(f"Currently serving {line[0]}.")
        del(line[0])