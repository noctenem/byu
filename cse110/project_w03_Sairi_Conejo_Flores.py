"""
Program: Adventure Game

Author: Sairi Conejo Flores
Purpose: Make a story with the statements if/elif/else
"""

# Example
# a = 1
# b = 2
#
# if a > b:
#     print(a)
# elif b > a:
#     print(b)
# else:
#     print("hello world!")

# Simplification of the code to a single recursive function,
# which avoids excessive nesting when creating several levels.
# I have also shown this little game to my family and they liked it.

def game(levels):

    message = levels["message"]
    question = levels["question"]
    options = levels["options"]

    print(message)
    if not options:
        return
    
    choice = input(f"{question} ({" / ".join(options.keys())}): ").upper()

    if choice in options:
        game(options[choice])
    else:
        print("GAME OVER! - The entered value is NOT RECOGNIZED.")

##################
#     levels     #
##################
level_four = {
    "YES": {
        "message" : "\nExcellent! I'll wait for you next time.\n",
        "question" : None,
        "options" : None
    },
    "NO": {
        "message" : "\nSorry, next time I'll do better.\n",
        "question" : None,
        "options" : None
    },
    "MAYBE": {
        "message" : "\nSorry, we'll do better next time.\n",
        "question" : None,
        "options" : None
    }
}

level_three = {
    "left" : {
        "YES" : {
            "message" : """
Maybe it's okay, even though Marco is a very annoying neighbor.
""",
            "question": "Did you like the story?",
            "options": level_four
        },
        "NO" : {
            "message" : """
Even if your decision comes late you could change history at some point.
""",
            "question": "Did you like the story?",
            "options": level_four
        },
    },
    "right" : {
        "YES" : {
            "message" : "\nOf course, because I liked it a lot.\n",
            "question": "Did you like the story?",
            "options": level_four
        },
        "NO" : {
            "message" : "\nMaybe you could do it another day.\n",
            "question": "Did you like the story?",
            "options": level_four
            }
        },

}

level_two = {
    "left" : {
        "CONTINUE" : {
            "message" : """
    But you continue on your way as if nothing had happened but you stop
    to think if what you did was right or wrong.
    """,
            "question" : "Was it a good idea?",
            "options" : level_three["left"]
        },
        "STOP" : {
            "message" : "\nYou stop and greet Marco and ask him he needs help.\n",
            "question" : "What did Marco answer?",
            "options" : level_three["left"]
        }
    },
    "right" : {
        "BOOK" : {
            "message" : """
So, you pick up the book and read it with great interest since a very well known
writer recommended it to you but when the story was more entertaining, night comes
and you have to leave.
""",
            "question" : "Will you read it again?",
            "options" : level_three["right"]
        },
        "VIDEO GAME" : {
            "message" : """
You pick up the video game and you see that there is a game that entertains you
and you play it for a long time but night comes and you have to leave.
""",
            "question" : "Will you play it again?",
            "options" : level_three["right"]
        }
    }

}

level_one = {
        "GO BACK": {
            "message" : """
So you decide to go back but on the way you meet Marco
your neighbor, who has two boxes.
""",
            "question" : "What will you do?",
            "options" : level_two["left"]
        },
        "WAIT": {
        "message" : """
But that doesn't bother you because you're on vacation
and you decide to wait and to pass the time you look for something to do
and you have a book and a video game.
""",
            "question" : "Which one do you chooce?",
            "options" : level_two["right"]
        }
}

levels = {
    "message" : """
Imagine you are driving your car, calmly enjoying the scenery
and suddenly the road you were supposed to take is blocked by roadworks.
Now you have two options: "GO BACK" or "WAIT".
""",
    "question" : "What are you going to do?",
    "options" : level_one
}

game(levels)