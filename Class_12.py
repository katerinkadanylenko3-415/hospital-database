# винятки
# try except

# try:
#     some bad code
#
# except:
#     what to do with error

# try:
#     amount = int(input("enter amount of received items: "))
#     items_type = input("enter type of items: ")
#     parts_number = int(input("enter the number of parts: "))
#     parts_amount = amount / parts_number
#     print(f"Supply of {amount}, {items_type} saved!")
# except:
#     print("please enter numeric value")



# try:
#     amount = int(input("enter amount of received items: "))
#     items_type = input("enter type of items: ")
#     parts_number = int(input("enter the number of parts: "))
#     parts_amount = amount / parts_number
#     print(f"Supply of {amount}, {items_type} saved!")
# except ValueError:
#     print("please enter numeric value")
# except ZeroDivisionError:
#     print("Cant divide by zero")
# except Exception:
#     print("Something went wrong")
# finally:
#     print("Program had finished")

# try:
#     num = int(input("enter number - "))
#     print(num**2)
# except ValueError:
#     print("need a number")
# else: # working if no error
#     print("All is good")
# finally: # always working
#     print("Program had finished")


# try:
#     salary = int(input("enter salary: "))
#     if salary < 0:
#         raise Exception("salary must be possitive")
# except Exception as ex:
#     print("Error: ", ex)

#
# print("Final price calculating")
# try:
#     price = float(input("Enter start product price of: "))
#     discount = float(input("Enter discount price of discount: "))
#     if discount < 0 or discount > 100:
#         raise ValueError("discount price of discount must be between 0 and 100")
#     final_price = price * (1 - discount / 100)
#     print(f"Final price is: {final_price:.2f} uah")
# except ValueError as ex:
#     print(f"Input error: {ex}")
# except:
#     print("We have some error")
# finally:
#     print("Calculating is finished")


# try:
#     num = float(input("Введіть суму в доларах (USD): "))
#     euro = float(input("Введіть курс обміну (EUR за 1 USD): "))
#     if num < 0:
#         raise ValueError("Your number cant be negative, please try again.")
#     if euro == 0:
#         raise Exception("Курс обміну не може дорівнювати нулю.")
#     final_num = num * euro
#     print("Your final number is:", final_num)
# except ValueError as ex:
#     print(f"Input error: {ex}")
# except:
#     print("Something went wrong.")
# finally:
#     print("Calculating has finished. Goodbye!")



grades_input = input("Введіть оцінки студентів через пробіл: ")
try:
    grades_str_list = grades_input.split()

    if grades_str_list < 0:
        raise Exception("Your marks cant be negative")
    if not grades_str_list:
        raise Exception("Your marks cant be empty")
    total_sum = sum(grades_str_list)
    count = len(grades_str_list)
    average = total_sum / count
    print(f"Середнє значення оцінок: {average:.2f}")

except ZeroDivisionError as ex:
    print(f"Помилка обчислення: {ex}")

except Exception:
    print("Сталася невідома помилка.")

finally:
    print("Завершення обчислень")







