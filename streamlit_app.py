import streamlit as st
import pandas as pd

st.set_page_config(
    page_title="Medical Health Prediction Dashboard",
    page_icon="🩺",
)

st.title("🩺 لوحة التنبؤ بالمؤشرات الصحية والجلطات المتقدمة")
st.write("مرحباً بك في نظامك الطبي الذكي. يرجى إدخال بيانات المريض من القائمة الجانبية للحصول على التحليل الشامل والرسوم البيانية الفورية.")

st.sidebar.header("بيانات المريض الحيوية")

def user_input_features():
    age = st.sidebar.slider("العمر", 10, 100, 35)
    bmi = st.sidebar.slider("مؤشر كتلة الجسم (BMI)", 10.0, 50.0, 24.5)
    bp = st.sidebar.slider("ضغط الدم (Systolic)", 80, 200, 125)
    glucose = st.sidebar.slider("مستوى السكر في الدم", 70, 300, 110)
    cholesterol = st.sidebar.slider("مستوى الكوليسترول", 120, 300, 200)
    
    data = {
        'Age': age,
        'BMI': bmi,
        'Blood Pressure': bp,
        'Glucose': glucose,
        'Cholesterol': cholesterol
    }
    features = pd.DataFrame(data, index=[0])
    return features

df = user_input_features()

st.subheader("📊 ملخص المؤشرات المدخلة:")
st.dataframe(df)

if st.button("إجراء التحليل الشامل والتنبؤ"):
    risk_score = (df['BMI'][0] * 0.3) + (df['Blood Pressure'][0] * 0.25) + (df['Glucose'][0] * 0.2) + (df['Cholesterol'][0] * 0.15) + (df['Age'][0] * 0.1)
    
    st.subheader("نتائج التنبؤ والتحليل الطبي:")
    st.metric(label="مؤشر الخطر المحتمل", value=f"{risk_score:.1f}%")
    
    if risk_score > 65:
        st.error("⚠️ تحذير عالي المستوى: المؤشرات الحيوية تدل على احتمالية مرتفعة لوجود مخاطر صحية أو مؤشرات مبكرة للجلطات. يُنصح بمراجعة الطبيب المختص فوراً.")
    elif risk_score > 45:
        st.warning("⚠️ تنبيه متوسط: بعض المؤشرات مرتفعة قليلاً عن المعدل الطبيعي. يُفضل تنظيم الغذاء ومتابعة الفحص دورياً.")
    else:
        st.success("✅ المؤشرات مستقرة ضمن النطاق الطبيعي والأمور الصحية ممتازة ولا توجد مخاطر ظاهرة حالياً.")

    st.subheader("📈 رسم بياني توضيحي للمؤشرات:")
    chart_data = pd.DataFrame({
        'Indicator': ['BMI', 'Blood Pressure', 'Glucose', 'Cholesterol'],
        'Value': [df['BMI'][0], df['Blood Pressure'][0], df['Glucose'][0], df['Cholesterol'][0]]
    })
    st.bar_chart(chart_data.set_index('Indicator'))




