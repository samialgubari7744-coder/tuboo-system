
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
def calculate_total_revenue():
    total_revenue = sum(invoice['net_total'] for invoice in invoices_database)
    print(f"\n--- التقارير المالية ---")
    print(f"إجمالي المبيعات والأرباح (شامل الضريبة): {total_revenue} ريال")
    print(f"عدد الفواتير الصادرة: {len(invoices_database)}")

# تجربة حساب الأرباح والمبيعات
calculate_total_revenue()
def add_new_branch(branch_name, city):
    branch = {
        "branch_name": branch_name,
        "city": city,
        "status": "مفعل"
    }
    branches_database.append(branch)
    print(f"تم إضافة الفرع بنجاح: {branch_name} - مدينة {city}")

# تجربة إضافة فرع جديد للنظام
add_new_branch("فرع الرياض الرئيسي", "الرياض")
def send_whatsapp_notification(customer_name, phone_number, order_status):
    message = f"مرحباً {customer_name}، نود إعلامك بأن طلبك أصبح حالياً في حالة: {order_status}. شكراً لاختيارك لنا!"
    print(f"تم إعداد رسالة واتساب للرقم {phone_number}: {message}")

# تجربة إرسال إشعار تجريبي للعميل
send_whatsapp_notification("أحمد محمد", "+966500000000", "جاهز للتسليم")
def generate_sales_report():
    total_sales = sum(order["price"] for order in orders_database)
    total_orders = len(orders_database)
    print(f"--- تقرير المبيعات والأرباح ---")
    print(f"إجمالي عدد الطلبات المسجلة: {total_orders}")
    print(f"إجمالي قيمة المبيعات: {total_sales} ريال")

# تجربة طباعة التقرير
generate_sales_report()
def generate_electronic_invoice(order_id, customer_name, total_amount):
    vat = total_amount * 0.15  # احتساب ضريبة القيمة المضافة 15%
    final_total = total_amount + vat
    print(f"=== فاتورة إلكترونية ضريبية ===")
    print(f"رقم الطلب: {order_id}")
    print(f"اسم العميل: {customer_name}")
    print(f"المبلغ الإضافي (بدون ضريبة): {total_amount} ريال")
    print(f"ضريبة القيمة المضافة (15%): {vat:.2f} ريال")
    print(f"المبلغ الإجمالي المستحق: {final_total:.2f} ريال")
    print(f"الحالة: جاهزة للطباعة مع رمز الاستجابة السريعة (QR)")

# تجربة إصدار فاتورة
generate_electronic_invoice(108, "أحمد محمد", 450)
# نظام تحديد صلاحيات وأدوار المستخدمين
def check_user_permission(role, action):
    permissions = {
        "مدير الفرع": ["إدارة الطلبات", "عرض التقارير", "إدارة الموظفين", "تعديل الأسعار"],
        "الاستقبال": ["تسجيل عميل جديد", "إنشاء طلب", "إصدار فاتورة"],
        "خياط": ["عرض الطلبات المخصصة", "تحديث حالة خياطة الثوب"]
    }
    
    if role in permissions and action in permissions[role]:
        print(f"المستخدم ذو الدور ({role}) مسموح له بـ: {action}")
        return True
    else:
        print(f"عذراً! المستخدم ذو الدور ({role}) ليس لديه صلاحية لـ: {action}")
        return False

# تجربة التحقق من الصلاحيات
check_user_permission("الاستقبال", "إنشاء طلب")
check_user_permission("خياط", "عرض التقارير")
# نظام تتبع مراحل سير الطلب لخيّاط تيوبو
class TailorOrderTracker:
    def __init__(self, order_id, customer_name):
        self.order_id = order_id
        self.customer_name = customer_name
        self.stages = [
            "1. استقبال العميل وأخذ المقاسات",
            "2. إدخال المقاسات والتصميم",
            "3. متابعة الطلبات الابتكارية والقص",
            "4. مرحلة الخياطة والتطريز",
            "5. مرحلة الكي والتجهيز",
            "6. جاهز للتسليم",
            "7. تم التسليم للعميل"
        ]
        self.current_stage_index = 0

    def advance_stage(self):
        if self.current_stage_index < len(self.stages) - 1:
            self.current_stage_index += 1
            print(f"تم تحديث الطلب #{self.order_id} للعميل {self.customer_name} إلى المرحلة: {self.stages[self.current_stage_index]}")
        else:
            print(f"الطلب #{self.order_id} مكتمل ومسلم بالفعل!")

# تجربة مسار الطلب
my_order = TailorOrderTracker(108, "أحمد محمد")
my_order.advance_stage()
my_order.advance_stage()
# نظام إصدار الفواتير الإلكترونية وحساب الإجماليات
def calculate_tailoring_invoice(service_name, price, discount=0):
    tax_rate = 0.15 # نسبة ضريبة القيمة المضافة 15%
    subtotal = price - discount
    tax_amount = subtotal * tax_rate
    total_amount = subtotal + tax_amount
    
    print("--- فاتورة مشغل تيوبو الإلكترونية ---")
    print(تفاصيل الخدمة: {service_name})
    print(السعر الأساسي: {price} ر.س)
    print(الخصم: {discount} ر.س)
    print(المجموع الخاضع للضريبة: {subtotal} ر.س)
    print(قيمة الضريبة (15%): {tax_amount} ر.س)
    print(المجموع الإجمالي الواجب سداده: {total_amount} ر.س)
    print("-----------------------------------")
    return total_amount

# تجربة إصدار فاتورة لتفصيل ثوب
calculate_tailoring_invoice("تفصيل ثوب رجالي فاخر", 300, 20)
# نظام تقارير الأرباح والمبيعات اليومية
sales_records = []

def record_sale(order_id, amount):
    sales_records.append({"order_id": order_id, "amount": amount})
    print(f"تم تسجيل المبيعات للطلب #{order_id} بمبلغ {amount} ر.س")

def generate_sales_report():
    total_sales = sum(item["amount"] for item in sales_records)
    total_orders = len(sales_records)
    
    print("--- تقرير الأرباح والمبيعات لبرنامج تيوبو ---")
    print(f"إجمالي عدد الطلبات المباعة: {total_orders}")
    print(f"إجمالي الإيرادات الكلية: {total_sales} ر.س")
    print("------------------------------------------")

# تجربة تسجيل مبيعات وعرض التقرير
record_sale(101, 300)
record_sale(102, 450)
generate_sales_report()
