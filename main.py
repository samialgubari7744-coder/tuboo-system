
# نظام إدارة الخياطة Tuboo - مع إدارة الأدوار وصلاحيات المستخدمين
print("--- مرحباً بك في نظام إدارة مشاغل الخياطة (تيوبو) ---")

# قوائم تخزين البيانات مؤقتاً
clients_database = []
orders_database = []
invoices_database = []
users_database = []

def add_system_user(username, role):
    user = {
        "username": username,
        "role": role # الأدوار: مدير, استقبال, خياط
    }
    users_database.append(user)
    print(f"تم إضافة المستخدم: {username} بدور: {role}")

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
        "status": "تحت القياس"
    }
    orders_database.append(order)
    
    invoice = {
        "client": client_name,
        "total_amount": price,
        "tax": price * 0.15,
        "net_total": price * 1.15
    }
    invoices_database.append(invoice)
    print(f"تم إنشاء الطلب للعميل: {client_name} بقيمة صافية: {invoice['net_total']} ريال")

# إعداد الصلاحيات وتجربة النظام:
add_system_user("سالم", "مدير النظام")
add_system_user("خالد", "موظف استقبال")
add_system_user("أحمد", "خياط")

add_new_client("محمد أحمد", "0501234567", 42, 38, 60)
create_order("محمد أحمد", "قماش قطن ياباني", 250)

print(f"إحصائيات النظام -> المستخدمين: {len(users_database)} | العملاء: {len(clients_database)} | الطلبات: {len(orders_database)}")
def create_order(client_name, fabric_type, price):
    order = {
        "client": client_name,
        "fabric": fabric_type,
        "price": price,
        "status": "تحت القياس"
    }
    orders_database.append(order)
    
    invoice = {
        "client": client_name,
        "total_amount": price,
        "tax": price * 0.15,
        "net_total": price * 1.15
    }
    invoices_database.append(invoice)
    print(f"تم إنشاء الطلب للعميل: {client_name} بقيمة صافية: {invoice['net_total']} ريال")

# تجربة إنشاء طلب وفاتورة
create_order("محمد أحمد", "قماش قطن ياباني", 250)
def display_orders():
    print("\n--- قائمة الطلبات الحالية ---")
    for index, order in enumerate(orders_database, 1):
        print(f"{index}. العميل: {order['client']} | القماش: {order['fabric']} | الحالة: {order['status']}")

# تجربة عرض الطلبات
display_orders()
