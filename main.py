# Tuboo Tailoring Management System - Database Simulation
print("--- مرحباً بك في نظام إدارة مشاغل الخياطة (تيوبو) ---")

# قائمة لتخزين العملاء والمقاسات مؤقتاً
clients_database = []

def add_new_client(name, phone, chest, waist, length):
    client = {
        "name": name,
        "phone": phone,
        "measurements": {
            "chest": chest,
            "waist": waist,
            "length": length
        }
    }
    clients_database.append(client)
    print(f"تم إضافة العميل بنجاح: {name}")

# تجربة إضافة عميل للنظام
add_new_client("محمد أحمد", "0501234567", 42, 38, 60)

print(f"إجمالي عدد العملاء المسجلين حالياً: {len(clients_database)}")
