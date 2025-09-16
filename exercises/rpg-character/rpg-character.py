full_dot = '●' 
empty_dot = '○' 

def create_character(character_name, strength, intelligence, charisma):

    if not isinstance(character_name, str):
        return "The character name should be a string"

    if len(character_name) > 10:
        return "The character name is too long"

    if " " in character_name:
        return "The character name should not contain spaces"

    if not isinstance(strength, int) or not isinstance(intelligence, int) or not isinstance(charisma, int): 
        return "All stats should be integers"

    if strength < 1 or intelligence < 1 or charisma < 1:
        return "All stats should be no less than 1"

    if strength > 4 or intelligence > 4 or charisma > 4:
        return "All stats should be no more than 4"

    if strength + intelligence + charisma != 7:
        return "The character should start with 7 points"

    str_line = "STR " + full_dot*strength + empty_dot*(10-strength)  
    int_line = "INT " + full_dot*intelligence + empty_dot*(10-intelligence)  
    cha_line = "CHA " + full_dot*charisma + empty_dot*(10-charisma) 

    return character_name + "\n" + str_line + "\n" + int_line + "\n" + cha_line
