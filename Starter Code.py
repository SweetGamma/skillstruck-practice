user_input = input("Enter 5 strings separated by spaces: ")


strings = user_input.split()


if len(strings) != 5:
   print("Please enter exactly 5 strings.")
else:
   first_item = strings[0]
   last_item = strings[-1]
   print(f"Some animals {first_item} and some {last_item}")
