# loop_tasks.py
# Real-world example: Vehicle Parking Management System

print("🚗 Welcome to Parking Management System")

# 1️⃣ For loop to print parking slot numbers (1–100)
print("\nAvailable Parking Slots:")
for slot in range(1, 101):
    print(slot, end=" ")
print("\n")


# 2️⃣ While loop countdown (gate opening timer)
print("⏳ Gate opening in:")
time = 5
while time > 0:
    print(time, "seconds")
    time -= 1
print("Gate is now open!\n")


# User input
vehicles = int(input("Enter number of vehicles entering: "))
total_fee = 0


# 3️⃣ Break and Continue
# 4️⃣ Loop combined with conditions
for i in range(1, vehicles + 1):
    vehicle_type = input(f"\nEnter vehicle type for vehicle {i} (bike/car/truck): ").lower()

    if vehicle_type == "":
        print("⚠️ No input provided. Skipping vehicle.")
        continue

    if vehicle_type == "emergency":
        print("🚑 Emergency vehicle detected. Stopping entry.")
        break

    if vehicle_type == "bike":
        fee = 20
    elif vehicle_type == "car":
        fee = 50
    elif vehicle_type == "truck":
        fee = 100
    else:
        print("❌ Invalid vehicle type. Skipping.")
        continue

    total_fee += fee
    print("Parking fee:", fee)


# 5️⃣ Iterating over string characters (vehicle number plate)
plate = input("\nEnter vehicle number plate: ")
print("Number plate characters:")
for ch in plate:
    print(ch, end=" ")
print("\n")


# 6️⃣ Multiplication table (hourly fee calculation)
print("Hourly Parking Fee Table (Car):")
for hour in range(1, 6):
    print(f"{hour} hour(s) = ₹{hour * 50}")
print()


# 7️⃣ Range with steps (maintenance check slots)
print("Maintenance checks at slots:")
for slot in range(0, 101, 10):
    print("Slot", slot)
print()


# 8️⃣ While loop with condition (payment confirmation)
attempts = 3
while attempts > 0:
    payment = input("Confirm payment (yes/no): ").lower()
    if payment == "yes":
        print("✅ Payment successful")
        break
    else:
        attempts -= 1
        print("❌ Payment failed. Attempts left:", attempts)

if attempts == 0:
    print("🔒 Payment blocked. Contact support.")


# 9️⃣ Final summary
print("\n🧾 Parking Summary")
print("Total parking fee collected: ₹", total_fee)
print("Thank you for using the parking system 😊")
