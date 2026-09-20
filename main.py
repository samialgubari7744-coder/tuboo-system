import streamlit as st

st.set_page_config(page_title="خياطة تيوبو - تفاصيل الثوب", layout="centered")

st.title("خياطة تيوبو للخياطة الرجالية")
st.subheader("تسجيل تفاصيل الثوب والمقاسات")

with st.form("tailoring_form"):
    st.markdown("### بيانات العميل الأساسية")
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
    st.markdown("### جدول المقاسات")
    
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
    st.markdown("### خيارات التصميم والقص")
    
    d_col1, d_col2 = st.columns(2)
    with d_col1:
        sleeve_type = st.selectbox("نوع اليد", ["يد سادة", "يد كبك سادة", "عادي جيبرور"])
        collar_type = st.selectbox("نوع القلاب / الرقبة", ["نوع القلاب", "رقبة سادة دبل", "رقبة سادة خفيف"])
    with d_col2:
        pocket_type = st.selectbox("نوع الجيب", ["جيب بدون حشوة", "جيوب أخرى"])
        sewing_type = st.selectbox("نوع الخياطة", ["دعسة", "دعستين", "قطري", "كويتي كامل", "كويتي كسرة أمام"])

    notes = st.text_area("الملاحظات")

    submitted = st.form_submit_button("حفظ وحفظ المقاسات")
    if submitted:
        st.success("تم حفظ تفاصيل المقاسات والطلب بنجاح في خياطة تيوبو!")
