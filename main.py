import streamlit as st

# عنوان التطبيق
st.title("برنامج تيوبو (Tuboo) لإدارة مشاغل الخياطة")
st.write("مرحباً بك في لوحة تحكم نظام إدارة المشاغل السحابي")

# نموذج إدخال طلب جديد
st.header("إضافة طلب جديد")
client_name = st.text_input("اسم العميل")
fabric_type = st.text_input("نوع القماش")
price = st.number_input("سعر التفصيل (ر.س)", min_value=0.0, value=300.0)

if st.button("حفظ الطلب"):
    if client_name and fabric_type:
        st.success(f"تم حفظ طلب العميل: {client_name} بنجاح!")
        # هنا سيتم ربط تخزين البيانات بقاعدة البيانات لاحقاً
    else:
        st.warning("الرجاء إدخال اسم العميل ونوع القماش.")

# عرض قسم التقارير السريعة
st.header("تقارير سريعة")
if st.button("عرض إحصائيات المبيعات"):
    st.info("إجمالي المبيعات المسجلة حتى الآن: تم ربط النظام بنجاح.")

    
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
