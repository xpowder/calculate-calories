#creating a class with two attributes  
class mymeal:
    def __init__(self, name, calorise) -> None:
        self.name = name
        self.calorise = calorise
        
#Define functions inside the class to perform actions on objects   
    def dark(self):
        self.name = input("Enter your meal: ")
        self.calorise = float(input(f"Enter your calories for {self.name}: "))
        print(f"Your meal is {self.name} and your calories are {self.calorise}")

    
#creat a function to updat a calorise with one attribute
    def mugure_calorise(self, new_calorise):
        self._calorise = new_calorise
        print(f"update {self.name} calorise to {new_calorise}")
        
        
        
#Define functions outside of the class 
 
def call(weight, height, age, sex, user_list):
    for _ in sex:
        sex = sex.lower()  # Convert to lowercase for case-insensitive comparison
        if sex == "male":
            #to calculate number of calories for a man
            total_calories =  10 * weight + 6.25 * height - 5 * age + 5
        elif sex == "female":
            #to calculate number of calories for a woamn
            total_calories =  10 * weight + 6.25 * height - 5 * age - 161
    
    user_list.append({"weight" : weight, "height" : height, "age" : age, "sex" : sex, "calorise" : total_calories})
    return total_calories
user_list = []
while True:
    try:
        weight = float(input("Enter your weight: "))
        height = float(input("Enter your height: "))
        break  # If successful, exit the loop
    except ValueError:
        print("Invalid input. Please enter a valid number.")

    
age = int(input("Enter your age: "))
sex = input("What is your gender: ")
        

total_calories = call(weight, height, age, sex, user_list)
print(f"Your total calories are: {total_calories}")
#to print the list
for lis in user_list:
    print(lis)

breakfast = mymeal("breakfast", 300)
lunch = mymeal("Lunch", 400)
Dinner = mymeal("Dinner", 700)
breakfast.dark()
lunch.dark()
Dinner.dark()

