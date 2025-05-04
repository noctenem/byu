"""
Program: Clever Stories
Author: Sairi Conejo Flores

Purpose: This program interacts with the user to create a creative story.
"""

# A few more words have been added and also a function that will
# automatically handle the addition of 'a' or 'an' as appropriate.

print("Please enter the following:\n")

animal = input("insert an animal: \n")
adjective = input("insert an adjective: \n")
verb1 = input("insert a verb: \n")
exclamation = input("insert an exclamation: \n")
exclamation = exclamation.capitalize()
verb2 = input("insert a verb: \n")
place = input("insert a place: \n")
verb3 = input("insert a verb: \n")
object = input("insert an object: \n")
feeling = input("insert a feeling: \n")
name = input("insert a name: \n")


# function to handle the articles 'a' and 'an'
def article(word):
      return 'an' if word[0].lower() in 'aeiou' else 'a' # ternary operator
 
# This print shows the result of the story.
# The triple quotes are intentional, avoid using the "\n" character and the "print()" function.
print(f'''
Your story is:
      
The other day, I was really in trouble. It all started when I saw a very
{adjective} {animal} {verb1} down the hallway. "{exclamation}!" I yelled. But all
I could think to do was to {verb2} over and over. Miraculously,
that caused it to stop, but not before it tried to {verb3}
right in front of my family.

In a panic, I ran to {article(place)} {place} to find {article(object)} {object}
and protect myself. I was feeling so {feeling} but then my friend {article(name)} {name}
showed up and we fled the place.
      ''')