low = 1 
high = 100

print("Think of a number between 1 and 100")


while(low<=high):
    mid = (low+high) // 2
    print(f"My guess is: {mid}")
    feedback = input("Is it higher, lower, or correct")

    if feedback == "higher":
        low = mid + 1
    elif feedback =="lower":
        high = mid - 1
    elif feedback == "correct":
        print("Yay! I guessed your number!")
        break
    else:
        print("Invalid Input , Try again")
