# Pre-filled for you by the exercise
full_dot = '●' 
empty_dot = '○' 

# Function to create an RPG character with validated stats
def create_character(character_name, strength, intelligence, charisma):

    # Checks if the character name is a string
    if not isinstance(character_name, str):
        return "The character name should be a string"

    # Checks if the character name is too long
    if len(character_name) > 10:
        return "The character name is too long"

    # Checks if the character name contains spaces
    if " " in character_name:
        return "The character name should not contain spaces"

    # Checks if all stats are integers
    if not isinstance(strength, int) or not isinstance(intelligence, int) or not isinstance(charisma, int): 
        return "All stats should be integers"

    # Checks if any stat is less than 1
    if strength < 1 or intelligence < 1 or charisma < 1:
        return "All stats should be no less than 1"

    # Checks if any stat is greater than 4
    if strength > 4 or intelligence > 4 or charisma > 4:
        return "All stats should be no more than 4"

    # Checks if the sum of stats equals 7
    if strength + intelligence + charisma != 7:
        return "The character should start with 7 points"

    # Build the visual representation of each stat

    # For example, if strength = 3:
    #   full_dot*strength = '●●●'   -> shows the points they have
    #   empty_dot*(10-strength) = '○○○○○○○' -> fills up to 10 for consistent display
    # Combine them with the stat abbreviation so each line looks like: STR ●●●○○○○○○○

    str_line = "STR " + full_dot*strength + empty_dot*(10-strength)  # Strength line
    int_line = "INT " + full_dot*intelligence + empty_dot*(10-intelligence)  # Intelligence line
    cha_line = "CHA " + full_dot*charisma + empty_dot*(10-charisma)  # Charisma line

    # Return the final formatted character string
    return character_name + "\n" + str_line + "\n" + int_line + "\n" + cha_line
