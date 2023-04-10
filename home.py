def major_depressive_disorder():
    print(line_divider_text)
    score = 0
    print("This is the start of the Major Depressive Disorder inventory...")
    questions = ["Within the past two weeks, have you experienced a depressed episode, most of the "
                 "day or nearly every day, having feelings such as sadness, emptiness, "
                 "or hopelessness?"

        , "Have you lost interest or pleasure in all, or almost all, activities most of the "
          "day, nearly everyday?"

        , "Have you had significant weight loss or weight gain or a decrease or increase in appetite "
          "nearly every day?"

        , "Have you had insomnia or hypersomnia nearly every day?"

        , "Have you been fatigued or had loss over energy nearly every day?"

        , "Have you had feelings of worthlessness or guilt nearly every day?"

        , "Have you had a diminished ability to think or concentrate or have indecisiveness nearly "
          "every day?"

        , "Have you had recurrent thoughts of death or suicide without a specific plan, "
          "suicide attempt, or plan to commit suicide?"
        , "Psychomotor agitation or retardation (slowing down or hampering of physical activities) "
          "nearly every day?"
                 ]
    for question in questions:
        score += prompt(question)
    print("You have completed the Major Depressive Disorder inventory.\n"
          "You've scored " + str(score) + " out of 36. This indicates you... ...have Major Depressive Disorder.")


def prompt(question):
    print(line_divider_text)
    correct_input = False
    while not correct_input:
        print(on_a_scale_text)
        answer = input(
            "\n   " + question + "\n\nAnswer: ")
        answer_value = int(answer)
        if answer_value > 4 or answer_value < 0:
            print(correct_input_text)
            correct_input = False
            continue
        else:
            correct_input = True
    return answer_value


print("Welcome to the Mental Health Inventory program!")
print("We make our suggested diagnoses according to the DSM-5. Please seek a mental health professional for official "
      "diagnosis.")

on_a_scale_text = "On a scale from 0 to 4 where 0 is not at all, 1 is a mild, 2 is somewhat severe, 3 is severe, " \
                  "and 4 is very severe, where do your symptoms rate according to the following statement: "
correct_input_text = "\nPlease enter a number from range 0 to 4.\n"
line_divider_text = "-----------------------------------------------------------------------------------------------" \
                    "--------------------------------------------------------------------------------------"
print(line_divider_text)
correct_input_inventory_choice = False
while not correct_input_inventory_choice:
    inventory_choice = input("Please enter the number for the corresponding inventory...\n"
                             "0. Complete Inventory\n"
                             "1. Major Depressive Disorder\n")
    if int(inventory_choice) == 0:
        correct_input_inventory_choice = True
        break
    elif int(inventory_choice) == 1:
        major_depressive_disorder()
    else:
        print("Please enter a number listed.")

# Reverse score such as 5=1/ 1=5 ect. This is not an official test to diagnosis you with
# depression. Please see your PCP or go to a doctor to get official diagnosed with a mental health disorder. Your scores
# will not be saved to respect your privacy and to not violate HIPAA.
