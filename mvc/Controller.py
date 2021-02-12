from Model import Person
import View as View

def show_all():
    people_in_db = Person.get_all()
    return View.show_all(people_in_db)

def start():
    View.start_view()
    user_input = input("Enter Y/N: ")

    if user_input == 'Y':
        return show_all()
    else:
        return View.end_view()

if __name__ == '__main__':
    start()
    