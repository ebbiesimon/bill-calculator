print("Enter the type of bill you want to calculate:")
print("1) Electricity Bill")
print("2) Water Bill")
choice = int(input ("Your Choice: "))
if choice == 1:
  user_electric_meter_reading = input ("Enter your electric meter reading in kwH: ")
  user_number_household_members = int(input ("Enter the number people in your household - 20 max people "))
  if user_electric_meter_reading.isdigit():
    user_electric_meter_reading = float(user_electric_meter_reading)
    print ("Calculating Water bill...")
    if user_electric_meter_reading <= 100: 
      users_electric_bill = user_electric_meter_reading * 5 * user_number_household_members 
      print ("Your total Electricity bill is " + 
 str(users_electric_bill))
      user_bill_per_person = users_electric_bill / user_number_household_members
      print ("Your user bill per person is " + str (user_bill_per_person))
    elif user_electric_meter_reading > 100 and user_electric_meter_reading <= 1000:
      users_electric_bill = user_electric_meter_reading * 10 * user_number_household_members
      print ("Your total Electricity bill is " + str(users_electric_bill))
      user_bill_per_person = users_electric_bill / user_number_household_members
      print ("Your user bill per person is " + str (user_bill_per_person))
    elif user_electric_meter_reading > 1000:
      users_electric_bill = user_electric_meter_reading * 15 * user_number_household_members
      print ("Your total Electricity bill is " + str(users_electric_bill))
      user_bill_per_person = users_electric_bill / user_number_household_members
      print ("Your user bill per person is " + str (user_bill_per_person))
  else:
     print ("error: Please enter a numerical meter reading")
elif choice == 2:
  user_water_meter_reading = input ("Enter your water meter reading in m^3: ")
  user_number_household_members = int(input ("Enter the number people in your household - 20 max people "))
  if user_water_meter_reading.isdigit():
    user_water_meter_reading = float(user_water_meter_reading)
    print ("Calculating Water bill...")
    if user_water_meter_reading <= 500: 
        users_water_bill = user_water_meter_reading * 50 * user_number_household_members
        print ("Your total Water bill is " + str(users_water_bill))
        user_bill_per_person = users_water_bill_bill /user_number_household_members
        print ("Your user bill per person is " + str (user_bill_per_person))
    elif user_water_meter_reading > 500 and user_water_meter_reading <= 2500:
        users_water_bill = user_water_meter_reading * 60 * user_number_household_members
        print ("Your total Water bill is " + str(users_water_bill))
        user_bill_per_person = users_water_bill_bill / user_number_household_members
        print ("Your user bill per person is " + str (user_bill_per_person))
    elif user_water_meter_reading >= 2500:
        users_water_bill = user_water_meter_reading * 70 * user_number_household_members
        print ("Your total Water bill is " + str(users_water_bill))
        user_bill_per_person = users_water_bill_bill / user_number_household_members
        print ("Your user bill per person is " + str (user_bill_per_person))
  else:
     print ("error: Please enter a numerical meter reading")
else:
  print ("error: Enter a number to choose a bill type from the list")
