'''
LUIT Week 13 project
EC2 Random Name Generator
1. All the user to input how many EC2 instances they want names for and output the same amount of unique names.
2. Allow the user to input the name of their department that is used in the unique name.
3. Generate random characters and numbers that will be included in the unique name.

'''


import string
import random
 

def create_hostname(dept,number):
    for i in range(number):
        # initializing size of string
        N = 7
        # generating random strings
        res = ''.join(random.choices(string.ascii_uppercase + string.digits, k=N))
        # print result
        print(dept + "-" + str(res))

def rerun_script():
 while True:
    cont = input("\nWould you like to create more hostnames? yes/no > ")

    while cont.lower().strip() not in ("yes", "no"):
        cont = input("Would you like to create more hostnames? yes/no > ")

    if cont == "yes":
        break
    else:
        print("GoodBye!")
        exit()

def output_menu_tasks():
    """  
    Display a menu of choices to the user
    :return: nothing
    """
    print('''
    List of Departments
    1) Marketing
    2) FinOps
    3) Accounting     
    4) Exit Program
    ''')
    print()  

def input_menu_choice():
        """ 
        Gets the menu choice from a user
        :return: string
        """
        choice = str(input("Which option would you like to perform? [1 to 4] - ")).strip()
        print() 
        return choice

### Main ############################

while True:
 # Get instance numbers and department
    try:
        num = int(input("Input number of instances: "))
    except ValueError:
      print("Please input integer only...")  
      continue
# Print menu
    print("Please choose a department")
    output_menu_tasks()  # Shows menu
    choice_str = input_menu_choice()  # Get menu option

# Process user's menu choice
    if choice_str.strip() == '1': 
        create_hostname("MKTG", num)
        rerun_script()
        continue  

    elif choice_str == '2': 
        create_hostname("FINOPS", num)
        rerun_script()
        continue  

    elif choice_str == '3':  
        create_hostname("ACCT", num)
        rerun_script()
        continue  

    elif choice_str == '4': 
        print("Goodbye!")
        break 
    
