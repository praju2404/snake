import random

lst = ["s","w","g"]

chance = 10
no_of_chance = 0
computr_pt = 0
human_pt = 0
print(" \t   ******SNAKE WATER GUN GAME****** \n  ")
print(" s  for snake/w for water/g for gun\n")

while no_of_chance < chance:
    user_input = input("ENTER YOOUR CHOICE:")
    cmp_input = random.choice(lst)

    if user_input == cmp_input:
            print("MATCH TIE..BOTH SCORES ARE ZERO\n")

    if user_input == "s" and cmp_input == "w":
        human_pt = human_pt + 1
        print("YOU GAINED 1 POINT..!!")
        print(f"YOUR GUESS IS {user_input} AND COMPUTER GUESS IS {cmp_input}")
        print(f"YOUR SCORE IS {human_pt} AND COMPUTER SCORE IS {computr_pt}")

    elif user_input == "s" and cmp_input == "g":
        computr_pt = computr_pt + 1
        print("COMPUTER GAINED 1 POINT..!!")
        print(f"YOUR GUESS IS {user_input} AND COMPUTER GUESS IS {cmp_input}")
        print(f"YOUR SCORE IS {human_pt} ANS COMPUTER SCORE IS {computr_pt}")



    elif user_input == "w" and cmp_input == "s":
        computr_pt = computr_pt + 1
        print("COMPUTER GAINED 1 POINT..!!")
        print(f"YOUR GUESS IS {user_input} AND COMPUTER GUESS IS {cmp_input}")
        print(f"YOUR SCORE IS {human_pt} ANS COMPUTER SCORE IS {computr_pt}")

    elif user_input == "w" and cmp_input == "g":
        human_pt = human_pt + 1
        print("YOU GAINED 1 POINT..!!")
        print(f"YOUR GUESS IS {user_input} AND COMPUTER GUESS IS {cmp_input}")
        print(f"YOUR SCORE IS {human_pt} AND COMPUTER SCORE IS {computr_pt}")



    elif user_input == "g" and cmp_input == "s":
        human_pt = human_pt + 1
        print("YOU GAINED 1 POINT..!!")
        print(f"YOUR GUESS IS {user_input} AND COMPUTER GUESS IS {cmp_input}")
        print(f"YOUR SCORE IS {human_pt} AND COMPUTER SCORE IS {computr_pt}")

    elif user_input == "g" and cmp_input == "w":
        computr_pt = computr_pt + 1
        print("COMPUTER GAINED 1 POINT..!!")
        print(f"YOUR GUESS IS {user_input} AND COMPUTER GUESS IS {cmp_input}")
        print(f"YOUR SCORE IS {human_pt} ANS COMPUTER SCORE IS {computr_pt}")

    else:
        print("YOUR INPUT IS WRONG!!")

    no_of_chance = no_of_chance + 1
    print(f"{chance - no_of_chance} is left outof {chance}\n")


