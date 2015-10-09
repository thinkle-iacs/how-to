# When you set up your file with your peers, you're going to be 
# setting up functions and test functions first of all.
# You should make sure you think through... 
#
# Function names
# Arguments and return values
# Test functions
#
# I'm going to do the set-up for a math quiz game below.
# Notice I haven't written any of the actual code yet.
# But I *have* thought through the structure of the game
# and the tests necessary to write it. 
# 
# If I were working in a team, I could now have the team
# working on each section write their functions independently
# and use the tests already written to test them out.

def get_math_question (difficulty_level, question_history):
    '''Given a difficulty_level (integer 1-10) and a question_history
    (questions asked so far), ask the user a new question.
    
    We make sure not to ask questions already asked.'''
    return ['What is 3+4',7] # Return q_and_a

def display_question (question):
    '''Display the question to the user.'''
    print 'Write some code here!',question
    # No return value

def get_answer (question_and_answer, nchances):
    '''Given a question and a right answer, give user nchances chances
    to answer it correctly. Return True for correct, False for incorrect.
    '''
    # Write real code here
    return True # or False -- whether they get it right!

def display_score (quiz_length, score):
    '''Given the question_history of user's quiz, display the score
    so far. Print a message based on the score.'''
    pass # Doesn't return anything

def run_quiz (difficulty, quiz_length):
    '''Run a quiz of difficulty difficulty and length quiz_length.'''
    score = 0 # This starts at 0
    question_history = [] # These start out empty
    # Write code here
    # This will call get_math_question, display_question, get_answer
    # and finally display_score
    print "Write code!"
    # No return value

### TEST FUNCTIONS ###

def test_display_question ():
    for question in ['What is 4x3?','What is 7+5?','What is 9-3?']:
        display_question(question)

def test_get_answer ():
    for q_and_a in [['What is 4x3',12],['What is 7+5',12],['What is 9-3',6]]:
        print 'Calling get_answer for ',q_and_
        retval = get_answer(q_and_a,3) # Try three chances
        print 'Returned: ',retval

def test_get_math_question ():
    for difficulty_level in range(1,11):
        qh = [] #question_history
        for n in range(10): # Generate 10 questions per level...
            question = get_math_question(difficulty_level,qh)
            qh.append(question) # add the history to the question_history
            print 'Difficulty: ',difficulty_level,'generated question: ',question

def test_display_score ():
    for quiz_length in range(5,20):
        for score in range(0,quiz_length+1):
            display_score(quiz_length,score)
