from difflib import SequenceMatcher


def comparefile(COMPARISION_FILE):
    with open(COMPARISION_FILE) as TO_BE_CHECKED, open("B1.csv") as BOOK1, open("B2.csv") as BOOK2, open("B3.csv") as BOOK3, open("B4.csv") as BOOK4, open("B5.csv") as BOOK5, open("B6.csv") as BOOK6, open("B7.csv") as BOOK7, open("B8.csv") as BOOK8, open("B9.csv") as BOOK9, open("B10.csv") as BOOK10:
        MAIN_VARIABLE = TO_BE_CHECKED.read()
        TEMP_BOOK1 = BOOK1.read()
        TEMP_BOOK2 = BOOK2.read()
        TEMP_BOOK3 = BOOK3.read()
        TEMP_BOOK4 = BOOK4.read()
        TEMP_BOOK5 = BOOK5.read()
        TEMP_BOOK6 = BOOK6.read()
        TEMP_BOOK7 = BOOK7.read()
        TEMP_BOOK8 = BOOK8.read()
        TEMP_BOOK9 = BOOK9.read()
        TEMP_BOOK10 = BOOK10.read()

        print("The inserted data is : ", MAIN_VARIABLE)

        sum1 = SequenceMatcher(None, MAIN_VARIABLE, TEMP_BOOK1).ratio()
        sum2 = SequenceMatcher(None, MAIN_VARIABLE, TEMP_BOOK2).ratio()
        sum3 = SequenceMatcher(None, MAIN_VARIABLE, TEMP_BOOK3).ratio()
        sum4 = SequenceMatcher(None, MAIN_VARIABLE, TEMP_BOOK4).ratio()
        sum5 = SequenceMatcher(None, MAIN_VARIABLE, TEMP_BOOK5).ratio()
        sum6 = SequenceMatcher(None, MAIN_VARIABLE, TEMP_BOOK6).ratio()
        sum7 = SequenceMatcher(None, MAIN_VARIABLE, TEMP_BOOK7).ratio()
        sum8 = SequenceMatcher(None, MAIN_VARIABLE, TEMP_BOOK8).ratio()
        sum9 = SequenceMatcher(None, MAIN_VARIABLE, TEMP_BOOK9).ratio()
        sum10 = SequenceMatcher(None, MAIN_VARIABLE, TEMP_BOOK10).ratio()

        RES1 = sum1*100
        RES2 = sum2*100
        RES3 = sum3*100
        RES4 = sum4*100
        RES5 = sum5*100
        RES6 = sum6*100
        RES7 = sum7*100
        RES8 = sum8*100
        RES9 = sum9*100
        RES10 = sum10*100

        return RES1, RES2, RES3, RES4, RES5, RES6, RES7, RES8, RES9, RES10
