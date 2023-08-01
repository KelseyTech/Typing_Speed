import time
import random


# Selects random lines from the file
def random_line(fname):
    lines = open(fname).read().splitlines()
    return random.choice(lines)


def typing_attempt():
    # Difficulty
    sentence = input("Choose Easy or Hard: ")
    if sentence.title() == "Easy":
        sentence_len = random_line("sentences/short.txt")
    else:
        sentence_len = random_line("sentences/long.txt")

    wordcount = len(sentence_len.split())
    print(f"\n{sentence_len}")

    # Calculates the time taken
    start_time = time.time()
    timed_text = str(input("Enter the sentence: "))
    end_time = time.time()

    # Calculates the statistic
    accuracy = len(set(timed_text.split()) & set(sentence_len.split()))
    accuracy = accuracy / wordcount
    timetaken = end_time - start_time
    wpm = wordcount / timetaken * 60

    # Rounded numbers
    round_wpm = round(wpm, 2)
    round_accu = round(accuracy, 2)
    round_time = round(timetaken, 2)
    print(f"\nWPM: {round_wpm}\nAccuracy: {round_accu}\nTime Taken: {round_time} seconds\n" )


# Interactive Loop
exit = False
while not exit:
    user_input = input("p to play / q to quit: ")
    if user_input == "q":
        exit = True
    elif user_input == "p":
        typing_attempt()
    else:
        print("You need to enter either q or p")
