
# Create dictionary
staffdict = dict()
#hourscount = 0.0
#cashtips = None
#cardtips = None

def cashcardtips(cashinput, cardinput):
    cashtips = float(cashinput)
    cardtips = float(cardinput)
    #cardtips = cashinput * cardinput
    #return cardtips
    print("Total cash tips: $", float(cashinput), "\n" "Total card tips : $", float(cardinput))
    return cashtips, cardtips

cashtips = float(input('Enter Cash Tips Amount: '))
cardtips = float(input('Enter Card Tips Amount: '))

#cashcardtips(cash, card)
#print(cashcardtips(cash, card))

#Function to convert "Name" and "Hours" inputted by user to dictionary
def staffnamehours (nameinput, hoursinput):
    name = nameinput
    staffhours = float(hoursinput)
    print(nameinput, "worked", staffhours, "hours")
    namedict = dict()
    namedict[name] = staffhours
    print("Name Dictionary Key and Value: ", namedict)
    return namedict

#x = staffnamehours(input("Enter Name: "), input("Enter Hours: "))
#namedict = staffnamehours('Ace', 8)
#print(namedict)
#print(staffdict)

#Update Master Staff "Name and Hours Dictionary with new "Names and Hours"


while True:
    staffdict.update(staffnamehours(input("Enter Name: "), input("Enter Hours: ")))
    print("Staff Master Dictionary: ", staffdict)
    addstaff = input("Add new staff member? Y/N: ")
    # Add staff button returns Y or True
    if addstaff == 'Y':
        continue
    # Calculate Button returns N or False and exits loop to produce final calculation
    elif addstaff == 'N': 
        break

print("Staff Master Dictionary: ", staffdict)
#Sum total hours of all names in Master Staff dictionary
totalhours = sum(staffdict.values())
print("Total of all staff hours: ", totalhours)

print(staffdict.items(), "\n")
for (k, v) in staffdict.items():
    p = v/totalhours
    staffcashtips = round(p*cashtips, 2)
    staffcardtips = round(p*cardtips, 2)
    print(k, "worked", v, "hours and earned", round(p*100, 2), "% of total tips")
    print(k, "Cash Tips: $", staffcashtips)
    print(k, "Card Tips: $", staffcardtips, "\n")

print("Total staff hours worked: ", round(totalhours, 2), "hours")
print("Total staff cash tips:  $", round(cashtips, 2), sep='')
print("Total staff cash tips:  $", round(cardtips, 2), sep='')
print('\n')
