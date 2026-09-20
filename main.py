import streamlit as st

# إعداد الصفحة وتفعيل دعم الاتجاه من اليمين لليسار (RTL)
st.set_page_config(page_title="خياطة تيوبو - تفاصيل الثوب", layout="centered")

st.markdown("""
<style>
    /* توجيه كافة العناصر والنصوص من اليمين إلى اليسار */
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
    /* إخفاء أزرار الزائد والناقص الخاصة بحقول الأرقام لإظهارها بشكل نظيف */
    div[data-baseweb="spinbutton"] button {
        display: none !important;
    }
</style>
""", unsafe_allow_html=True)

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
        
        # خلية وسع اليد أصبحت خانة نصية واحدة لكتابة مقاسين معاً
        sleeve_width = st.text_input("وسع اليد (اكتب مقاسين هنا)")

    with m_col2:
        neck = st.number_input("الرقبة", value=0.0, format="%.2f")
        width = st.number_input("الوسع", value=0.0, format="%.2f")
        step_val = st.number_input("الخطوة", value=0.0, format="%.2f")

    st.markdown("---")
    st.markdown("### 3. خيارات التصميم والقص")
    
    d_col1, d_col2 = st.columns(2)
    with d_col1:
        tailoring_style = st.selectbox(
            "نوع التفصيل",
            [
                "🇸🇦 سعودي",
                "🇶🇦 قطري",
                "🇰🇼 كويتي كامل",
                "🇰🇼 كويتي كسرة أمام",
                "🇦🇪 إماراتي"
            ]
        )
        sleeve_type = st.selectbox(
            "تصميم اليد (الأكمام)", 
            [
                "✂️ يد سادة (عادي)", 
                "👔 يد كبك سادة", 
                "📐 عادي جيبرور"
            ]
        )
    with d_col2:
        collar_type = st.selectbox(
            "تصميم الرقبة والقلاب", 
            [
                "👔 رقبة سادة دبل", 
                "👕 رقبة سادة خفيف", 
                "📌 قلاب عادي"
            ]
        )
        sewing_type = st.selectbox(
            "نوع الخياطة والغرزة", 
            [
                "🧵 دعسة", 
                "🧵🧵 دعستين"
            ]
        )

    pocket_options = [
        "🟦 1. جيب مربع (كلاسيكي وعملي للاستخدام اليومي)",
        "🔻 2. جيب مدبب (شكل أنيق لمظهر كلاسيكي راقٍ)",
        "🔵 3. جيب بحافة دائرية (ناعم وانسيابي بمظهر هادئ)",
        "📑 4. جيب بشريحة (تصميم بسيط بشريحة رفيعة على الحافة)",
        "🧢 5. جيب بغطاء خارجي (كلاسيكي وفخم مع غطاء وزر)",
        "📥 6. جيب بغطاء مخفي (غطاء داخلي مخفي بمظهر ناعم ومرتب)",
        "📐 7. جيب بزاوية (لمسة عصرية بتصميم بزاوية مميزة)",
        "8. جيب بخط مزدوج (خط مزدوج أنيق يضيف تفصيلاً مميزاً)",
        "9. جيب بخياطة بارزة (خياطة بارزة على الحافة تعطي مظهراً أنيقاً)",
        "10. جيب بدون خياطة ظاهرة (تصميم عصري بسيط بدون خياطة ظاهرة)"
    ]
    
    pocket_choice = st.selectbox("اختيار شكل جيب الصدر (جميع الجيوب في الجهة اليسرى)", pocket_options)

    notes = st.text_area("الملاحظات الإضافية")

    submitted = st.form_submit_button("حفظ تفاصيل الطلب والمقاسات")
    if submitted:
        st.success(f"تم حفظ تفاصيل الطلب بنجاح! وسع اليد: {sleeve_width}")
