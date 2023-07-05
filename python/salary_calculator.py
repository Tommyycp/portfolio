def salary_calculator (month_leaving):
    salaries = []
    months = ["april", "may", "june", "july", "august", "september", "october", "novemeber", "december", "january", "february", "march",]
    index = months.index(month_leaving) + 1
    months = months[:index]
    for i in range(len(months)):
         salaries.append(int(input(f"Type your salary for {months[i]}.")))
    divisor = float(input("What is the percentage of your actual salary out of your contractual salary? (in demical place please)"))
    print (f"Your raw salary is {sum(salaries)/divisor}")

starting_prompt = input("Tell me the month you're leaving").lower()
salary_calculator (starting_prompt)
