# Create three strings using three different methods. Save your result to result_string_1, result_string_2,
# result_string_3 variables

result_string_1 = 'string'
result_string_2 = "String"
result_string_3 = '''STRING'''


# Enter your first and  last name. Join them together with a space in
# between. Save a result in a variable result_full_name and
# save the length of the whole name in result_full_name_length variable.

first_name = "Daniel "
last_name = "Smith"
result_full_name = first_name + last_name
print(result_full_name)
result_full_name_length = len(result_full_name)
print(result_full_name_length)


# Enter the capital city of California State in lower case. Change the case to title case.
# Save the result in result_ca_capital variable

result_ca_capital = str.title("sacramento")
print(result_ca_capital)



# Enter the name of our planet. Change the case to upper case. Save the result in
# result_planet variable

result_planet = str.upper("Earth")
print(result_planet)
