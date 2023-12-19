line_divider_text = "------------------------------------------------------------------------------------------------" \
                    "-------------------"
on_a_scale_text = "On a scale from 0 to 4 where 0 is not at all, 1 is a mild, 2 is somewhat severe, 3 is severe, " \
                  "and 4 is very severe,\nwhere do your symptoms rate according to the following statement: "
correct_input_text = "\nPlease enter a number from range 0 to 4.\n"
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


def persistent_depressive_disorder():
    # Also known as Dysthymia
    print(line_divider_text)
    score = 0
    print("This is the start of the Persistent Depressive Disorder inventory...")
    questions = ["Have you had a depressed mood for most of the day, for more days than not, as indicated by either "
                 "\n   subjective account or observation by others for at least two years."
            ,    "Presence while depressed of two or more of the following:\n"
                 " * Poor appetite or over eating?\n"
                 " * Insomnia or hypersomnia?\n"
                 " * Low energy or fatigue?\n"
                 " * Low self-esteem?\n"
                 " * Poor concentration or difficulty making decisions?\n"
                 " * Feelings of hopelessness?"
            ,
                 "Has the criteria of Major Depressive Disorder been present for more than two years?"
            ,
                 "Has there never been a manic or hypomanic episode and criteria has never been met for a cyclothymic "
                 "disorder?"
                 ]
    for question in questions:
        score += prompt(question)
    print("You have completed the Persistent Depressive Disorder inventory.\n"
          "You've scored " + str(score) + " out of 36. This indicates you... ...have Persistent Depressive Disorder.")
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

