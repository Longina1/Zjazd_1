salary = int(input("What's your gross salary? "))
no_of_children = int(input('How many children do you have? '))
child_benefit = 500

print('You will be paid ', int((salary - (salary * 0.20)) + 500 * no_of_children))

salary = int(input("What's your gross salary? "))
no_of_children = int(input('How many children do you have? '))
child_benefit = 500

if salary < 3000 and no_of_children < 2:
    print('You will be paid ', int(salary - (salary * 0.10)))
elif salary < 3000 and no_of_children >= 2:
    print('You will be paid ', int((salary - (salary * 0.10)) + 500 * no_of_children))
elif salary > 5000 and no_of_children >= 2:
    print('You will be paid ', int((salary - (salary * 0.20)) + 500 * no_of_children))
elif salary > 5000 and no_of_children < 2:
    print('You will be paid ', int((salary - (salary * 0.20))))

