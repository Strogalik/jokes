import os
import random

def show_location_home():
	# описываем место
	os.system("cls")
	print("Вы дома")
	print("1 - в казино")
	print("2 - ждать")

	# спросить пользователя
	user_choice = ""
	while user_choice not in ("1", "2"):
		user_choice = input("введите номер варианта и нажмите Enter ")

	# проверить ответ пользователя
	if user_choice == "1":
		show_location_casino()
	else:
		print("жду")
		os.system("cls")
		show_location_home()


def show_location_casino():
	# описываем место
	os.system("cls")
	print("Вы в казино")
	print("1 - домой")
	print("2 - ждать")
	print("3 - сыграть")

	# спросить пользователя
	user_choice = ""
	while user_choice not in ("1", "2", "3"):
		user_choice = input("введите номер варианта и нажмите Enter ")

	# проверить ответ пользователя
	if user_choice == "1":
		show_location_home()
	elif user_choice == "2":
		print("жду")
		os.system("cls")
		show_location_casino()
	else:
		show_gamble()


def show_gamble():
	casito_bank = 100000
	user_money = int(input("Ввдедите сумму для игры\n"))
	if user_money > 5000:
		print("Сделайте ставку меньше")
	else:
		print("У вас на входе", user_money)
		user_dice = random.randint(2, 12)
		casino_dice = random.randint(2, 12)
		print(f"Вы бросили кости, выпало {user_dice}")
		print(f"Казино кости, выпало {casino_dice}")
		if user_dice > casino_dice:
			print("Вы победили и получили", user_money * x)
		elif user_dice < casino_dice:
			print(f"Вы проиграли, у вас тпереь {user_money * x0}")
		else:
			print(f"Ничья, у вас {user_money} денег")
	input("Нажмите ENTER чтобы вернуться в казино")
	show_location_casino()


# игра началась здесь
user_name = "Вася"
x =  random.randint(1, 5)
x0 = 0
show_location_home()
