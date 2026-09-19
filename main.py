# نظام إدارة الخياطة Tuboo - محاكاة كاملة مع الفواتير وتتبع الطلبات
print("--- مرحباً بك في نظام إدارة مشاغل الخياطة (تيوبو) ---")

# قوائم تخزين البيانات مؤقتاً
clients_database = []
orders_database = []
invoices_database = []

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
    
    # إصدار فاتورة تلقائية للطلب
    invoice = {
        "client": client_name,
        "total_amount": price,
        "tax": price * 0.15, # احتساب ضريبة القيمة المضافة 15%
        "net_total": price * 1.15
    }
    invoices_database.append(invoice)
    
    print(f"تم إنشاء الطلب وإصدار الفاتورة للعميل: {client_name} - المبلغ الإجمالي مع الضريبة: {invoice['net_total']} ريال")

def update_order_status(client_name, new_status):
    for order in orders_database:
        if order["client"] == client_name:
            order["status"] = new_status
            print(f"تم تحديث حالة طلب العميل {client_name} إلى: {new_status}")

# تجربة النظام المحدث:
add_new_client("محمد أحمد", "0501234567", 42, 38, 60)
create_order("محمد أحمد", "قماش قطن ياباني", 250)
update_order_status("محمد أحمد", "قيد الخياطة")

print(f"إحصائيات النظام -> العملاء: {len(clients_database)} | الطلبات: {len(orders_database)} | الفواتير: {len(invoices_database)}")
