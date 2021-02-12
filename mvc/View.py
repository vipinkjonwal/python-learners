from Model import Person

def show_all(users):
    print("We have {} users.".format(len(users)))

    for i in users:
        print(i)
    
def start_view():
    print("MVC Example")
    print("Do you want to continue: ")

def end_view():
    print("Thanks. Goodbye!")
