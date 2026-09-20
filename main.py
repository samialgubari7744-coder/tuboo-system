import streamlit as st

# ضبط إعدادات الصفحة لتكون من اليمين لليسار (RTL) عبر ترميز HTML/CSS بسيط
st.markdown(
    """
    <style>
    body, [data-testid="stAppViewContainer"] {
        direction: rtl;
        text-align: right;
    }
    .stSelectbox, .stRadio, .stTextInput, .stNumberInput, .stDateInput, .stTextArea {
        text-align: right;
    }
    </style>
    """,
    unsafe_allow_html=True
)

st.set_page_config(page_title="خياطة تيوبو - تفاصيل الثوب", layout="centered")

st.title("خياطة تيوبو للخياطة الرجالية")
st.subheader("تسجيل تفاصيل الثوب والمقاسات والتصميم")

with st.form("tailoring_form"):
    st.markdown("### 1. بيانات العميل الأساسية")
    col1, col2 = st.columns(2)
    with col1:
        client_name = st.text_input("اسم العميل")
        fabric_type = st.text_input("نوع الأقمشة")
    with col2:
        phone_number = st.text_input("الجوال")
        count = st.number_input("العدد", min_value=1, value=1)

    col3, col4 = st.columns(2)
    with col3:
        tailoring_date = st.date_input("تاريخ التفصيل")
    with col4:
        delivery_date = st.date_input("تاريخ التسليم")

    st.markdown("---")
    st.markdown("### 2. جدول المقاسات (بالإنش)")
    
    m_col1, m_col2 = st.columns(2)
    with m_col1:
        length = st.number_input("الطول", value=0.0)
        shoulder = st.number_input("الكتف", value=0.0)
        sleeve_length = st.number_input("طول اليد", value=0.0)
    with m_col2:
        neck = st.number_input("الرقبة", value=0.0)
        width = st.number_input("الوسع", value=0.0)
        # تقسيم وسع اليد إلى مقاسين (وسع اليد العادي وعرض الأساور/الكبك)
        sub_col1, sub_col2 = st.columns(2)
        with sub_col1:
            sleeve_width_1 = st.number_input("وسع اليد (1)", value=0.0)
        with sub_col2:
            sleeve_width_2 = st.number_input("وسع اليد (2 - كبك/أساور)", value=0.0)

    st.markdown("---")
    st.markdown("### 3. خيارات التصميم والقص")
    
    # إضافة خلية الخطوة
    step_name = st.selectbox(
        "الخطوة",
        [
            "1. استقبال الطلب وأخذ المقاسات",
            "2. مرحلة القص",
            "3. مرحلة الخياطة",
            "4. مرحلة الكي والتفتيش",
            "5. جاهز للتسليم"
        ]
    )

    d_col1, d_col2 = st.columns(2)
    with d_col1:
        sleeve_type = st.selectbox(
            "تصميم اليد (الأكمام)", 
            [
                "✂️ يد سادة (عادي)", 
                "👔 يد كبك سادة", 
                "📐 عادي جبزور"
            ]
        )
        collar_type = st.selectbox(
            "تصميم الرقبة والقلاب", 
            [
                "👔 رقبة سادة دبل", 
                "👕 رقبة سادة خفيف", 
                "📌 قلاب عادي"
            ]
        )
    with d_col2:
        sewing_type = st.selectbox(
            "نوع الخياطة والغرزة", 
            [
                "🧵 دعسة", 
                "🧵🧵 دعستين", 
                "⚡ قطري", 
                "⭐ كويتي كامل", 
                "🌟 كويتي كسرة أمام"
            ]
        )

    st.markdown("#### 📍 اختيار شكل جيب الصدر")
    st.markdown("تنبيه: جميع الجيوب تكون في الجهة اليسرى")
    
    pocket_options = {
        "1": "🟦 1. جيب مربع",
        "2": "🔻 2. جيب مدبب",
        "3": "🔵 3. جيب بحافة دائرية",
        "4": "📑 4. جيب بشريحة",
        "5": "🧢 5. جيب بغطاء خارجي",
        "6": "📥 6. جيب بغطاء مخفي",
        "7": "📐 7. جيب بزاوية",
        "8": "📑 8. جيب بخط مزدوج",
        "9": "🧵 9. جيب بخياطة بارزة",
        "10": "⬜ 10. جيب بدون خياطة ظاهرة"
    }

    selected_pocket_key = st.radio(
        "اختر شكل الجيب المناسب:",
        list(pocket_options.keys()),
        format_func=lambda x: pocket_options[x]
    )

    notes = st.text_area("الملاحظات الإضافية")

    submitted = st.form_submit_button("حفظ تفاصيل الطلب والمقاسات")
    if submitted:
        st.success(f"تم حفظ تفاصيل الطلب بنجاح للخطوة: {step_name}!")
