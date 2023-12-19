import depressive as depressive

print("Welcome to the Mental Health Inventory program!")
print("We make our suggested diagnoses according to the DSM-5. Please seek a mental health professional for official "
      "diagnosis.")

on_a_scale_text = "On a scale from 0 to 4 where 0 is not at all, 1 is a mild, 2 is somewhat severe, 3 is severe, " \
                  "and 4 is very severe,\nwhere do your symptoms rate according to the following statement: "
correct_input_text = "\nPlease enter a number from range 0 to 4.\n"
line_divider_text = "------------------------------------------------------------------------------------------------" \
                    "-------------------"

print(line_divider_text)
correct_input_inventory_choice = False
while not correct_input_inventory_choice:
    inventory_choice = input("Please enter the number for the corresponding inventory...\n"
                             "0. Complete Inventory\n"
                             "1. Major Depressive Disorder\n"
                             "2. Persistent Depressive Disorder\n")
    inventory_choice_int = int(inventory_choice)
    if inventory_choice_int == 0:
        correct_input_inventory_choice = True
        break
    elif inventory_choice_int == 1:
        depressive.major_depressive_disorder()
    elif inventory_choice_int == 2:
        depressive.persistent_depressive_disorder()
    else:
        print("Please enter a number listed.")

# Reverse score such as 5=1/ 1=5 ect. This is not an official test to diagnosis you with
# depression. Please see your PCP or go to a doctor to get official diagnosed with a mental health disorder. Your scores
# will not be saved to respect your privacy and to not violate HIPAA.
