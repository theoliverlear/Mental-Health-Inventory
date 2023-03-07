def major_depressive_disorder():
    print(line_divider_text)
    print("This is the start of the Major Depressive Disorder inventory...")
    question_one_correct_input = False
    while not question_one_correct_input:
        print(on_a_scale_text)
        question_one = input("\n   Within the past two weeks, have you experienced a depressed episode, most of the day or "
                             "nearly every day, having feelings such as sadness, emptiness, or hopelessness?\n\nAnswer: ")
        question_one_value = int(question_one)
        if question_one_value > 5 or question_one_value < 1:
            print(correct_input_text)
            question_one_correct_input = False
        else:
            question_one_correct_input = True

    print(line_divider_text)
    question_two_correct_input = False
    while not question_two_correct_input:
        print(on_a_scale_text)
        question_two = input("\n   Have you lost interest or pleasure in all, or almost all, activities most of the day, "
                             "nearly everyday?\n\nAnswer: ")
        question_two_value = int(question_two)
        if question_two_value > 5 or question_two_value < 1:
            print(correct_input_text)
            question_two_correct_input = False
        else:
            question_two_correct_input = True


print("Welcome to the Mental Health Inventory program!")
print("We make our suggested diagnoses according to the DSM-5.")

on_a_scale_text = "On a scale from 1 to 5 where 1 is not at all, 2 is a mild, 3 is somewhat severe, 4 is severe, " \
                  "and 5 is very severe, where do your symptoms rate according to the following statement: "
correct_input_text = "Please enter a number from range 1 to 5."
line_divider_text = "-----------------------------------------------------------------------------------------------" \
                    "--------------------------------------------------------------------------------------"
print(line_divider_text)
inventory_choice = input("Please enter the number for the corresponding inventory...\n1. Major Depressive Disorder\n")
correct_input_inventory_choice = False
while not correct_input_inventory_choice:
    if int(inventory_choice) == 1:
        major_depressive_disorder()
    else:
        print("Please enter a number listed.")

# Reverse score such as 5=1/ 1=5 ect. This is not an official test to diagnosis you with
# depression. Please see your PCP or go to a doctor to get official diagnosed with a mental health disorder. Your scores
# will not be saved to respect your privacy and to not violate HIPPA.