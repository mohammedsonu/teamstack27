import string


def encrytpting(TEXT_TO_BE_COMPARED, FILENAME):

    TEMP_TEXT = TEXT_TO_BE_COMPARED.replace(" ", "")
    TEMP_TEXT = TEMP_TEXT.replace("’", "")
    TEMP_TEXT = TEMP_TEXT.replace("\n", "")
    TEMP_TEXT = TEMP_TEXT.replace("'", "")
    TEMP_TEXT = TEMP_TEXT.lower()
    PUNCTUATED = TEMP_TEXT.translate(str.maketrans('', '', string.punctuation))

    FILE_VARIABLE = open(FILENAME, "w")
    FILE_VARIABLE.write(PUNCTUATED)
    print("Successfully Written Data")
    return PUNCTUATED
