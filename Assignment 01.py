class studentManager:
   
   # Creating a function to get the names of the students and store them in a list
   
    def s_name(self):
        student_names = []
            
        for i in range(3):
            student_name = input(f"Enter the {i+1} student's name: ")
            student_names.append(student_name)
            
        return student_names
    
    # Creating a function to get the scores of the students and store them in a list
    
    def s_scores(self, student_names):
        student_scores = []

        print("\n")

        for i in range(3):
            student_score = float(input(f"Enter the score for {student_names[i]}: "))
            student_scores.append(student_score)
            
        return student_scores
    
    # Creating a function to find the top scorer among the students
    
    def top_scorer(self, names, scores):
        top_index = 0
        
        for i in range(1, len(scores)):
            if scores[i] > scores[top_index]:
                top_index = i
        
        return names[top_index], scores[top_index]
    
    # Creating the constructor to initialize the student manager and display the results
    
    def __init__(self): 
        self.names = self.s_name()
        self.scores = self.s_scores(self.names)
        
        top_name, top_score = self.top_scorer(self.names, self.scores)

        print("\n")

        # Displaying the names and scores of students who scored 50 or above

        for i in range(len(self.names)):
            if self.scores[i] < 50:
                continue
            print(f"{self.names[i]} scored {self.scores[i]}.")

        print("\n")

        # Displaying the top scorer's name and score

        print(f"The top scorer is {top_name} with a score of {top_score}.")

print("\n")
print("Welcome to the Student Manager!" "\n")

obj = studentManager()