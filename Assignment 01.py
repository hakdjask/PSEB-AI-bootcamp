class studentManager:
    def s_name(self):
        student_names = []
            
        for i in range(3):
            student_name = input(f"Enter the {i+1} student's name: ")
            student_names.append(student_name)
            
        return student_names
    
    def s_scores(self, student_names):
        student_scores = []

        print("\n")

        for i in range(3):
            student_score = float(input(f"Enter the score for {student_names[i]}: "))
            student_scores.append(student_score)
            
        return student_scores
    
    
    def top_scorer(self, names, scores):
        top_index = 0
        
        for i in range(1, len(scores)):
            if scores[i] > scores[top_index]:
                top_index = i
        
        return names[top_index], scores[top_index]
    
    def __init__(self): 
        self.names = self.s_name()
        self.scores = self.s_scores(self.names)
        
        top_name, top_score = self.top_scorer(self.names, self.scores)

        print("\n")

        for i in range(len(self.names)):
            if self.scores[i] < 50:
                continue
            print(f"{self.names[i]} scored {self.scores[i]}.")

        print("\n")

        print(f"The top scorer is {top_name} with a score of {top_score}.")

print("\n")
print("Welcome to the Student Manager!" "\n")

obj = studentManager()