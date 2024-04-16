import csv, sys

ability_score_names = ["str","dex","con","int","wis","cha"]
skill_names = [
    "acrobatics", "animal handling", "arcana", "athletics", "deception", "history",
    "insight", "intimidation", "investigation", "medicine", "nature", "perception",
    "performance", "persuasion", "religion", "sleight of hand", "stealth", "survival"
]
skill_ability_scores = [
    "dex", "wis", "int", "str", "cha",
    "int", "wis", "cha", "int", "wis",
    "int", "wis", "cha", "cha", "int",
    "dex", "dex", "wis"
]
proficiency_bonus = 2
def display_menu():
    print(
        "\nCharacter Sheet\nMAIN MENU\n"
        )
    print("Commands: ")
    print("View")
    print("Edit")
    print("Back\n")
    print("To view commands at any time, type HELP")

def display_submenu():
    print("AS - Ability Scores")
    print("Sk - Skills")
    print("AC - Armor Class")
    print("Pr - Proficiencies")
    print("Back\n")
    print("To view commands at any time, type HELP")

def view():
    print("\nChoose something to view:\n")
    display_submenu()
    while True:
        command = input("Command: ")
        if command.lower() == "as":
            display_ability_scores()
        elif command.lower() == "sk":
            display_skills()
        elif command.lower() == "ac":
            continue
        elif command.lower() == "pr":
            display_proficiencies()
        elif command.lower() == "help":
            display_submenu()
        elif command.lower() == "back":
            main()

def edit():
    print("\nChoose something to edit:\n")
    display_submenu()
    while True:
        command = input("Command: ")
        if command.lower() == "as":
            display_ability_scores()
            print("\nSelect ability score to edit: ")
        elif command.lower() == "sk":
            display_skills()
            print("\nSelect skill to edit: ")
        elif command.lower() == "ac":
            continue
        elif command.lower() == "pr":
            display_proficiencies()
            print("\nSelect proficiency to edit: ")
        elif command.lower() == "help":
            display_submenu()
        elif command.lower() == "back":
            main()

def display_ability_scores():
    ability_scores = read_ability_scores()
    for i,j in zip(ability_score_names,ability_scores):
        print(f"{i} - {j} ({calc_mod(j)})")

def read_ability_scores():
    ability_scores = []
    with open("abilityscores.csv", newline="") as file:
            reader = csv.reader(file)
            for row in reader:
                ability_scores.append(row)
    return ability_scores

def display_skills():
    proficiencies = read_proficiencies()
    for i,j in zip(skill_names,skill_mods):
        if proficiencies in skill_names:
            for proficiencies in skill_names:
                print(f"{i} - {int(j) + proficiency_bonus}")
        else:
            print(f"{i} - {j} ")

def display_proficiencies():
    proficiencies = read_proficiencies()
    for i in proficiencies:
        print(i)

def read_proficiencies():
    proficiencies = []
    with open("proficiencies.csv", newline="") as file:
            reader = csv.reader(file)
            for row in reader:
                proficiencies.extend(row)
    return proficiencies

def calc_mod(ability_scores):
    as_mods = zip([x for x in range(0,32,2)],[y for y in range(-5,11)])
    if int(ability_scores[1]) % 2 == 0:
        return [x[1] for x in as_mods if ability_scores[1]==x[0]][0]
    else:
        i = int(ability_scores[1]) - 1
        return [x[1] for x in as_mods if i==x[0]][0]

    #This is all redundant
    # score_value = int(ability_scores)
    # if score_value % 2 == 0:
    #     i = possible_ability_scores.index(score_value)
    #     modifier = modifiers_list[i]
    # else:
    #     value = score_value - 1
    #     i = possible_ability_scores.index(value)
    #     modifier = modifiers_list[i]
    # return modifier

def calc_skill_modifiers():
    ability_scores = read_ability_scores()
    modifiers = calc_mod(ability_scores)
    ability_scores_plus_modifiers = zip(ability_score_names,modifiers)
    skill_modifiers = []
    []
    for i,j in zip(skill_names,skill_ability_scores):
        if j.lower() in ability_scores_plus_modifiers:
            skill_modifiers.extend(ability_scores_plus_modifiers[j])

def skills():
    zipped_ability_scores = zip(ability_score_names,read_ability_scores)
    asm = zip(skill_names,skill_ability_scores)
    [x for x in asm for x[1] in zipped_ability_scores[x]]
    

def main():
    display_menu()

    while True:
        command = input("Command: ")
        if command.lower() == "view":
            view()
        elif command.lower() == "edit":
            edit()
        elif command.lower() == "exit":
            break
        elif command.lower() == "read":
            display_ability_scores()
        else:
            print("Enter a valid command.")

if __name__ == "__main__":
    main()