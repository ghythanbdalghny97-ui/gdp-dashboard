import streamlit as st
import pandas as pd

st.set_page_config(
    page_title="لوحة التنبؤ الطبي والصحي",
    page_icon="🩺",
)

st.title("🩺 لوحة التنبؤ بالمؤشرات الصحية والجلطات")
st.write("مرحباً بك في نظامك الطبي الذكي. يرجى إدخال بيانات المريض أدناه للحصول على التحليل والتنبؤ الفوري.")

st.sidebar.header("بيانات المريض الحيوية")

def user_input_features():
    age = st.sidebar.slider("العمر", 10, 100, 30)
    bmi = st.sidebar.slider("مؤشر كتلة الجسم (BMI)", 10.0, 50.0, 22.0)
    bp = st.sidebar.slider("ضغط الدم (Systolic)", 80, 200, 120)
    glucose = st.sidebar.slider("مستوى السكر في الدم", 70, 300, 100)
    
    data = {
        'Age': age,
        'BMI': bmi,
        'Blood Pressure': bp,
        'Glucose': glucose
    }
    features = pd.DataFrame(data, index=[0])
    return features

df = user_input_features()

st.sub("البيانات المدخلة للمريض:")
st.write(df)

if st.button("إجراء التحليل والتنبؤ"):
    # نموذج تجريبي مبدئي للتنبؤ بناءً على المؤشرات
    risk_score = (df['BMI'][0] * 0.4) + (df['Blood Pressure'][0] * 0.2) + (df['Glucose'][0] * 0.1)
    
    st.sub("نتائج التحليل:")
    if risk_score > 60:
        st.error("⚠️ تحذير: المؤشرات تشير إلى احتمالية عالية وجود خطورة أو مؤشرات مبكرة للجلطات. يُنصح بمراجعة الطبيب المختص فوراً.")
    else:
        st.success("✅ المؤشرات مستقرة ضمن النطاق الطبيعي ولا توجد مخاطر ظاهرة حالياً.")

