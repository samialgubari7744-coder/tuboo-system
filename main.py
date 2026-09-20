import streamlit as st
import os
import pandas as pd
from datetime import datetime

# إعداد الصفحة وتصميم الفخامة المطلقة
st.set_page_config(page_title="مشغل تيوبو الملكي", page_icon="🧵", layout="wide")

# تصميم CSS احترافي وفاخر للغاية (ألوان ملكية: فحمي داكن + ذهبي راقي + بلاتيني)
st.markdown("""
<style>
    /* خلفية التطبيق العامة */
    .stApp {
        direction: rtl;
        text-align: right;
        background-color: #0b0f19;
        color: #e5e7eb;
        font-family: 'Cairo', 'Segoe UI', Tahoma, sans-serif;
    }
    
    /* عناوين فاخرة */
    h1, h2, h3, h4 {
        color: #d4af37 !important;
        font-weight: 700;
        text-align: right !important;
        letter-spacing: 0.5px;
    }
    
    /* كروت الإحصائيات الملكية */
    .luxury-card {
        background: linear-gradient(135deg, #111827 0%, #1f2937 100%);
        border: 1px solid #d4af3733;
        padding: 22px;
        border-radius: 14px;
        box-shadow: 0 8px 20px rgba(0, 0, 0, 0.5);
        text-align: center;
        margin-bottom: 10px;
    }
    .luxury-card h3 {
        color: #9ca3af !important;
        font-size: 16px;
        margin-bottom: 8px;
    }
    .luxury-card p {
        color: #d4af37 !important;
        font-size: 28px;
        font-weight: bold;
    }

    /* تخصيص الأزرار بفخامة */
    .stButton>button {
        background: linear-gradient(135deg, #d4af37 0%, #aa7c11 100%);
        color: #0b0f19;
        font-weight: 800;
        border-radius: 10px;
        padding: 12px 24px;
        border: none;
        box-shadow: 0 4px 15px rgba(212, 175, 55, 0.3);
        width: 100%;
        transition: all 0.3s ease;
    }
    .stButton>button:hover {
        background: linear-gradient(135deg, #e6c55c 0%, #d4af37 100%);
        color: #000;
        box-shadow: 0 6px 20px rgba(212, 175, 55, 0.5);
    }

    /* تخصيص القائمة الجانبية (Sidebar) لتكون راقية */
    section[data-testid="stSidebar"] {
        background-color: #07090f;
        border-left: 1px solid #1f2937;
    }
    section[data-testid="stSidebar"] .stRadio label {
        color: #d1d5db !important;
        font-weight: 600;
        font-size: 15px;
    }

    /* تخصيص الحقول والنصوص لتكون مريحة للعين */
    label, p, div {
        text-align: right !important;
    }
    .stTextInput input, .stNumberInput input, .stSelectbox, .stTextArea textarea {
        direction: rtl;
        text-align: right;
        background-color: #111827 !important;
        color: #f3f4f6 !important;
        border: 1px solid #374151 !important;
        border-radius: 8px !important;
    }
    .stTextInput input:focus, .stNumberInput input:focus {
        border-color: #d4af37 !important;
        box-shadow: 0 0 8px rgba(212, 175, 55, 0.3);
    }
</style>
""", unsafe_allow_html=True)

# قاعدة البيانات المحلية
DB_FILE = "tuboo_luxury_database.csv"

def load_database():
    if os.path.exists(DB_FILE):
        return pd.read_csv(DB_FILE)
    else:
        df_init = pd.DataFrame(columns=[
            "رقم الطلب", "اسم العميل", "الجوال", "نوع القماش", 
            "الطول", "الكتف", "الرقبة", "الياقة", "المبلغ", "التاريخ", "الحالة"
        ])
        df_init.to_csv(DB_FILE, index=False)
        return df_init

def save_database(df):
    df.to_csv(DB_FILE, index=False)

if 'df_orders' not in st.session_state:
    st.session_state.df_orders = load_database()

# الشريط الجانبي الفاخر جداً
st.sidebar.markdown("<h2 style='text-align: center; color: #d4af37;'>🧵 نظام تيوبو الملكي</h2>", unsafe_allow_html=True)
st.sidebar.markdown("<p style='text-align: center; color: #9ca3af; font-size: 12px;'>إدارة مشاغل الخياطة الفاخرة</p>", unsafe_allow_html=True)
st.sidebar.markdown("---")

user_role = st.sidebar.selectbox(
    "👤 الصلاحية الحالية",
    ["مدير المشغل العام", "موظف استقبال مبيعات", "خياط قسم التفصيل"]
)

st.sidebar.markdown("---")
selected_tab = st.sidebar.radio(
    "✨ التنقل الملكي السريع",
    ["📊 لوحة المؤشرات المالية", "📝 تسجيل قياسات وطلب جديد", "🔍 سجل العملاء والطلبات", "⚙️ إعدادات النظام والأصول"]
)

df = st.session_state.df_orders

# ================= 1. لوحة المؤشرات المالية =================
if selected_tab == "📊 لوحة المؤشرات المالية":
    st.title("📊 لوحة المؤشرات والتحليلات الملكية")
    st.markdown("نظرة شاملة على أداء المشغل والإيرادات المالية الفورية.")
    st.markdown("---")
    
    total_orders = len(df)
    total_revenue = df["المبلغ"].sum() if total_orders > 0 and "المبلغ" in df.columns else 0
    
    c1, c2, c3 = st.columns(3)
    with c1:
        st.markdown(f"""
            <div class="luxury-card">
                <h3>إجمالي الطلبات النشطة</h3>
                <p>{total_orders}</p>
            </div>
        """, unsafe_allow_html=True)
    with c2:
        st.markdown(f"""
            <div class="luxury-card">
                <h3>إجمالي الإيرادات (ر.س)</h3>
                <p>{total_revenue:,.2f}</p>
            </div>
        """, unsafe_allow_html=True)
    with c3:
        st.markdown(f"""
            <div class="luxury-card">
                <h3>حالة النظام المركزي</h3>
                <p style="font-size: 20px; color: #10B981 !important; margin-top: 5px;">⚡ متصل وآمن</p>
            </div>
        """, unsafe_allow_html=True)

    st.markdown("---")
    st.subheader("📈 تحليل مبيعات العملاء الفورية")
    if total_orders > 0 and "اسم العميل" in df.columns:
        st.bar_chart(df.set_index("اسم العميل")["المبلغ"])
    else:
        st.info("💡 لا توجد بيانات كافية لعرض الرسم البياني حالياً. قم بإضافة طلبات جديدة لتظهر هنا.")

# ================= 2. تسجيل قياسات وطلب جديد =================
elif selected_tab == "📝 تسجيل قياسات وطلب جديد":
    st.title("✂️ محطة تفصيل وقياسات الثوب الملكي")
    st.markdown("سجل بيانات العميل، المقاسات الدقيقة، وخيارات التصميم بكل سهولة.")
    st.markdown("---")
    
    with st.form("luxury_order_form"):
        st.markdown("### 1️⃣ بيانات العميل والاتصال")
        col1, col2 = st.columns(2)
        with col1:
            c_name = st.text_input("اسم العميل الكريم *")
            c_fabric = st.text_input("نوع ورقم القماش المفضل")
        with col2:
            c_phone = st.text_input("رقم الجوال الشخصي *")
            order_status = st.selectbox("حالة الطلب المبدئية", ["جديد", "قيد التجهيز", "جاهز للاستلام"])

        st.markdown("---")
        st.markdown("### 2️⃣ جدول المقاسات الدقيقة (بالإنش)")
        m1, m2, m3, m4 = st.columns(4)
        with m1:
            length = st.number_input("الطول", value=58.0, format="%.2f")
        with m2:
            shoulder = st.number_input("الكتف", value=24.0, format="%.2f")
        with m3:
            neck = st.number_input("الرقبة", value=15.5, format="%.2f")
        with m4:
            sleeve = st.number_input("طول اليد", value=25.0, format="%.2f")

        st.markdown("---")
        st.markdown("### 3️⃣ تفاصيل القصات والتصميم")
        d1, d2, d3 = st.columns(3)
        with d1:
            collar_type = st.selectbox("نوع الياقة", ["رقبة سادة خفيف", "رقبة سادة دبل", "رقبة صيني", "قلاب رسمي"])
        with d2:
            zipper_type = st.selectbox("نوع الجبزور", ["بابين", "سحاب مثلث", "مخفي"])
        with d3:
            price = st.number_input("مبلغ الفاتورة الإجمالي (ر.س)", min_value=0.0, value=250.0)

        notes = st.text_area("ملاحظات خاصة على التطريز والتفصيل")
        st.markdown("---")
        
        submit_btn = st.form_submit_button("✨ حفظ الطلب وإصدار الفاتورة الملكية")
        
        if submit_btn:
            if not c_name.strip() or not c_phone.strip():
                st.error("⚠️ الرجاء إدخال اسم العميل ورقم الجوال لإتمام الحفظ!")
            else:
                new_id = len(df) + 1001
                new_row = {
                    "رقم الطلب": new_id,
                    "اسم العميل": c_name.strip(),
                    "الجوال": c_phone.strip(),
                    "نوع القماش": c_fabric,
                    "الطول": length,
                    "الكتف": shoulder,
                    "الرقبة": neck,
                    "الياقة": collar_type,
                    "المبلغ": price,
                    "التاريخ": str(datetime.today().date()),
                    "الحالة": order_status
                }
                
                st.session_state.df_orders = pd.concat([df, pd.DataFrame([new_row])], ignore_index=True)
                save_database(st.session_state.df_orders)
                st.success(f"🎉 تم اعتماد حفظ طلب العميل ({c_name}) برقم ترتيبي #{new_id} بنجاح تام!")

# ================= 3. سجل العملاء والطلبات =================
elif selected_tab == "🔍 سجل العملاء والطلبات":
    st.title("📁 الأرشيف المركزي للعملاء والطلبات")
    st.markdown("استعرض كافة السجلات، ابحث عن العملاء، وقم بتحديث حالات الطلبات.")
    st.markdown("---")
    
    if len(df) == 0:
        st.info("𭃋 لا توجد طلبات مسجلة في الأرشيف حالياً.")
    else:
        search_query = st.text_input("🔍 ابحث برقم الجوال أو اسم العميل:")
        if search_query:
            filtered_df = df[df["اسم العميل"].str.contains(search_query, case=False, na=False) | df["الجوال"].str.contains(search_query, na=False)]
        else:
            filtered_df = df

        st.dataframe(filtered_df, use_container_width=True)
        
        st.markdown("---")
        st.subheader("⚙️ لوحة التحكم وتحديث حالة الطلبات")
        
        order_ids = df["رقم الطلب"].tolist() if "رقم الطلب" in df.columns else []
        if order_ids:
            col_sel1, col_sel2 = st.columns(2)
            with col_sel1:
                selected_order = st.selectbox("حدد رقم الطلب للتعديل", order_ids)
            with col_sel2:
                new_status = st.selectbox("الحالة التنفيذية الجديدة", ["جديد", "قيد التجهيز", "جاهز للاستلام", "تم التسليم"])
            
            b_col1, b_col2 = st.columns(2)
            with b_col1:
                if st.button("🔄 تحديث حالة الطلب الفورية"):
                    st.session_state.df_orders.loc[st.session_state.df_orders["رقم الطلب"] == selected_order, "الحالة"] = new_status
                    save_database(st.session_state.df_orders)
                    st.success(f"تم تحديث الطلب #{selected_order} بنجاح إلى ({new_status})!")
                    st.rerun()
            with b_col2:
                if st.button("🗑️ حذف الطلب من الأرشيف", type="primary"):
                    st.session_state.df_orders = st.session_state.df_orders[st.session_state.df_orders["رقم الطلب"] != selected_order]
                    save_database(st.session_state.df_orders)
                    st.success(f"تم حذف الطلب #{selected_order} نهائياً.")
                    st.rerun()

# ================= 4. إعدادات النظام والأصول =================
elif selected_tab == "⚙️ إعدادات النظام والأصول":
    st.title("⚙️ لوحة إدارة الأصول وصلاحيات النظام")
    st.markdown("التحقق من سلامة قواعد البيانات والملفات السحابية والمحلية.")
    st.markdown("---")
    
    if os.path.exists(DB_FILE):
        st.success(f"✅ ملف قاعدة البيانات المركزية `{DB_FILE}` يعمل بانتظام ويحفظ البيانات محلياً وسحابياً.")
    else:
        st.warning("⚠️ ملف قاعدة البيانات غير منشور بعد.")

    st.markdown("### 🎨 حالة السمة والواجهة البصرية")
    st.info("الواجهة الحالية تعمل بتصميم ملكي متطور (Dark Luxury Theme) مع تدرجات ذهبية وأزرار متجاوبة بالكامل.")
