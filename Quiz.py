import csv, random

def get_questions():
	questions = []
	
	#opening and reading from a file
	with open("C:/Python34/Workspace/Quiz game/quiz.csv",mode="r",encoding="utf-8") as my_file:
		quiz = csv.reader(my_file)
		for question in quiz:
			questions.append(question)
	return questions

def ask_question(questions, score):
	print(questions[0])

	#Printing the options 
	for question in questions[1:-1]:
		''' '<'	Forces the field to be left-aligned within the available space (this is the default for most objects).
			'>'	Forces the field to be right-aligned within the available space (this is the default for numbers).
			'='	Forces the padding to be placed after the sign (if any) but before the digits.
					 This is used for printing fields in the form ‘+000000120’. This alignment option is only valid for numeric types.
			'^'	Forces the field to be centered within the available space. '''
		
		print("{0:>5}{1}".format("", question))

	#Accepting Input and calculating score
	answer = input("Please select an answer : \n")
	if answer == questions[-1]:
		print("Correct answer! ")
		score +=1
	else:
		print("Incorrect! I am sorry - The Correct answer is {0} \n".format(questions[-1]))
	return score

def main():
	#Calling the get_questions function to get the questions printed on the screen
	questions = get_questions()
	
	# setting the score variable to keep rack of the score
	score = 0

	print("========= Welcome to the Quiz !! ============\n ======================================\n\n")
	number = int(input("There are {0} questions - how many do you want in your quiz\n".format(len(questions))))
	
	for next_question in range(number):
		# To call a question randomly
		question = random.choice(questions)
		score = ask_question(question, score)
		
		#Removing the questions already asked from the questions[]
		questions.remove(question)

	print("Your final score was {0} out of {1}.\n".format(score,number))

main()
