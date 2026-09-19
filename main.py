# Tuboo Tailoring Management System - Complete Simulation
print("--- مرحباً بك في نظام إدارة مشاغل الخياطة (تيوبو) ---")

# قوائم تخزين البيانات مؤقتاً
clients_database = []
orders_database = []

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

def create_order(client_name, fabric_type, price):
    order = {
        "client": client_name,
        "fabric": fabric_type,
        "price": price,
        "status": "تحت القياس" # الحالة الأولى للطلب
    }
    orders_database.append(order)
    print(f"تم إنشاء طلب جديد للعميل: {client_name} - النوع: {fabric_type} - السعر: {price} ريال")

def update_order_status(client_name, new_status):
    for order in orders_database:
        if order["client"] == client_name:
            order["status"] = new_status
            print(f"تم تحديث حالة طلب العميل {client_name} إلى: {new_status}")

# تجربة النظام المتكامل:
add_new_client("محمد أحمد", "0501234567", 42, 38, 60)
create_order("محمد أحمد", "قماش قطن ياباني", 250)

# محاكاة تغيير حالة الطلب
update_order_status("محمد أحمد", "قيد الخياطة")

print(f"إجمالي عدد العملاء: {len(clients_database)} | إجمالي عدد الطلبات: {len(orders_database)}")
