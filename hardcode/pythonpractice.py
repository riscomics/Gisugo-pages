def takehome_income(r, rh, o, oh):
    tax = .2241
    ira = .05    
    benefits = 158.60
    total_income = (r * rh) + (o * oh)
    total_deductions = (total_income * (tax + ira)) + benefits 
    takehome =  round(total_income - total_deductions, 2)
    return takehome

regular_pay_rate = 30
regular_hours = 80

overtime_pay_rate = 45
overtime_hours = 11.23

total_takehome_income = takehome_income(regular_pay_rate, regular_hours, overtime_pay_rate, overtime_hours)

print("===========================")
print(f"You clocked in a total of {regular_hours} hours plus {overtime_hours} overtime hours in this pay cycle.")
print("") 
print(f"With regular hours paid at a rate of ${regular_pay_rate}/hour and overtime hours being paid at a rate of ${overtime_pay_rate}/hour")
print(f"Your takehome income in this paycycle with income tax and benefits subtracted is ${total_takehome_income}")

print("===========================")

def tax_percent(t, g):
    return (t / g) * 100

tax = 929.17
gross = 3620.40

percent = round(tax_percent(tax, gross), 2)
print(f"${tax} is {percent}% tax of your ${gross} gross pay.")

print("===========================")


def to_fahrenheit(c):
    f = (c * 9/5) + 32
    return f

def temp(c):
    fahrenheit = round(to_fahrenheit(c), 2)
    print(f"{c} degrees in celcius is {fahrenheit} in fahrenheit.")

temp(32)
temp(28)

def to_celcius(f):
    c = (f - 32) * 5/9
    return c

def temp(f):
    c = round(to_celcius(f), 2)
    print(f"{f} degrees in fahrenheit is {c} degrees in celcius.")

temp(32)
temp(28)
print("===========================")

def area_of_circle(r):
    pi = 3.14
    aoe = round((pi * r * r), 2)
    return aoe

dagger_reach = 1.1
katana_reach = 2
spear_reach = 3
arrow_reach = 12

dagger_damage = area_of_circle(dagger_reach)
katana_damage = area_of_circle(katana_reach)
spear_damage = area_of_circle(spear_reach)
arrow_damage = area_of_circle(arrow_reach)

def player_health(h, damage, weapon):
    status_health = h - damage
    print(f"Player's health is now at {status_health} after receiving {damage} points from a {weapon}")

health = 100

player_health(health, dagger_damage, "dagger")
player_health(health, katana_damage, "katana")
player_health(health, spear_damage, "spear")
player_health(health, arrow_damage, "arrow")


print(f"")
print(f"======= COST PER GALLON =======") 
def cost_per_gallon(cost, mpg):    
    return round((cost / mpg), 2)

def main():
    cost_gallon(65, 22)

def cost_gallon(cost, mpg):
    gallon_price = cost_per_gallon(cost, mpg)
    print(f"You spent ${cost} for fuel, which is ${gallon_price} per gallon.")

main()
print(f"")

print(f"======= Travel Expense =======") 
def round_trip(pay, gallon, mpg, miles):
    gallons_used = round((miles / mpg), 2)
    gallon_cost = round((gallon * gallons_used), 2)
    net_comp = round((pay - gallon_cost), 2)
    return gallons_used, gallon_cost, net_comp

def main():
    trip_comp(16.25, 2.88, 22, 26) 

def trip_comp(pay, gallon, mpg, miles):
    gallons_used, gallon_cost, net_comp = round_trip(pay, gallon, mpg, miles) 
    print(f"You drove a total of {miles} miles round trip and are paid ${pay}.")
    print(f"The round trip used up {gallons_used} gallons of fuel and costs a total of ${gallon_cost}0.")
    print(f"You are paid a net remainder of ${net_comp}.")

main()

print(f"")
print(f"======= MILES TO COST =======") 
def miles_to_cost(miles, mpg, gallon):
    gallon_miles = miles / mpg
    cost_miles = round((gallon_miles * gallon), 2)
    return gallon_miles, cost_miles

def main():
    drive_cost(431, 25, 2.88)

def drive_cost(miles, mpg, gallon):
    gallon_miles, cost_miles = miles_to_cost(miles, mpg, gallon)
    print(f"Your vehicle used a total of {gallon_miles} gallons of fuel.")
    print(f"Costing a total of ${cost_miles}.") 

main()

print(f"")
print(f"======= FUEL TO MPG =======") 
def fuel_to_mpg(cost, gallon, miles):
    total_gallons = round((cost / gallon), 2)
    total_mpg = round((miles / total_gallons), 2)
    return total_gallons, total_mpg

def main():
    driven(50, 2.88, 431)

def driven(total_cost, gallon_price, miles_driven):
    total_gallons, total_mpg = fuel_to_mpg(total_cost, gallon_price, miles_driven)    
    print(f"You spent ${total_cost} for {total_gallons} gallons of fuel.")
    print(f"Based on your fuel consupmtion, you have a total of {total_mpg} MPG.")

main()

print(f"")
print(f"======= FUEL TO MILES =======") 

def fuel_to_miles(cost, gallon, mpg):
    total_gallons = round((cost / gallon), 2)
    miles = total_gallons * mpg
    return total_gallons, miles

def main():
    travel(50, 2.88, 25)

def travel(cost, gallon, mpg):
    purchased_gallons, driven_miles = fuel_to_miles(cost, gallon, mpg)
    print(f"You spent ${cost} to purchase a total of {purchased_gallons} gallons of fuel.")
    print(f"This let you drove a total of {driven_miles} miles.")

main()

print(f"======= Board Game Production Cost =======") 

def boardgame_cost(board_price, board_qty, pieces_price, pieces_sets):
    board_cost = round((board_price * board_qty), 2)
    chess_pieces = round((pieces_price * pieces_sets), 2)
    return board_cost, chess_pieces

def main():
    game_production(6.80, 2000, 2.59, 2000) 
    game_production(6.80, 500, 2.59, 500)

def game_production(board_price, board_qty, pieces_price, pieces_sets):
    board_cost, chess_pieces = boardgame_cost(board_price, board_qty, pieces_price, pieces_sets)
    print(f"Producing {board_qty} chessboards costs a total of ${board_cost:.2f}.")
    print(f"Purchasing {pieces_sets} sets of chess pieces costs a total of ${chess_pieces:.2f}.")
    print(f"")

main() 

print(f"==============")

def weekly_income(regular_hours, regular_rate, overtime_hours, overtime_rate, tax, benefits, roth):
    gross_pay = round(((regular_hours * regular_rate) + (overtime_hours * overtime_rate)), 2)
    net_pay = round( (gross_pay) - (gross_pay * tax) - benefits - ( ((gross_pay)-(gross_pay * tax)-(benefits)) * roth), 2)
    return gross_pay, net_pay

def main():
    paycheck1(80, 30, 28, 45, .21, 155, .15)
    paycheck2(80, 30, 15, 45, .21, 155, .15)
    
def paycheck1(regular_hours, regular_rate, overtime_hours, overtime_rate, tax, benefits, roth):
    gross_pay = round(((regular_hours * regular_rate) + (overtime_hours * overtime_rate)), 2)
    total_pay, takehome_pay = weekly_income(regular_hours, regular_rate, overtime_hours, overtime_rate, tax, benefits, roth)
    tax_rate = round(tax * 100)
    tax_total = (gross_pay * tax) 
    retirement_percent = round(roth * 100)
    retirement_fund =  ((gross_pay)-(gross_pay * tax)-(benefits)) * roth
    print(f"For the first 2 weeks of the month:")
    print(f"You worked a total of {regular_hours} regular hours at a rate of ${regular_rate} per hour \nand {overtime_hours} overtime hours at a rate of ${overtime_rate} per hour.")
    print(f"")
    print(f"The company paid you ${total_pay} before tax.")
    print(f"After a {tax_rate}% tax rate of ${tax_total}, health insurance benefits of ${benefits}, \nand a {retirement_percent}% Roth IRA retirement fund contribution of ${retirement_fund}, your takehome paycheck is ${takehome_pay:.2f}.")
    print(f"=======")    

def paycheck2(regular_hours, regular_rate, overtime_hours, overtime_rate, tax, benefits, roth):
    gross_pay = round(((regular_hours * regular_rate) + (overtime_hours * overtime_rate)), 2)
    total_pay, takehome_pay = weekly_income(regular_hours, regular_rate, overtime_hours, overtime_rate, tax, benefits, roth)
    tax_rate = round(tax * 100)
    tax_total = (gross_pay * tax) 
    retirement_percent = round(roth * 100)
    retirement_fund =  ((gross_pay)-(gross_pay * tax)-(benefits)) * roth
     
    print(f"For the second 2 weeks of the month:")
    print(f"You worked a total of {regular_hours} regular hours at a rate of ${regular_rate} per hour \nand {overtime_hours} overtime hours at a rate of ${overtime_rate} per hour in two weeks.")
    print(f"")
    print(f"The company paid you ${total_pay} before tax.")
    print(f"After a {tax_rate}% tax rate of ${tax_total}, health insurance benefits of ${benefits}, \nand a {retirement_percent}% Roth IRA retirement fund contribution of ${retirement_fund}, your takehome paycheck is ${takehome_pay:.2f}.")
    print(f"")  

main()


print(f"==============")

 
def Canada_USA(celcius, USA):
    Canada_weather = f"If the temperature in Canada is {celcius} degrees celcius"
    conversion = (celcius * 9/5) + 32
    US_weather = f" the temperature is {conversion} degrees fahrenheit"
    return Canada_weather, US_weather

def main(): 
    temps(30, "in the USA,")

def temps(Celcius_temp, America):
    Canada, USA = Canada_USA(Celcius_temp, America)
    print(f"{Canada}, {America}{USA}.")

main()
 
def get_receipt(range, mpg, gallon):
    drive = f"You drove a total of {range} miles, consuming {mpg} miles per gallon."
    distance = f"At the price of ${gallon} per gallon of fuel," 
    full_tank = (range / mpg) * gallon
    return drive, distance, full_tank

def yearly_fuel_cost(months, refuel, full_tank):
    fuel_budget = (months * refuel) * full_tank
    return fuel_budget

def main():
    fuel_data(445, 23, 2.88, "your cost of a full tank of fuel is ", 12, 3,)    

def fuel_data(range, mpg, gallon, tank_cost, months, refuel):
    drive, distance, full_tank = get_receipt(range, mpg, gallon)
    fuel_budget = yearly_fuel_cost(months, refuel, full_tank)
    print(f"{drive} {distance} {tank_cost}${full_tank:.2f}.")
    print(f"Refueling {refuel} times a month, your fuel cost in {months} months is ${fuel_budget:,.2f}.")

main()