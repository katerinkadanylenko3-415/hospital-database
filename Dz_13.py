# робота з файлами

file_name = "main.txt"

# file = open(file_name, 'w')
# file.write("some text")
# file.close()

# try:
#     file = open(file_name, 'a')
#     file.write("some text\n")
#     file.close()
# except:
#     print("cant open")
# finally:
#     file.close()
# file = open(file_name, 'r')
# info = file.read()
# print(info)
# file.close()

# my_list = ["line1\n", "line2\n", "line3\n"]
#
# file = open(file_name, 'w+')
# file.writelines(my_list)
#
# # data_list = file.readlines()
# # print(data_list)
# file.close()
#
# file = open(file_name)
# file.seek(6)
# print(file.tell())
# data1 = file.read(6)
# print(file.tell())
# data2 = file.read(6)
# print(file.tell())
# print(data1, data2)
# file.close()
#
#
# with open(file_name, 'r') as file:
#     print(file.read())
#
# try:
#     with open('main.txt', 'r') as outfile, open('main.txt', 'w') as infile:
#         data = outfile.read()
#         infile.write(data.lower())
#
# except (FileNotFoundError, FileExistsError) as ex:
#     print(ex)
#


def add_contact(name, phone):
    try:
        with open('contacts.txt', 'a', encoding='utf-8') as f:
            f.write(f"{name}: {phone}\n")
        print("New contact added successfully")

    except Exception as ex:
        print("Error with writing",ex)


def show_all_contacts():
    try:
        with open('contacts.txt', 'r', encoding='utf-8') as f:
            data = f.readline()
            if data.strip() == "":
                print("empty data")
            else:
                print("----------All Contacts----------")
                print(data)
                for count in range(1, len(data)+1):
                    print(f"{count}, {data[count-1]}")
    except FileNotFoundError:
        print("File not found")


def find_contact(name):
    try:
        with open('contacts.txt', 'r', encoding='utf-8') as f:
            for line in f:
                if line.lower().startswith(name.lower()):
                    print("Find:", line.strip())
                    return
                print("not found")
    except FileNotFoundError:
        print("File not found")

import csv

def export_to_csv(txt_file="contacts.txt", csv_file="contacts.csv"):
    try:
        contacts = []

        with open(txt_file, 'r', encoding='utf-8') as f:
            for line in f:
                line = line.strip()
                if line:
                    name, phone = line.split(':')
                    contacts.append([name.string(), phone.string()])
        with open(csv_file, 'w', encoding='utf-8') as f:
            writer = csv.writer(f)
            writer.writerows(['name', 'phone'])
            writer.writerows(contacts)
        print(f"Export finished!")

    except FileNotFoundError:
        print("File not found")
    except Exception as ex:
        print(ex)


def menu():
    while True:
        print("------------Contact book------------")
        print("1. Add new Contact")
        print("2. Show All Contacts")
        print("3. Exit")

        choice = input("Enter your number of choice: ")
        if choice == '1':
            name = input("Enter your name: ")
            phone = input("Enter your phone number: ")
            add_contact(name, phone)

        elif choice == '2':
            show_all_contacts()

        elif choice == '3':
            break
        elif choice == '4':
            name = input("Enter your name: ")
            find_contact(name)

        elif choice == '5':
            name = input("Enter your name: ")
            del_contact(name)

        else:
            print("Error menu choice")

menu()



