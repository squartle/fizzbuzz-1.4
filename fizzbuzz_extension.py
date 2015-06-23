user_input = raw_input("Choose an upper limit. ")

while user_input.isdigit() == False:
    user_input = raw_input("That's not right.  Please choose an integer. ")
else:
    print "Fizz buzz counting up to " + user_input + "."

user_input = int(user_input)
count = 0

for n in range(0, user_input):
    if count % 3 == 0 and n % 5 == 0:
        print "fizz buzz"
        count += 1
    elif count % 3 == 0:
        print "fizz"
        count += 1
    elif count % 5 == 0:
        print "buzz"
        count += 1
    else:
        print count
        count +=1
