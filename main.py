import streamlit as st

# إعداد الصفحة وتفعيل اتجاه الكتابة من اليمين لليسار (RTL)
st.set_page_config(page_title="خياطة تيوبو - النظام المطور", layout="centered")

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

st.title("خياطة تيوبو للخياطة الرجالية")
st.subheader("نظام إدارة المقاسات والتصاميم البصرية المتقدمة")

with st.form("tailoring_system_form"):
    st.markdown("### 1. بيانات العميل الأساسية")
    col1, col2 = st.columns(2)
    with col1:
        client_name = st.text_input("اسم العميل")
        fabric_type = st.text_input("نوع الأقمشة")
    with col2:
        phone_number = st.text_input("الجوال")
        count = st.number_input("العدد", min_value=1, value=1, format="%d")

    col3, col4 = st.columns(2)
    with col3:
        tailoring_date = st.date_input("تاريخ التفصيل")
    with col4:
        delivery_date = st.date_input("تاريخ التسليم")

    st.markdown("---")
    st.markdown("### 2. جدول المقاسات (بالإنش)")
    
    m_col1, m_col2 = st.columns(2)
    with m_col1:
        length = st.number_input("الطول", value=0.0, format="%.2f")
        shoulder = st.number_input("الكتف", value=0.0, format="%.2f")
        sleeve_length = st.number_input("طول اليد", value=0.0, format="%.2f")
        sleeve_width = st.text_input("وسع اليد (مباشر)")
    with m_col2:
        neck = st.number_input("الرقبة", value=0.0, format="%.2f")
        width = st.number_input("الوسع", value=0.0, format="%.2f")
        step_val = st.number_input("الخطوة", value=0.0, format="%.2f")

    st.markdown("---")
    st.markdown("### 3. خيارات التصميم والقص المرئي")
    
    d_col1, d_col2 = st.columns(2)
    with d_col1:
        tailoring_style = st.selectbox(
            "نوع التفصيل",
            ["🇸🇦 سعودي", "🇶🇦 قطري", "🇰🇼 كويتي كامل", "🇰🇼 كويتي كسرة أمام", "🇦🇪 إماراتي"]
        )
        
        collar_type = st.selectbox(
            "نوع الياقة والقلاب", 
            ["👔 رقبة سادة خفيف", "👔 رقبة سادة دبل", "⭕ رقبة صيني", "📐 قلاب رسمي"]
        )
        
        sleeve_type = st.selectbox(
            "نوع الأكمام", 
            ["👕 يد سادة", "📌 يد كبك سادة", "📌 كبك جرزور", "🌟 كبك العاش"]
        )
        
    with d_col2:
        # أسماء خيارات الجبزور المطابقة للصور الشفافة التي أرفقتها
        zipper_type = st.selectbox(
            "نوع الجبزور",
            ["بابين", "سحاب مثلث", "سحاب مربع", "مخفي مثلث", "مخفي مربع"]
        )
        
        sewing_type = st.selectbox(
            "نوع الخياطة والغرزة", 
            ["🧵 دعسة", "🧵🧵 دعستين"]
        )

    pocket_choice = st.selectbox(
        "نوع الجيب", 
        ["🟦 مربع", "🔻 مشطوف", "🔵 دائري", "📑 مخفي", "📐 عادي جرزور"]
    )

    # عرض الصورة الشفافة للجبزور تلقائياً بناءً على الاختيار
    st.markdown("#### معاينة المخطط البصري للجبزور:")
    try:
        if zipper_type == "بابين":
            st.image("assets/zipper_babain.png", width=220, caption="مخطط تصميم بابين")
        elif zipper_type in ["سحاب مثلث", "سحاب مربع"]:
            st.image("assets/zipper_sakhap.png", width=220, caption="مخطط تصميم السحاب")
        elif zipper_type in ["مخفي مثلث", "مخفي مربع"]:
            st.image("assets/zipper_makhfi.png", width=220, caption="مخطط التصميم المخفي")
    except:
        st.info("ملاحظة: سيتم عرض الصورة الشفافة فور وضعها في مجلد assets بالأسماء الصحيحة.")

    notes = st.text_area("الملاحظات الإضافية")

    submitted = st.form_submit_button("حفظ وحساب الطلب")
    if submitted:
        st.success(f"تم حفظ تفاصيل العميل {client_name} بنجاح! | الجبزور: {zipper_type}")
