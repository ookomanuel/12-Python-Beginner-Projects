# string concatenation (aka how to put strings together) === madlib
# suppose we want to create a string that says "subscribe to _______"
#youtuber = "Kylie Ying" #some string variable

# a few ways to do this
# print("subscribe to " + youtuber)
# print("subscribe to {}".format(youtuber))
# print(f"subscribe to {youtuber}")

adj = input("Adjective: ")
adj1 = input("Adjective: ")
adj2 = input("Adjective: ")
precious_mineral = input("Precious Mineral: ")
verb1 = input("Verb: ")
verb2 = input("Verb: ")
verb3 = input("Verb: ")
adj3 = input("Adjective: ")
adj4 = input("Adjective: ")
adverb = input("Adverb for burning: ")
verb4 = input("2nd Last Verb: ")
last_verb = input("Last Verb: ")
noun1 = input("Noun: ")
adj5 = input("Adjective: ")

#madlib = f"Computer programming is so {adj}! It makes me so excited all the time because \
#I love to {verb1}. Stay hydrated and {verb2} like you are {famous_person}!"

#print(madlib)

geschichte = f"I once met a {adj} man. He was {adj1} and {adj2} about Life.\
    He had a flair about him because all he went near seemed to turn a little {precious_mineral}.\
        He could {verb1}, {verb2} and {verb3} the piano.\
            Yes, he was {adj3} with a {adj4} personality and inside he burned {adverb}!\
                This young man always {verb4} about his future while trying to {last_verb} his past.\
                    This {noun1} wasn't always {adj5}!"

print(geschichte)
