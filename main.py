from spy_details import spy_name, spy_salutation, spy_age, spy_rating


def start_chat(spy_name, spy_age, spy_rating):
    menu_choices = "What do you want to do? \n 1. Add a status update\n"
    menu_choice = input(menu_choices)

    if menu_choice == 1:
        print menu_choice

    else:
        print "Exiting"

print 'Let\'s get started'

question = "Continue as " + spy_salutation + " " + spy_name + "(Y/N)?"
existing = raw_input(question)

if (existing == "Y"):
  print "Welcome %s %s with rating %.2f" % (spy_salutation,spy_name,spy_rating)

  start_chat(spy_name,spy_age,spy_rating)
else:

    spy_name = raw_input("Welcome to spy chat, you must tell me your spy name first: ")

    if len(spy_name) >0 :
        print 'Welcome ' + spy_name + '. Glad to have you back with us.'

        spy_salutation = raw_input("Should I call you Mister or Miss?: ")

        spy_name = spy_salutation + " " + spy_name

        print "Alright " + spy_salutation + " " + spy_name + ". I'd like to know a little bit more about you before we proceed..."

        spy_age = 0 # This is my initialization foor spy age
        spy_rating = 0.0
        spy_is_online = False
        spy_age = input("What is your age?")
        if spy_age > 12 and spy_age < 50:
            spy_rating = input("What is your spy rating?")
            if spy_rating > 4.5:
                print 'Great ace!'
            elif spy_rating > 3.5 and spy_rating <= 4.5:
                print 'You are one of the good ones.'
            elif spy_rating >= 2.5 and spy_rating <= 3.5:
                print 'You can always do better'
            else:
                print 'We can always use somebody to help in the office.'
            spy_is_online = True
            print "Authentication complete. Welcome " + spy_name + " age: " + str(spy_age) + " and rating of: " + str(spy_rating )+ " Proud to have you onboard"
            start_chat();
        else:
            print 'Sorry you are not of the correct age to be a spy'


    else :
        print "Please Enter Spyname"