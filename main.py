import streamlit as st

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
        sleeve_width = st.number_input("وسع اليد", value=0.0)

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

    st.markdown("---")
    st.markdown("### 4. جيب الصدر (أشكال الجيوب القياسية)")
    
    chest_pocket = st.selectbox(
        "اختر شكل جيب الصدر المفضل",
        [
            "1️⃣ جيب مربع (كلاسيكي وعملي مناسب للاستخدام اليومي)[span_1](start_span)[span_1](end_span)",
            "2️⃣ جيب مدبب (شكل أنيق لمظهر كلاسيكي راقٍ)[span_2](start_span)[span_2](end_span)",
            "3️⃣ جيب بحافة دائرية (ناعمه وانسيابي يعطي مظهراً هادئاً)[span_3](start_span)[span_3](end_span)",
            "4️⃣ جيب بشريحة (تصميم بسيط وأنيق شريحة رفيعة على الحافة)[span_4](start_span)[span_4](end_span)",
            "5️⃣ جيب بغطاء خارجي (كلاسيكي وفخم مع غطاء وزر)[span_5](start_span)[span_5](end_span)",
            "6️⃣ جيب بغطاء مخفي (غطاء داخلي مخفي مظهر ناعم ومرتب)[span_6](start_span)[span_6](end_span)",
            "7️⃣ جيب بزاوية (لمسة عصري بتصميم بزاوية مميزة)[span_7](start_span)[span_7](end_span)",
            "8️⃣ جيب بخط مزدوج (خط مزدوج أنيق يضيف detail أنيق)[span_8](start_span)[span_8](end_span)",
            "9️⃣ جيب بخياطة بارزة (خياطة بارزة على الحافة تعطي مظهراً أنيقاً)[span_9](start_span)[span_9](end_span)",
            "🔟 جيب بدون خياطة ظاهرة (تصميم عصري بسيط بدون أي خياطة ظاهرة)[span_10](start_span)[span_10](end_span)"
        ]
    )

    notes = st.text_area("الملاحظات الإضافية (تنبيه: جميع الجيوب تكون في الجهة اليسرى)")

    submitted = st.form_submit_button("حفظ تفاصيل الطلب والمقاسات")
    if submitted:
        st.success("تم حفظ تفاصيل الطلب والمقاسات بنجاح في خياطة تيوبو!")
