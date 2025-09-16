# RPG Character Exercise 🎲

In this exercise, I built a simple Python function that creates an RPG character. 
This mini-project from FreeCodeCamp served as an excellent first exercise to get used to some of the rules and quirks of Python.

---

## Objective 🎯

Create a function named `create_character` that takes a character name and three stats: strength, intelligence, and charisma. The function should validate all inputs and return a formatted string displaying the character’s stats visually with dots.

By completing this exercise, I practiced:  
- Writing functions with parameters  
- Input validation in Python  
- String formatting and concatenation  
- Using control flow (`if` statements) effectively 

---

## What I Did 🛠️

1. **Function Setup**  
   - Created a function called `create_character`.
   - It accepts four arguments in this order: `character_name`, `strength`, `intelligence`, `charisma`.

2. **Validate Character Name 📝**  
   - If the name is not a string → return `"The character name should be a string"`.  
   - If the name is longer than 10 characters → return `"The character name is too long"`.  
   - If the name contains spaces → return `"The character name should not contain spaces"`.

3. **Validate Stats ⚡**  
   - All stats must be integers → otherwise return `"All stats should be integers"`.  
   - Stats must be between 1 and 4 inclusive → return `"All stats should be no less than 1"` or `"All stats should be no more than 4"`.  
   - The sum of all stats must equal 7 → otherwise return `"The character should start with 7 points"`.

4. **Format Character Output ✨**  
   - If all inputs are valid, a string is returned with four lines:  
     1. The first line shows the character name.  
     2. Lines 2–4 show each stat (`STR`, `INT`, `CHA`) followed by a number of full dots (`●`) equal to the stat value, and empty dots (`○`) to make a total of 10.

> ⚠️ Note: Avoid using `str` or `int` as variable names since they are Python keywords.

---

## Solution 💻

My complete implementation of this exercise is included in this folder as `rpg-character.py` as well as a version with comments to make it easy to follow along.
It follows all the validation rules and formatting requirements described above. 

Use it if you are stuck, but attempt the challenge yourself first!

---

## Tips & Suggestions 💡

- Don't allow the steps to overwhelm you. Simply focus on one step at a time and adjust as you go along.  
- Use the 'Run Tests' button throughout the challenge to check your progress as you go rather than waiting until the end.
- If you're unsure about the syntax for a line of code, try writing it out in simpler language first, then refine it. Use Google to check examples if needed.
    - Example: Instruction "If the character name is longer than 10 characters, the function should return `The character name is too long`"
        - You may start with:
        ```python
        if character_name is > 10
          return "The character name is too long"
        ```
        
        - This would result in a `TypeError`:
        ```bash
        TypeError: '>' not supported between instances of 'str' and 'int'
        ```

        - Then, you research how to check the length of a string, so you adjust it to proper Python syntax:
        ```python
        if len(character_name) > 10:
            return "The character name is too long"
        ```
      