def display_console(fichier):
    """This print the content of the level.txt file. This function is used for MVP demonstration, you have to enter a
    position for the ball until all the x are removed.

    PRE :
        file named level.txt in "data" folder
        level.txt is == "x x x x x x x x x x x x x
                         x x x x x x x x x x x x x
                         x x x x x x x x x x x x x
                         x x x x x x x x x x x x x"
    POST :
        return END if not x in list_of_all_lists

    RAISES :
        ValueError if level.txt has been modified
        FileNotFoundError not level.txt in data
        IOError if not level.txt in data

    """
    try:
        with open(fichier, "r") as file:
            list_ball = [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']
            list_of_lists = []

            # Main display
            for line in file:
                stripped_line = line.strip()
                line_list = stripped_line.split()
                list_of_lists.append(line_list)

            for elem in list_of_lists:
                if elem != ['x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x']:
                    raise ValueError("The level.txt file has been modified, please keep original version !")

            end = False
            while end is not True:

                # Place the ball at the index indicated by the user
                response = input("Quelle position attribuez vous à la balle ?  ")
                # Checks if the user enters a number between 1 and 13
                if 13 >= int(response) > 0:
                    end = False
                    touch = False
                    list_ball[int(response) - 1] = "*"
                    index_ball = list_ball.index("*")
                    while not end:
                        if str(list_of_lists[3][index_ball]) == "x":
                            list_of_lists[3][index_ball] = "-"
                            touch = True

                        if str(list_of_lists[2][index_ball]) == "x":
                            if not touch:
                                list_of_lists[2][index_ball] = "-"
                                touch = True

                        if str(list_of_lists[1][index_ball]) == "x":
                            if not touch:
                                list_of_lists[1][index_ball] = "-"
                                touch = True

                        if str(list_of_lists[0][index_ball]) == "x":
                            if not touch:
                                list_of_lists[0][index_ball] = "-"
                                touch = True
                        end = True

                    print(' '.join(map(str, list_of_lists[0])))
                    print(' '.join(map(str, list_of_lists[1])))
                    print(' '.join(map(str, list_of_lists[2])))
                    print(' '.join(map(str, list_of_lists[3])))

                    print(' '.join(map(str, list_ball)))
                    list_ball[int(response) - 1] = ' '
                    print("\n")

                    for elem in list_of_lists:
                        if 'x' in elem:
                            end = False
                        else:
                            end = True
                    if end:
                        print("END")
                else:
                    print("Please enter a number between 1 and 13 inclusive!")
                    break
    except FileNotFoundError:
        return 'File not found !'
    except IOError:
        return 'Error IO.'
