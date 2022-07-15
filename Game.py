def game():
    import random
    SetA = (1,11)
    A = (random.sample(SetA, 1))
    Cards = ("A", "J", "Q", "K")
    Computer = random.randint(2,10)
    Computer_2 = ''.join(random.sample(Cards, 1))
    You = random.randint(2,10)
    You_2 = (''.join(random.sample(Cards, 1)))
    VarYou = You_2
    print("Computer: ", Computer, 'Sum = ', Computer)
    RandomChooserForA = A
    if (VarYou == "A"):
        if (RandomChooserForA == [1]):
            VarYou = 1
        if (RandomChooserForA == [11]):
            VarYou = 11
    elif (VarYou == "J" or "Q" or "K"):
        VarYou = 10
    YouSum = You + VarYou
    print("You:      ", You, You_2,'Sum = ', YouSum)
    if YouSum == 21:
        print("You Won As You Got To 21 First.")
        game()
    Varcomp = Computer_2
    if (Varcomp == "A"):
        RandomChooserForA = A
        if (RandomChooserForA == [1]):
            Varcomp = 1
        if (RandomChooserForA == [11]):
            Varcomp = 11
    elif (Varcomp == "J" or "Q" or "K"):
        Varcomp = 10
    CompSum = Computer + Varcomp
    if YouSum < 21:
        desicion3 = input("Hit or Stand: ")
        UPPERcase = desicion3.upper()
        j = 0
        while j == 0:
            if UPPERcase != 'HIT':
                if UPPERcase != 'STAND':
                    print("Enter a propper command: ")
                    desicion3 = input("Hit or Stand: ")
                    UPPERcase = desicion3.upper()
                else:
                    j += 1
            else:
                j += 1
        if (UPPERcase == 'HIT'):
            Escapeset = ('Number', 'Letter')
            EscapesetValue = ''.join(random.sample(Escapeset,1))
            if EscapesetValue == 'Number':
                You_3 = random.randint(2,10)
                YouSum = YouSum + You_3
                y1 = print('You:     ', You, You_2, You_3, "Sum = ", YouSum)
                if YouSum == 21:
                    print ("You Won As You Got To 21 First.")
                    game()
                if YouSum > 21:
                    print ("You Lost As You Got Over 21 And Busted.")
                    game()
            elif EscapesetValue == 'Letter':
                Varyou = (''.join(random.sample(Cards, 1)))
                You_3 = Varyou
                if (Varyou == "A"):
                    RandomChooserForA = A
                    if (RandomChooserForA == [1]):
                        Varyou = 1
                    if (RandomChooserForA == [11]):
                        Varyou = 11
                elif (Varyou == "J" or "Q" or "K"):
                    Varyou = 10
                YouSum = YouSum + Varyou
                y1 = print('You:     ', You, You_2, You_3, "Sum = ", YouSum)
                if YouSum == 21:
                    print ("You Won As You Got To 21 First.")
                    game()
                if YouSum > 21:
                    print ("You Lost As You Got Over 21 And Busted.")
                    game()
        elif (UPPERcase == 'STAND'):
            print('You:     ', You, You_2, "Sum = ", YouSum)
    if CompSum < 21:
        alpha = ('Hit', 'Stand')
        if CompSum <= 15:
            desicion2 = 'Hit'
        if CompSum >= 16:
            desicion2 = 'Stand'
            if CompSum == YouSum:
                desicion2 = 'Hit'
        if CompSum == YouSum:
            desicion2 = 'Hit'
        if desicion2 == 'Hit':
            Escapeset = ('Number', 'Letter')
            EscapesetValue = ''.join(random.sample(Escapeset,1))
            if EscapesetValue == 'Number':
                Computer_3 = random.randint(2,10)
                CompSum = CompSum + Computer_3
                c1 = print('Computer:  ', Computer, Computer_2, Computer_3, "Sum = ", CompSum)
                if CompSum == 21:
                    print("You Lost As The Computer Got To 21 First.")
                    game()
                if CompSum > 21:
                    print ("You Won As The Computer Got Over 21 And Busted.")
                    game()
            elif EscapesetValue == 'Letter':
                VarComp = (''.join(random.sample(Cards, 1)))
                Computer_3 = VarComp
                if (VarComp == "A"):
                    RandomChooserForA = A
                    if (RandomChooserForA == [1]):
                        VarComp = 1
                    if (RandomChooserForA == [11]):
                        VarComp = 11
                elif (VarComp == "J" or "Q" or "K"):
                    VarComp = 10
                CompSum = CompSum + VarComp
                c1 = print('Computer: ', Computer, Computer_2, Computer_3, "Sum = ", CompSum)
                if CompSum == 21:
                    print ("You Lost As The Computer Got To 21 First.")
                    game()
                if CompSum > 21:
                    print ("You Won As The Computer Got Over 21 And Busted.")
                    game()
        elif desicion2 == "Stand":
            print('Computer: ', Computer, Computer_2, "Sum = ", CompSum)
    if YouSum < 21:
        desicion5 = input("Hit or Stand: ")
        UPPERCase = desicion5.upper()
        j = 0
        while j == 0:
            if UPPERCase != 'HIT':
                if UPPERCase != 'STAND':
                    print("Enter a propper command: ")
                    desicion5 = input("Hit or Stand: ")
                    UPPERCase = desicion5.upper()
                else:
                    j += 1
            else:
                j += 1
        if (UPPERCase == 'HIT'):
            Escapeset = ('Number', 'Letter')
            EscapesetValue = ''.join(random.sample(Escapeset,1))
            if EscapesetValue == 'Number':
                You_4 = random.randint(2,10)
                YouSum = YouSum + You_4
                try:y1
                except NameError:print("You:      ", You, You_2, You_4, "Sum = ", YouSum)
                else:y2 = print("You:      ", You, You_2, You_3, You_4, "Sum = ", YouSum)
                if YouSum == 21:
                    print ("You Won As You Got To 21 First.")
                    game()
                if YouSum > 21:
                    print ("You Lost As You Got Over 21 And Busted.")
                    game()
            elif EscapesetValue == 'Letter':
                Varyyou = (''.join(random.sample(Cards, 1)))
                You_4 = Varyyou
                if (Varyyou == "A"):
                    RandomChooserForA = A
                    if (RandomChooserForA == [1]):
                        Varyyou = 1
                    if (RandomChooserForA == [11]):
                        Varyyou = 11
                elif (Varyyou == "J" or "Q" or "K"):
                    Varyyou = 10
                YouSum = YouSum + Varyyou
                try:y1
                except NameError:print("You:      ", You, You_2, You_4, "Sum = ", YouSum)
                else:y2 = print("You:      ", You, You_2, You_3, You_4, "Sum = ", YouSum)
                if YouSum == 21:
                    print ("You Won As You Got To 21 First.")
                    game()
                if YouSum > 21:
                    print ("You Lost As You Got Over 21 And Busted.")
                    game()
        elif (UPPERCase == 'STAND'):
            try:y1
            except NameError:print("You:      ",You, You_2, "Sum = ", YouSum)
            else:print("You:      ",You, You_2, You_3, "Sum = ", YouSum)
    if CompSum < 21:
        if CompSum <= 15:
            desicion4 = 'Hit'
        if CompSum >= 16:
            desicion4 = 'Stand'
            if CompSum == YouSum:
                desicion4 = 'Hit'
        if CompSum < YouSum:
            desicion4 = 'Hit'
        if CompSum == YouSum:
            desicion4 = 'Hit'
        if desicion4 == 'Hit':
            Escapeset = ('Number', 'Letter')
            EscapesetValue = ''.join(random.sample(Escapeset,1))
            if EscapesetValue == 'Number':
                Computer_4 = random.randint(2,10)
                CompSum = CompSum + Computer_4
                try:c1
                except NameError:print("Computer: ", Computer, Computer_2, Computer_4, "Sum = ", CompSum)
                else:c2 = print("Computer: ", Computer, Computer_2, Computer_3, Computer_4, "Sum = ", CompSum)
                if CompSum == 21:
                    print ("You Lost As The Computer Got To 21 First.")
                    game()
                if CompSum > 21:
                    print ("You Won As The Computer Got Over 21 And Busted.")
                    game()
            elif EscapesetValue == 'Letter':
                Varccomp = (''.join(random.sample(Cards, 1)))
                Computer_4 = Varccomp
                if (Varccomp == "A"):
                    Computer_4 = Varccomp
                    if (RandomChooserForA == [1]):
                        Varccomp = 1
                    if (RandomChooserForA == [11]):
                        Varccomp = 11
                elif (Varccomp == "J" or "Q" or "K"):
                    Varccomp = 10
                CompSum = CompSum + Varccomp
                try:c1
                except NameError:print("Computer: ", Computer, Computer_2, Computer_4, "Sum = ", CompSum)
                else:c2 = print("Computer: ", Computer, Computer_2, Computer_3, Computer_4, "Sum = ", CompSum)
                if CompSum == 21:
                    print ("You Lost As The Computer Got To 21 First.")
                    game()
                if CompSum > 21:
                    print ("You Won As The Computer Got Over 21 And Busted.")
                    game()
        if desicion4 == 'Stand':
            try:c1
            except NameError:print("Computer: ", Computer, Computer_2, "Sum = ", CompSum)
            else:print("Computer: ", Computer, Computer_2, Computer_3, "Sum = ", CompSum)
    if YouSum < 21:
        desicion6 = input("Hit or Stand: ")
        UPPERCAse = desicion6.upper()
        j = 0
        while j == 0:
            if UPPERCAse != 'HIT':
                if UPPERCAse != 'STAND':
                    print("Enter a propper command: ")
                    desicion6 = input("Hit or Stand: ")
                    UPPERCAse = desicion6.upper()
                else:
                    j += 1
            else:
                j += 1
        if (UPPERCAse == 'HIT'):
            Escapeset = ('Number', 'Letter')
            EscapesetValue = ''.join(random.sample(Escapeset,1))
            if EscapesetValue == 'Number':
                You_5 = random.randint(2,10)
                YouSum = YouSum + You_5
                try:y1
                except NameError:
                    try:y2
                    except NameError:print("You:     ", You, You_2, You_5,"Sum = ", YouSum)
                    else:print("You:      ", You, You_2, You_4, You_5,"Sum = ", YouSum)
                else:
                    try:y2
                    except NameError:print("You:     ", You, You_2, You_3, You_5,"Sum = ", YouSum)
                    else:
                        print("You:     ", You, You_2, You_3, You_4, You_5,"Sum = ", YouSum)
                        if YouSum < 21:
                            print("You Won As You Took 5 Cards Without Going Over.")
                            game()
                if YouSum == 21:
                    print("You Won As You Got To 21 First.")
                    game()
                if YouSum > 21:
                    print ("You Lost As You Got Over 21 And Busted.")
                    game()
            elif EscapesetValue == 'Letter':
                Varyyyou = (''.join(random.sample(Cards, 1)))
                You_5 = Varyyyou
                if (Varyyyou == "A"):
                    RandomChooserForA = A
                    if (RandomChooserForA == [1]):
                        Varyyyou = 1
                    if (RandomChooserForA == [11]):
                        Varyyyou = 11
                elif (Varyyyou == "J" or "Q" or "K"):
                    Varyyyou = 10
                YouSum = YouSum + Varyyyou
                try:y1
                except NameError:
                    try:y2
                    except NameError:print("You:     ", You, You_2, You_5,"Sum = ", YouSum)
                    else:print("You:      ", You, You_2, You_4, You_5,"Sum = ", YouSum)
                else:
                    try:y2
                    except NameError:print("You:     ", You, You_2, You_3, You_5,"Sum = ", YouSum)
                    else:
                        print("You:     ", You, You_2, You_3, You_4, You_5,"Sum = ", YouSum)
                        if YouSum < 21:
                            print("You Won As You Took 5 Cards Without Going Over.")
                            game()
                if YouSum == 21:
                    print ("You Won As You Got To 21 First.")
                    game()
                if YouSum > 21:
                    print ("You Lost As You Got Over 21 And Busted.")
                    game()
        elif (UPPERCAse == 'STAND'):
            try:y1
            except NameError:
                try:y2
                except NameError:print("You:      ", You, You_2, "Sum = ", YouSum)                
                else:print("You:      ", You, You_2, You_4, "Sum = ", YouSum)
            else:
                try:y2
                except NameError:print("You:      ", You, You_2, You_3, "Sum = ", YouSum)             
                else:print("You:      ", You, You_2, You_3, You_4, "Sum = ", YouSum)
    if CompSum < 21:
        if CompSum <= 15:
            desicion5 = 'Hit'
        if CompSum >= 16:
            desicion5 = 'Stand'
            if CompSum == YouSum:
                desicion5 = 'Hit'
            if CompSum == YouSum:
                desicion5 = 'Hit'
        if CompSum <= YouSum:
            desicion5 = 'Hit'
        if desicion5 == 'Hit':
            Escapeset = ('Number', 'Letter')
            EscapesetValue = ''.join(random.sample(Escapeset,1))
            if EscapesetValue == 'Number':
                Computer_5 = random.randint(2,10)
                CompSum = CompSum + Computer_5
                try:c1
                except NameError:
                    try:c2
                    except NameError:print("Computer: ", Computer, Computer_2, Computer_5,"Sum = ", CompSum)
                    else:print("Computer: ", Computer, Computer_2, Computer_4, Computer_5,"Sum = ", CompSum)
                else:
                    try:c2
                    except NameError:print("Computer: ", Computer, Computer_2, Computer_3, Computer_5,"Sum = ", CompSum)
                    else:
                        print("Computer: ", Computer, Computer_2, Computer_3, Computer_4, Computer_5,"Sum = ", CompSum)
                        if CompSum < 21:
                            print("The Computer Won As It Took 5 Cards Without Going Over 21")
                            game()
                if CompSum == 21:
                    print("The Computer Won As It Reached 21 First")
                    game()
                if CompSum > 21:
                    print ("You Won As The Computer Got Over 21 And Busted.")
                    game()
            elif EscapesetValue == 'Letter':
                Varcccomp = (''.join(random.sample(Cards, 1)))
                Computer_5 = Varcccomp
                if (Varcccomp == "A"):
                    RandomChooserForA = A
                    if (RandomChooserForA == [1]):
                        Varcccomp = 1
                    if (RandomChooserForA == [11]):
                        Varcccomp = 11
                elif (Varcccomp == "J" or "Q" or "K"):
                    Varcccomp = 10
                CompSum = CompSum + Varcccomp
                try:c1
                except NameError:
                    try:c2
                    except NameError:print("Computer: ", Computer, Computer_2, Computer_5,"Sum = ", CompSum)
                    else:print("Computer: ", Computer, Computer_2, Computer_4, Computer_5,"Sum = ", CompSum)
                else:
                    try:c2
                    except NameError:print("Computer: ", Computer, Computer_2, Computer_3, Computer_5,"Sum = ", CompSum)
                    else:
                        print("Computer: ", Computer, Computer_2, Computer_3, Computer_4, Computer_5,"Sum = ", CompSum)    
                        if CompSum > 21:
                            print("You Won As The Computer Went Overt 21 And Busted.")
                            game()
                        if CompSum < 21:
                            print("The Computer Won As It Took 5 Cards Without Going Over.")
                            game()
                if CompSum == 21:
                    print("You Lost As The Computer Got To 21 First.")
                    game()
                if CompSum > 21:
                    print ("You Won As The Computer Got Over 21 And Busted.")
                    game()
            elif desicion5 == "Stand":
                try:c1
                except NameError:
                    try:c2
                    except NameError:print("Computer: ", Computer, Computer_2, "Sum = ", CompSum)                
                    else:print("Computer: ", Computer, Computer_2, Computer_4, "Sum = ", CompSum)
                else:
                    try:c2
                    except NameError:print("Computer: ", Computer, Computer_2, Computer_3, "Sum = ", CompSum)                
                    else:print("Computer: ", Computer, Computer_2, Computer_3, Computer_4, "Sum = ", CompSum)
    if CompSum and YouSum < 21:
        if YouSum > CompSum:
            print("You Won As You Stood With A Higher Score Than The Computer.")
            game()
        if CompSum > YouSum:
            print("You Lost As You Stood With A Lower Score Than The Computer.")
            game()
        if CompSum == YouSum:
            print("It was a very rare draw!!!")
            game()
game()