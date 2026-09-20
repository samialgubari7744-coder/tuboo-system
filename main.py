# Tuboo Tailoring Management System
print("Welcome to Tuboo Tailoring Management System")

store_name = "Tuboo Men Tailoring"
version = "1.0.0"

print("Store Name: " + store_name)
print("Version: " + version)

clients_database = []

def add_new_client(name, phone):
    client = {"name": name, "phone": phone}
    clients_database.append(client)
    print("Client added successfully: " + name)

add_new_client("Ahmed Mohammed", "0501234567")
print("Total Clients: 1")
