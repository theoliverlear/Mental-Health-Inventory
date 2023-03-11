def major_depressive_disorder():
    print(line_divider_text)
    print("This is the start of the Major Depressive Disorder inventory...")

    # Question 1

    print(line_divider_text)
    question_one_correct_input = False
    while not question_one_correct_input:
        print(on_a_scale_text)
        question_one = input("\n   Within the past two weeks, have you experienced a depressed episode, most of the "
                             "day or nearly every day, having feelings such as sadness, emptiness, "
                             "or hopelessness?\n\nAnswer: ")
        question_one_value = int(question_one)
        if question_one_value > 5 or question_one_value < 1:
            print(correct_input_text)
            question_one_correct_input = False
            continue
        else:
            question_one_correct_input = True

    # Question 2

    print(line_divider_text)
    question_two_correct_input = False
    while not question_two_correct_input:
        print(on_a_scale_text)
        question_two = input("\n   Have you lost interest or pleasure in all, or almost all, activities most of the "
                             "day, nearly everyday?\n\nAnswer: ")
        question_two_value = int(question_two)
        if question_two_value > 5 or question_two_value < 1:
            print(correct_input_text)
            question_two_correct_input = False
            continue
        else:
            question_two_correct_input = True

    # Question 3

        print(line_divider_text)
        question_three_correct_input = False
        while not question_three_correct_input:
            print(on_a_scale_text)
            question_three = input(
                "\n   Have you had significant weight loss or weight gain or a decrease or increase in appetite "
                "nearly every day?\n\nAnswer: ")
            question_three_value = int(question_three)
            if question_three_value > 5 or question_three_value < 1:
                print(correct_input_text)
                question_three_correct_input = False
                continue
            else:
                question_three_correct_input = True

    # Question 4

            print(line_divider_text)
            question_four_correct_input = False
            while not question_four_correct_input:
                print(on_a_scale_text)
                question_four = input(
                    "\n   Have you had insomnia or hypersomnia nearly every day?\n\nAnswer: ")
                question_four_value = int(question_four)
                if question_four_value > 5 or question_four_value < 1:
                    print(correct_input_text)
                    question_four_correct_input = False
                    continue

                else:
                    question_four_correct_input = True

    # Question 5

            print(line_divider_text)
            question_five_correct_input = False
            while not question_five_correct_input:
                print(on_a_scale_text)
                question_five = input(
                    "\n   Have you been fatigued or had loss over energy nearly every day?\n\nAnswer: ")
                question_five_value = int(question_five)
                if question_five_value > 5 or question_five_value < 1:
                    print(correct_input_text)
                    question_five_correct_input = False
                    continue

                else:
                    question_five_correct_input = True

    # Question 6

            print(line_divider_text)
            question_six_correct_input = False
            while not question_six_correct_input:
                print(on_a_scale_text)
                question_six = input(
                    "\n   Have you had feelings of worthlessness or guilt nearly every day?\n\nAnswer: ")
                question_six_value = int(question_six)
                if question_six_value > 5 or question_six_value < 1:
                    print(correct_input_text)
                    question_six_correct_input = False
                    continue

                else:
                    question_six_correct_input = True

    # Question 7

            print(line_divider_text)
            question_seven_correct_input = False
            while not question_seven_correct_input:
                print(on_a_scale_text)
                question_seven = input(
                    "\n   Have you had a diminished ability to think or concentrate or have indecisiveness nearly "
                    "every day?\n\nAnswer: ")
                question_seven_value = int(question_seven)
                if question_seven_value > 5 or question_seven_value < 1:
                    print(correct_input_text)
                    question_seven_correct_input = False
                    continue

                else:
                    question_seven_correct_input = True

    # Question 8

            print(line_divider_text)
            question_eight_correct_input = False
            while not question_eight_correct_input:
                print(on_a_scale_text)
                question_eight = input(
                    "\n   Have you had recurrent thoughts of death or suicide without a specific plan, "
                    "suicide attempt, or plan to commit suicide?\n\nAnswer: ")
                question_eight_value = int(question_eight)
                if question_eight_value > 5 or question_eight_value < 1:
                    print(correct_input_text)
                    question_eight_correct_input = False
                    continue

                else:
                    question_eight_correct_input = True

    # Question 9

            print(line_divider_text)
            question_nine_correct_input = False
            while not question_nine_correct_input:
                print(on_a_scale_text)
                question_nine = input(
                    "\n   Psychomotor agitation or retardation (slowing down or hampering of physical activities) "
                    "nearly every day?\n\nAnswer: ")
                question_nine_value = int(question_nine)
                if question_nine_value > 5 or question_nine_value < 1:
                    print(correct_input_text)
                    question_nine_correct_input = False
                    continue

                else:
                    question_nine_correct_input = True

    print("You have completed the Major Depressive Disorder inventory.")

print("Welcome to the Mental Health Inventory program!")
print("We make our suggested diagnoses according to the DSM-5. Please seek a mental health professional for official "
      "diagnosis.")

on_a_scale_text = "On a scale from 1 to 5 where 1 is not at all, 2 is a mild, 3 is somewhat severe, 4 is severe, " \
                  "and 5 is very severe, where do your symptoms rate according to the following statement: "
correct_input_text = "\nPlease enter a number from range 1 to 5.\n"
line_divider_text = "-----------------------------------------------------------------------------------------------" \
                    "--------------------------------------------------------------------------------------"
print(line_divider_text)
correct_input_inventory_choice = False
while not correct_input_inventory_choice:
    inventory_choice = input("Please enter the number for the corresponding inventory...\n0. Completed Inventory\n1. "
                             "Major Depressive Disorder\n")
    if int(inventory_choice) == 0:
        correct_input_inventory_choice = True
        break
    elif int(inventory_choice) == 1:
        major_depressive_disorder()
    else:
        print("Please enter a number listed.")

# Reverse score such as 5=1/ 1=5 ect. This is not an official test to diagnosis you with
# depression. Please see your PCP or go to a doctor to get official diagnosed with a mental health disorder. Your scores
# will not be saved to respect your privacy and to not violate HIPPA.