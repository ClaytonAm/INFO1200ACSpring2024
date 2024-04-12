import random, sys

def main():
    dashes = "------------------------------------"
    nums = [1, 3, 2, 23, 1, 6, 5, 89, 0]
    print(nums)
    print(dashes)

    nums.append(11) #add value to the end of a list
    print(nums)
    print(dashes)

    nums.insert(3,25.4) #args: (index, value to be inserted)
    print(nums)
    print(dashes)

    num = nums.pop()
    print(num)
    print(nums)
    print(dashes)

    if 2 in nums:
        nums.remove(2)
    print(nums)
    print(dashes)

    bullet = 1
    for i in nums:
        print(f"{bullet}. {i}")
        bullet += 1
    print(dashes)
    
    for i, item in enumerate(nums, start=1):
        print(f"{i}. {item}")
    print(dashes)

    nums.sort()
    print(nums)
    print(dashes)

    randnum = random.choice(nums)
    print(randnum)
    print(dashes)

    random.shuffle(nums)
    print(nums)
    print(dashes)

    newtuple = {3, 23, 0, 25.4, 1, 5, 6, 1, 89}
    print(sys.getsizeof(nums))
    print(sys.getsizeof(newtuple))
    print(dashes)

    ability_scores_list = []
    for i in range(0, 32, 2):
        ability_scores_list.append(i)
    print(ability_scores_list)
    possible_modifiers_list = []
    for i in range(-5, 10):
        possible_modifiers_list.append(i)
    print(possible_modifiers_list)

if __name__ == "__main__":
    main()