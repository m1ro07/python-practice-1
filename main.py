customerName= input("Enter customer name: ")
item1 = input("Enter name of item 1: ")
price1 = float(input("Enter price of item 1 (KZT): "))
item2 = input("Enter name of item 2: ")
price2 = float(input("Enter price of item 2 (KZT): "))
people = int(input("Enter number of people: "))

subtotal = price1 + price2
tip = subtotal * 0.1
total = subtotal + tip
per_person = total / people

print("=" * 30)
print("CAFE BILL")
print("=" * 30)
print("Customer :", customerName)
print(item1, ":", price1)
print(item2, ":", price2)
print("-" * 30)
print("Subtotal :", subtotal, "KZT")
print("Tip (10%) :", tip, "KZT")
print("Total : ", total, "KZT")
print("Per person :", per_person)
print("=" * 30)
print("Tip included:" , tip > 0)
print("Bill over 5000 KZT:", total > 5000)

input("Нажми Enter, чтобы закрыть окно...")