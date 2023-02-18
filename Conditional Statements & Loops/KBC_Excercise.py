
question = ["What is the Capital of India?", "What is the Capital of west bengal?", "Who won the FIFA 2022?",
            "Take a name of a France Football Player", "Which city is called \"City of Joy?\""]

option = [["A: Delhi B: Mumbai"], ["A: Kolkata B: Chennai"], [
    "A: Argentina B: Portugal"], ["A: Mabappe B: Ronaldo"], ["A: Kolkata B: Bangaluru"]]

correctAns = ['A', 'A', 'A', 'A', 'A']
count = 0
print("\n\n-------------You will get Rs 1000 fo each Question------------\n\n")
for i in range(5):
    print("Question ", (i+1), ": ", question[i], "\n")
    print(option[i], "\nEnter your Answer", end=': ')
    ans = input()
    if(correctAns[i] == ans):
        count += 1000
print("\nYou earned: ", count)
