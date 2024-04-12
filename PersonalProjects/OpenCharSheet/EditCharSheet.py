import csv, sys

ability_score_names = ["Str","Dex","Con","Int","Wis","Cha"]
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
    print("\nCharacter Sheet\nMAIN MENU\n")
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
                ability_scores.extend(row)
    return ability_scores

def display_skills():
    proficiencies = read_proficiencies()
    for i,j in zip(skill_names,skill_mods):
        if proficiencies in skill_names:
            for proficiencies in skill_names
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
    possible_ability_scores = [0,2,4,6,8,10,12,14,16,18,20,22,24,26,28,30]
    modifiers_list = [-5,-4,-3,-2,-1,0,1,2,3,4,5,6,7,8,9,10]

    score_value = int(ability_scores)
    if score_value % 2 == 0:
        i = possible_ability_scores.index(score_value)
        modifier = modifiers_list[i]
    else:
        value = score_value - 1
        i = possible_ability_scores.index(value)
        modifier = modifiers_list[i]
    return modifier

def calc_skill_modifiers():
    ability_scores = read_ability_scores()
    modifiers = calc_mod(ability_scores)
    ability_scores_plus_modifiers = zip(ability_score_names,modifiers)
    skill_modifiers = []
    for i,j in zip(skill_names,skill_ability_scores):
        if j.lower() in ability_scores_plus_modifiers:
            skill_modifiers.extend(ability_scores_plus_modifiers[j])

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