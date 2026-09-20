# Tuboo Tailoring Management System
print("مرحباً بك في نظام إدارة مشاغل الخياطة (تيوبو)")

# بيانات تجريبية للنظام
store_name = "مشغل تيوبو للخياطة الرجالية"
version = "1.0.0"

print("اسم المشغل: " + store_name)
print("الإصدار: " + version)

# قائمة لتخزين العملاء
clients_database = []

def add_new_client(name, phone):
    client = {"name": name, "phone": phone}
    clients_database.append(client)
    print("تم إضافة العميل بنجاح: " + name)

# تجربة إضافة عميل
add_new_client("أحمد محمد", "0501234567")
print("إجمالي العملاء: 1")
