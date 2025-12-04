#1
print("Nothing \nwill work \nunless you do")

#2
# \" - для того, щоб ввести лапку всередину рядка
print("\"Anyone who \n\tstops \n\tlearning is old, \n\twhether at twenty or eighty\"\n\tHenry Ford")
#
#3
# float(input(... - для того, щоб пайтон приймав і дробові значення number  не лякався дробового значення у result
number = float(input("Enter a metr - "))
result_1 = number*100
result_2 = number*10
result_3 = number*1000
result_4 = number/1609
print(result_1 , "см ," , result_2 , "дм ," , result_3 , "мм , " , result_4 , "милі .")

#4
diagonal_1 = int(input("Enter a diamond's diagonal_1 - "))
diagonal_2 = int(input("Enter a diamond's diagonal_2 - "))
diamond_area = (diagonal_1*diagonal_2)/2
print("Diamond's area is" , diamond_area)

#5
num1 = int(input("Enter your salary - "))
num2 = int(input("Enter your the amount of the monthly payment on a bank loan - "))
num3 = int(input("Enter your debt for utility services - "))
num4 = num1 - (num2 + num3)
print("You will have" , num4 , "hryvnias .")

#6
# підсумкова вартість = ((відстань\100 км)) * витрата на 100 км) * вартість 1 л бензину
distance = int(input("Enter your distance traveled -"))
consumption = int(input("Enter your gasoline consumption per 100 km -"))
price = int(input("Enter your price per liter of gasoline -"))
cost = ((distance/100)*consumption)*price
print("The cost of the trip is", cost , "hryvnias.")

