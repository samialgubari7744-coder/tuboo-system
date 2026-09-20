import streamlit as st
import os
import pandas as pd
from datetime import datetime

# إعداد الصفحة وتفعيل اتجاه الكتابة من اليمين لليسار (RTL)
st.set_page_config(page_title="خياطة تيوبو - النظام المتكامل", layout="centered")

st.markdown("""
<style>
    .stApp {
        direction: rtl;
        text-align: right;
    }
    label, h1, h2, h3, h4, p, div {
        text-align: right !important;
    }
    .stTextInput input, .stNumberInput input, .stSelectbox, .stTextArea textarea {
        direction: rtl;
        text-align: right;
    }
    div[data-baseweb="spinbutton"] button {
        display: none !important;
    }
</style>
""", unsafe_allow_html=True)

# شاشة تسجيل الدخول وتحديد الصلاحيات والأدوار
st.sidebar.title("🔐 بوابة النظام والأدوار")
user_role = st.sidebar.selectbox(
    "اختر دور المستخدم",
    ["مدير الفرع", "موظف الاستقبال", "خياط الفرع"]
)

st.sidebar.markdown("---")
navigation = st.sidebar.radio(
    "القائمة الرئيسية",
    ["تسجيل طلب جديد", "إدارة العملاء والطلبات", "تقارير وأرباح المشغل"]
)

# محاكاة تخزين البيانات المؤقت في الذاكرة (أو جلسة Streamlit)
if 'orders_db' not in st.session_state:
    st.session_state.orders_db = []

# --- الواجهة الأولى: تسجيل طلب جديد ---
if navigation == "تسجيل طلب جديد":
    st.title("🧵 نظام خياطة تيوبو - تسجيل طلب مفصل")
    
    # التحقق من الصلاحيات بناءً على الدور المختار
    if user_role == "خياط الفرع":
        st.warning("⚠️ تنبيه: دور (خياط الفرع) مخصص لمشاهدة المقاسات والتفاصيل ولا يُسمح له بإنشاء فواتير جديدة عادةً، ولكن يمكنك المتابعة للتجربة.")

    with st.form("tuboo_full_system_form"):
        st.markdown("### 1. بيانات العميل والطلب الأساسية")
        col1, col2 = st.columns(2)
        with col1:
            client_name = st.text_input("اسم العميل")
            fabric_type = st.text_input("نوع الأقمشة واللون والرقم")
        with col2:
            phone_number = st.text_input("رقم الجوال")
            order_count = st.number_input("العدد", min_value=1, value=1, format="%d")

        col3, col4 = st.columns(2)
        with col3:
            tailoring_date = st.date_input("تاريخ التفصيل", value=datetime.today())
        with col4:
            delivery_date = st.date_input("تاريخ الاستلام والتسليم")

        st.markdown("---")
        st.markdown("### 2. جدول المقاسات التفصيلية (بالإنش)")
        
        m_col1, m_col2 = st.columns(2)
        with m_col1:
            length = st.number_input("الطول", value=0.0, format="%.2f")
            shoulder = st.number_input("الكتف", value=0.0, format="%.2f")
            sleeve_length = st.number_input("طول اليد", value=0.0, format="%.2f")
            sleeve_width = st.number_input("وسع اليد (مباشر)", value=0.0, format="%.2f")
        with m_col2:
            neck = st.number_input("الرقبة", value=0.0, format="%.2f")
            width = st.number_input("الوسع (الصدر والبطن)", value=0.0, format="%.2f")
            step_val = st.number_input("الخطوة / الوسع أسفل", value=0.0, format="%.2f")
            pocket_depth = st.number_input("عمق الجيب / ملاحظة مقاس", value=0.0, format="%.2f")

        st.markdown("---")
        st.markdown("### 3. خيارات التصميم المرئي والقص")
        
        d_col1, d_col2 = st.columns(2)
        with d_col1:
            tailoring_style = st.selectbox(
                "نوع التفصيل العام",
                ["🇸🇦 سعودي", "🇶🇦 قطري", "🇰🇼 كويتي كامل", "🇦🇪 إماراتي"]
            )
            
            collar_choice = st.selectbox(
                "نوع الياقة والقلاب", 
                ["رقبة سادة خفيف", "رقبة سادة دبل", "رقبة صيني", "قلاب رسمي"]
            )
            
            sleeve_choice = st.selectbox(
                "نوع الأكمام", 
                ["يد سادة", "كبك سادة", "كبك جرزور", "كبك العاش"]
            )
            
        with d_col2:
            zipper_choice = st.selectbox(
                "نوع الجبزور",
                ["بابين", "سحاب مثلث", "سحاب مربع", "مخفي مثلث", "مخفي مربع"]
            )
            
            sewing_type = st.selectbox(
                "نوع الخياطة والغرزة", 
                ["دعسة واحدة", "دعستين مزدوجة"]
            )

        pocket_choice = st.selectbox(
            "نوع الجيب الصدري وجيوب الجانب", 
            ["مربع", "مشطوف", "دائري", "مخفي", "عادي جرزور"]
        )

        st.markdown("---")
        st.markdown("### 🔍 معاينة التصاميم البصرية المرفوعة")
        
        img_col1, img_col2 = st.columns(2)
        
        with img_col1:
            st.markdown(f"**الياقة المختارة:** {collar_choice}")
            collar_img_map = {
                "رقبة سادة خفيف": "assets/collar_plain_light.png",
                "رقبة سادة دبل": "assets/collar_plain_double.png",
                "رقبة صيني": "assets/collar_chinese.png",
                "قلاب رسمي": "assets/collar_official_flap.png"
            }
            c_path = collar_img_map.get(collar_choice, "")
            if os.path.exists(c_path):
                st.image(c_path, width=180)
            else:
                st.info(f"صورة الياقة غير متوفرة ({c_path})")

        with img_col2:
            st.markdown(f"**الجبزور المختار:** {zipper_choice}")
            zipper_img_map = {
                "بابين": "assets/zipper_babain.png",
                "سحاب مثلث": "assets/zipper_sakhap.png",
                "سحاب مربع": "assets/zipper_sakhap.png",
                "مخفي مثلث": "assets/zipper_makhfi.png",
                "مخفي مربع": "assets/zipper_makhfi.png"
            }
            z_path = zipper_img_map.get(zipper_choice, "")
            if os.path.exists(z_path):
                st.image(z_path, width=180)
            else:
                st.info(f"صورة الجبزور غير متوفرة ({z_path})")

        notes = st.text_area("ملاحظات خاصة إضافية على الطلب")
        total_price = st.number_input("إجمالي مبلغ الفاتورة (ر.س)", min_value=0.0, value=150.0)

        submitted = st.form_submit_button("💾 حفظ الطلب وإضافته لقاعدة البيانات")
        
        if submitted:
            if client_name.strip() == "":
                st.error("الرجاء إدخال اسم العميل على الأقل لحفظ الطلب!")
            else:
                order_data = {
                    "اسم العميل": client_name,
                    "الجوال": phone_number,
                    "نوع القماش": fabric_type,
                    "الياقة": collar_choice,
                    "الجبزور": zipper_choice,
                    "المبلغ": total_price,
                    "التاريخ": str(tailoring_date),
                    "المسؤول": user_role
                }
                st.session_state.orders_db.append(order_data)
                st.success(f"تم حفظ طلب العميل ({client_name}) بنجاح وإرساله إلى النظام المركزي!")

# --- الواجهة الثانية: إدارة العملاء والطلبات ---
elif navigation == " إدارة العملاء والطلبات":
    st.title("📋 سجل الطلبات والعملاء الحاليين")
    if len(st.session_state.orders_db) == 0:
        st.info("لا توجد طلبات مسجلة حتى الآن. قم بإضافة طلب جديد من القائمة الجانبية.")
    else:
        df_orders = pd.DataFrame(st.session_state.orders_db)
        st.dataframe(df_orders, use_container_width=True)
        
        if st.button("🗑️ مسح السجل وتفريغ البيانات"):
            st.session_state.orders_db = []
            st.success("تم تفريغ السجل بنجاح.")

# --- الواجهة الثالثة: تقارير وأرباح المشغل ---
elif navigation == "تقارير وأرباح المشغل":
    st.title("📊 لوحة التقارير والتحليلات المالية")
    if user_role != "مدير الفرع":
        st.error("🚫 عذراً، هذه الصفحة مخصصة لـ (مدير الفرع) فقط لأسباب أمنية وصلاحيات الإدارة.")
    else:
        st.success("أهلاً بك يا مدير الفرع في لوحة المؤشرات.")
        if len(st.session_state.orders_db) > 0:
            df_rep = pd.DataFrame(st.session_state.orders_db)
            total_income = df_rep["المبلغ"].sum()
            total_orders_count = len(df_rep)
            
            col_r1, col_r2 = st.columns(2)
            col_r1.metric("إجمالي الإيرادات المتوقعة", f"{total_income} ر.س")
            col_r2.metric("إجمالي عدد الطلبات", f"{total_orders_count}")
            
            st.markdown("### تفصيل الأرباح حسب الطلبات المسجلة")
            st.bar_chart(df_rep.set_index("اسم العميل")["المبلغ"])
        else:
            st.info("لا توجد بيانات كافية لعرض الرسوم البيانية حتى الآن.")
