import streamlit as st
import os
import pandas as pd
from datetime import datetime

# إعداد الصفحة وتفعيل اتجاه الكتابة وتصميم الفخامة البصرية
st.set_page_config(page_title="مشغل تيوبو الاحترافي", page_icon="🧵", layout="wide")

# تصميم الألوان والستايلات المشابهة لأنظمة "شفق" الفخمة (Dark/Modern Luxury Theme)
st.markdown("""
<style>
    /* خلفية التطبيق العامة واتجاه اليمين لليسار */
    .stApp {
        direction: rtl;
        text-align: right;
        background-color: #0e1117;
        color: #ffffff;
    }
    
    /* تنسيق العناوين الرئيسية */
    h1, h2, h3, h4 {
        color: #00d2ff;
        font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
        text-align: right !important;
    }
    
    /* تنسيق الكروت والإحصائيات */
    .metric-card {
        background: linear-gradient(135deg, #1f2937 0%, #111827 100%);
        border: 1px solid #374151;
        padding: 20px;
        border-radius: 12px;
        box-shadow: 0 4px 6px rgba(0, 0, 0, 0.3);
        text-align: center;
    }
    
    /* زر الإرسال والحفظ الاحترافي */
    .stButton>button {
        background: linear-gradient(90deg, #0072ff 0%, #00c6ff 100%);
        color: white;
        font-weight: bold;
        border-radius: 8px;
        padding: 10px 24px;
        border: none;
        box-shadow: 0 4px 10px rgba(0, 114, 255, 0.4);
        width: 100%;
    }
    .stButton>button:hover {
        background: linear-gradient(90deg, #0056b3 0%, #0099cc 100%);
        color: #fff;
    }

    /* تنسيق الحقول والجداول */
    label, p, div {
        text-align: right !important;
    }
    .stTextInput input, .stNumberInput input, .stSelectbox, .stTextArea textarea {
        direction: rtl;
        text-align: right;
        background-color: #1f2937 !important;
        color: white !important;
        border-radius: 6px !important;
    }
</style>
""", unsafe_allow_html=True)

# الشريط الجانبي الفاخر
st.sidebar.markdown("## 🧵 نظام تيوبو المطور")
st.sidebar.markdown("---")
user_role = st.sidebar.selectbox(
    "👤 حدد الصلاحية الحالية",
    ["مدير المشغل العام", "موظف استقبال مبيعات", "خياط قسم التفصيل"]
)

st.sidebar.markdown("---")
selected_tab = st.sidebar.radio(
    "🚀 أقسام النظام الرئيسية",
    ["✨ لوحة التحكم والتحليلات", "📝 تسجيل قياسات وطلب جديد", "👥 سجل العملاء والأرشيف", "⚙️ إعدادات الصور والتصاميم"]
)

# ذاكرة النظام المؤقتة
if 'orders_db' not in st.session_state:
    st.session_state.orders_db = [
        {"اسم العميل": "سلطان العتيبي", "الجوال": "0501112233", "نوع القماش": "ياباني سوبر ديلوكس", "الياقة": "رقبة سادة دبل", "المبلغ": 250.0, "التاريخ": "2026-06-01", "الحالة": "قيد التجهيز"},
        {"اسم العميل": "فهد القحطاني", "الجوال": "0554445566", "نوع القماش": "كوري ملكي", "الياقة": "رقبة صيني", "المبلغ": 300.0, "التاريخ": "2026-06-02", "الحالة": "جاهز للاستلام"}
    ]

# ================= 1. لوحة التحكم والتحليلات (Dashboard) =================
if selected_tab == "✨ لوحة التحكم والتحليلات":
    st.title("📊 لوحة المؤشرات الذكية - مشغل تيوبو")
    st.markdown("مرحباً بك مجدداً في نظام الإدارة المتقدم. نظرة عامة على أداء المشغل:")
    
    # بطاقات إحصائية ملونة تشبه أنظمة "شفق"
    c1, c2, c3, c4 = st.columns(4)
    
    total_orders = len(st.session_state.orders_db)
    total_revenue = sum([item["المبلغ"] for item in st.session_state.orders_db]) if total_orders > 0 else 0
    
    with c1:
        st.markdown(f"""
            <div class="metric-card">
                <h3>📦 إجمالي الطلبات</h3>
                <p style="font-size: 28px; font-weight: bold; color: #00d2ff;">{total_orders}</p>
            </div>
        """, unsafe_allow_html=True)
    with c2:
        st.markdown(f"""
            <div class="metric-card">
                <h3>💰 الإيرادات العامة</h3>
                <p style="font-size: 28px; font-weight: bold; color: #10B981;">{total_revenue} ر.س</p>
            </div>
        """, unsafe_allow_html=True)
    with c3:
        st.markdown("""
            <div class="metric-card">
                <h3>⭐ تقييم العملاء</h3>
                <p style="font-size: 28px; font-weight: bold; color: #F59E0B;">4.9 / 5</p>
            </div>
        """, unsafe_allow_html=True)
    with c4:
        st.markdown("""
            <div class="metric-card">
                <h3>⚡ حالة النظام</h3>
                <p style="font-size: 20px; font-weight: bold; color: #3B82F6;">متصل ومستقر</p>
            </div>
        """, unsafe_allow_html=True)

    st.markdown("---")
    st.subheader("📈 تتبع مبيعات الطلبات الحية")
    if total_orders > 0:
        df_chart = pd.DataFrame(st.session_state.orders_db)
        st.bar_chart(df_chart.set_index("اسم العميل")["المبلغ"])
    else:
        st.info("لا توجد بيانات كافية للرسوم البيانية حالياً.")

# ================= 2. تسجيل قياسات وطلب جديد =================
elif selected_tab == "📝 تسجيل قياسات وطلب جديد":
    st.title("✂️ محطة تفصيل وقياسات الثوب الرجالي")
    
    with st.form("advanced_order_form"):
        st.markdown("### 1️⃣ بيانات العميل الأساسية")
        col_a, col_b = st.columns(2)
        with col_a:
            c_name = st.text_input("اسم العميل الكريم")
            c_fabric = st.text_input("نوع ورقم القماش واللون")
        with col_b:
            c_phone = st.text_input("رقم الجوال الشخصي")
            c_count = st.number_input("عدد الأثواب المطلوبة", min_value=1, value=1)

        st.markdown("---")
        st.markdown("### 2️⃣ تفاصيل المقاسات الدقيقة (بالإنش)")
        
        m1, m2 = st.columns(2)
        with m1:
            length = st.number_input("الطول", value=0.0, format="%.2f")
            shoulder = st.number_input("الكتف", value=0.0, format="%.2f")
            sleeve = st.number_input("طول اليد", value=0.0, format="%.2f")
            s_width = st.number_input("وسع اليد", value=0.0, format="%.2f")
        with m2:
            neck = st.number_input("الرقبة", value=0.0, format="%.2f")
            chest_w = st.number_input("الوسع (الصدر والبطن)", value=0.0, format="%.2f")
            bottom_w = st.number_input("الخطوة / الوسع أسفل", value=0.0, format="%.2f")
            pocket_n = st.number_input("عمق الجيب", value=0.0, format="%.2f")

        st.markdown("---")
        st.markdown("### 3️⃣ القصات والتصاميم المرئية التفاعلية")
        
        d1, d2 = st.columns(2)
        with d1:
            style_type = st.selectbox("طراز التفصيل العام", ["🇸🇦 سعودي كلاسيك", "🇶🇦 قطري حديث", "🇰🇼 كويتي فاخر", "🇦🇪 إماراتي تطريز"])
            collar_type = st.selectbox("نوع الياقة والقلاب", ["رقبة سادة خفيف", "رقبة سادة دبل", "رقبة صيني", "قلاب رسمي"])
            sleeve_type = st.selectbox("نوع الأكمام", ["يد سادة", "كبك سادة", "كبك جرزور", "كبك العاش"])
        with d2:
            zipper_type = st.selectbox("نوع الجبزور", ["بابين", "سحاب مثلث", "سحاب مربع", "مخفي مثلث"])
            sewing_style = st.selectbox("نوع الخياطة والغرزة", ["دعسة واحدة", "دعستين مزدوجة"])

        st.markdown("---")
        st.markdown("### 👁️ المعاينة البصرية الحية للقصات")
        prev_col1, prev_col2 = st.columns(2)
        
        with prev_col1:
            st.write(f"**الياقة المختارة:** {collar_type}")
            collar_map = {
                "رقبة سادة خفيف": "assets/collar_plain_light.png",
                "رقبة سادة دبل": "assets/collar_plain_double.png",
                "رقبة صيني": "assets/collar_chinese.png",
                "قلاب رسمي": "assets/collar_official_flap.png"
            }
            c_img = collar_map.get(collar_type, "")
            if os.path.exists(c_img):
                st.image(c_img, width=170)
            else:
                st.info(f"صورة الياقة قيد التحميل ({c_img})")

        with prev_col2:
            st.write(f"**الجبزور المختار:** {zipper_type}")
            z_img = "assets/zipper_babain.png"
            if os.path.exists(z_img):
                st.image(z_img, width=170)
            else:
                st.info("صورة الجبزور قيد التحميل في assets")

        notes = st.text_area("ملاحظات خاصة على الثوب والتطريز")
        price = st.number_input("إجمالي السعر (ر.س)", min_value=0.0, value=200.0)

        submit_btn = st.form_submit_button("✨ حفظ و اعتماد الطلب وإصدار الفاتورة")
        
        if submit_btn:
            if c_name == "":
                st.error("الرجاء إدخال اسم العميل على الأقل!")
            else:
                new_order = {
                    "اسم العميل": c_name,
                    "الجوال": c_phone,
                    "نوع القماش": c_fabric,
                    "الياقة": collar_type,
                    "المبلغ": price,
                    "التاريخ": str(datetime.today().date()),
                    "الحالة": "جديد"
                }
                st.session_state.orders_db.append(new_order)
                st.success(f"🎉 تم تسجيل طلب العميل ({c_name}) بنجاح تام وإضافته للنظام!")

# ================= 3. سجل العملاء والأرشيف =================
elif selected_tab == "👥 سجل العملاء والأرشيف":
    st.title("📁 سجل أرشيف العملاء والطلبات السابقة")
    if len(st.session_state.orders_db) > 0:
        df_all = pd.DataFrame(st.session_state.orders_db)
        st.dataframe(df_all, use_container_width=True)
        
        if st.button("🗑️ مسح وإفراغ الأرشيف بالكامل"):
            st.session_state.orders_db = []
            st.success("تم تفريغ الأرشيف.")
    else:
        st.info("لا توجد طلبات مسجلة في الأرشيف حالياً.")

# ================= 4. إعدادات الصور والتصاميم =================
elif selected_tab == "⚙️ إعدادات الصور والتصاميم":
    st.title("⚙️ حالة مجلد الأصول والتصاميم البصرية")
    st.write("يتحقق النظام من جاهزية صور الياقات والكبكات والجبزور داخل مجلد `assets` على مستودعك في GitHub:")
    
    files_to_check = [
        "assets/collar_plain_light.png",
        "assets/collar_plain_double.png",
        "assets/collar_chinese.png",
        "assets/collar_official_flap.png",
        "assets/zipper_babain.png"
    ]
    
    for f in files_to_check:
        if os.path.exists(f):
            st.success(f"✅ الملف متوفر وجاهز: `{f}`")
        else:
            st.warning(f"⚠️ الملف غير متوفر أو مساره يحتاج لمراجعة: `{f}`")
