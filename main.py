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
    /* تعديل محاذاة العناوين وحقول الإدخال لتتناسب مع اللغة العربية */
    label, h1, h2, h3, h4, p, div {
        text-align: right !important;
    }
    .stTextInput input, .stNumberInput input, .stSelectbox, .stTextArea textarea {
        direction: rtl;
        text-align: right;
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
        
        # تقسيم خلية "وسع اليد" إلى خليتين في نفس السطر لتسجيل مقاسين
        st.markdown("وسع اليد (مقاسين)")
        s_col1, s_col2 = st.columns(2)
        with s_col1:
            sleeve_width_1 = st.number_input("الأول", value=0.0, key="sw1")
        with s_col2:
            sleeve_width_2 = st.number_input("الثاني", value=0.0, key="sw2")

    with m_col2:
        neck = st.number_input("الرقبة", value=0.0)
        width = st.number_input("الوسع", value=0.0)
        # خلية "الخطوة" تحت وسع اليد وبنفس تنسيق باقي خلايا جدول المقاسات
        step_val = st.number_input("الخطوة", value=0.0)

    st.markdown("---")
    st.markdown("### 3. خيارات التصميم والقص")
    
    d_col1, d_col2 = st.columns(2)
    with d_col1:
        sleeve_type = st.selectbox(
            "تصميم اليد (الأكمام)", 
            [
                "✂️ يد سادة (عادي)", 
                "👔 يد كبك سادة", 
                "📐 عادي جيبرور"
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

    # اختيار شكل جيب الصدر ضمن خيارات التصميم والقص
    st.markdown("#### 📍 اختيار شكل جيب الصدر")
    st.markdown("تنبيه: جميع الجيوب تكون في الجهة اليسرى")
    
    pocket_options = {
        "1": "🟦 1. جيب مربع (كلاسيكي وعملي للاستخدام اليومي)",
        "2": "🔻 2. جيب مدبب (شكل أنيق لمظهر كلاسيكي راقٍ)",
        "3": "🔵 3. جيب بحافة دائرية (ناعم وانسيابي بمظهر هادئ)",
        "4": "📑 4. جيب بشريحة (تصميم بسيط بشريحة رفيعة على الحافة)",
        "5": "🧢 5. جيب بغطاء خارجي (كلاسيكي وفخم مع غطاء وزر)",
        "6": "📥 6. جيب بغطاء مخفي (غطاء داخلي مخفي بمظهر ناعم ومرتب)",
        "7": "📐 7. جيب بزاوية (لمسة عصرية بتصميم بزاوية مميزة)",
        "8": "📑 8. جيب بخط مزدوج (خط مزدوج أنيق يضيف تفصيلاً مميزاً)",
        "9": "🧵 9. جيب بخياطة بارزة (خياطة بارزة على الحافة تعطي مظهراً أنيقاً)",
        "10": "⬜ 10. جيب بدون خياطة ظاهرة (تصميم عصري بسيط بدون خياطة ظاهرة)"
    }

    selected_pocket_key = st.radio(
        "اختر شكل الجيب المناسب:",
        list(pocket_options.keys()),
        format_func=lambda x: pocket_options[x]
    )

    notes = st.text_area("الملاحظات الإضافية")

    submitted = st.form_submit_button("حفظ تفاصيل الطلب والمقاسات")
    if submitted:
        st.success(f"تم حفظ تفاصيل الطلب بنجاح! مقاسا وسع اليد: ({sleeve_width_1}, {sleeve_width_2}) | الخطوة: {step_val}")
