def add():
    user_name = input("Enter the name: ")
    number = input(f"Enter the mobile number of {user_name}: ")
    email = input(f"Enter the email address of {user_name}: ")
    address = input(f"Enter the address of {user_name}: ")

    contact_book[user_name] = (number, email, address)
    keys.append(user_name)

def view():
    for i in keys:
        temp = contact_book[i]
        print(f"Name: {i}\nMobile number: {temp[0]}\nEmail address: {temp[1]}\nAddress: {temp[2]}\n")

def search():
    search_name = input("Enter the user_name you want to search for: ")
    if search_name in keys:
        temp = contact_book[search_name]
        print("Contact found:")
        print(f"Name: {search_name}\nMobile number: {temp[0]}\nEmail address: {temp[1]}\nAddress: {temp[2]}\n")
    else:
        print("Contact not found in the contact book")

def update():
    edit_name = input("Enter the user name you want to edit the details: ")
    if edit_name in keys:
        edit_num = input("Enter the new number: ")
        edit_mail = input("Enter the new email: ")
        edit_address = input("Enter the new address: ")
        contact_book[edit_name] = (edit_num, edit_mail, edit_address)
    else:
        print("No contact found. Create a new contact.")

def delete():
    del_name = input("Enter the username you want to delete the contact for: ")
    if del_name in keys:
        contact_book.pop(del_name)
        keys.remove(del_name)
    else:
        print("Contact not found in the contact book.")

def default():
    print("Choose a valid option")

contact_book = {}
keys = []
while True:
    print("Select your option:")
    choice = int(input("1. Add contact\n2. View contact\n3. Search contact\n4. Update contact\n5. Delete contact\n"))

    cases = {
        1: add,
        2: view,
        3: search,
        4: update,
        5: delete
    }

    selected_case = cases.get(choice, default)
    selected_case()
