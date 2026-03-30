#D) cafe bill

name = input("Enter customer name:")
items = 0
subtotal = 0

while True:
    item = input("Enter item name (or 'done' to finish):")
    if item == "done":
        break
    price = int(input("Enter price:"))
    items += 1
    subtotal += price
hour = int(input("Enter current hour (0-23):"))

print("\n")
print("-" * 30)
print("Customer :", name)
print("Items :", items)
print("Subtotal :", subtotal)

if 6 <= hour < 12:
    discount_label = "Morning discount"
    discount_rate = 0.1
elif 12 <= hour < 17:
    discount_label = "No discount"
    discount_rate = 0
elif 17 <= hour < 22:
    discount_label = "Evening discount"
    discount_rate =0.05
else:
    print("Time period : Closed")
    print("Cafe is closed")
    print("-" * 30)

    print("Name uppercase :", name.upper())
    print("Name lowercase :", name.lower())
    print("Name length :", len(name))

    if name[0].upper() == 'A' or name[0].upper() == 'S':
        print("VIP customer")
    else:
        print("Regular customer")

    exit()


discount = subtotal * discount_rate
after_discount = subtotal - discount
tip = after_discount * 0.1
total = after_discount + tip

print("-" * 30)
print("Time period :", discount_label)
print("Discount :", discount, "KZT")
print("Tip(10%) :", tip)
print("Total :", total, "KZT")
print("-" * 30)

print("Name uppercase : ", name.upper())
print("Name lowercase : ", name.lower())
print("Name length :", len(name))

if name[0].upper() == 'A' or name[0].upper() == 'S':
    print("VIP customer")
else:
    print("Regular customer")
