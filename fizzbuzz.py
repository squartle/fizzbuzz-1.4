count = 0
print "Fizz buzz counting up to 100."

for n in range(0, 100):
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
