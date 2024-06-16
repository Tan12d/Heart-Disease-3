import pickle
import streamlit as st
from streamlit_option_menu import option_menu
import pandas as pd
import plotly.express as px
import matplotlib.pyplot as plt
from pygwalker.api.streamlit import StreamlitRenderer
from streamlit_extras.stylable_container import stylable_container
from streamlit_extras.colored_header import colored_header
from streamlit_extras.chart_annotations import get_annotations_chart
import altair as alt
import numpy as np
from streamlit_extras.chart_container import chart_container
import time



st.set_page_config(
    page_title = "Multipage App",
    page_icon = "👋"
)

heart_disease_model = pickle.load(open('trained_model1.sav', 'rb'))

# sidebar for navigation
with st.sidebar:
    
    selected = option_menu('Heart Disease Prediction Using ML',
                          
                          ['📖 Heart Disease Calculator',
                           '📊 Visualization'],
                          icons=['heart','activity'],
                          default_index=0)
    
    st.sidebar.success("Select a page above.")
    

# Heart Disease Prediction Page
if (selected == '📖 Heart Disease Calculator'):
    
    # page title
    st.title('Heart Disease Prediction using ML')

    
    
    colored_header(
        label="Predictive System",
        description="Fill the details...",
        color_name="violet-70",
    )
    
    col1, col2, col3 = st.columns(3)
    
    with col1:
        age = st.number_input("Age", value=None, min_value=20, max_value=100, placeholder="Enter the age")
        
    with col2:
        sex = st.selectbox('Sex', (1,0), index=None, placeholder="Male:1 Female:0")
        
    with col3:
        cp = st.selectbox('Chest Pain types', ("0: Typical angina","1: Atypical angina","2: Non-anginal pain","3: Asymptomatic"), index=None)
        
    with col1:
        trestbps = st.number_input('Resting Blood Pressure', value=None, min_value=1, placeholder="Enter the value")
        
    with col2:
        chol = st.number_input('Serum Cholestoral in mg/dl', 
        value=None, min_value=1, placeholder="Enter the value")
        
    with col3:
        fbs = st.selectbox('Fasting Blood Sugar > 120 mg/dl', ("0: Normal Blood sugar level", "1: High Blood sugar level"), index=None)
        
    with col1:
        restecg = st.selectbox('Resting Electrocardiographic results', ("0: Normal", "1: Abnormal", "2: Significant"), index=None)
        
    with col2:
        thalach = st.number_input('Maximum Heart Rate achieved', value=None, min_value=1, placeholder="Enter the value")
        
    with col3:
        exang = st.selectbox('Exercise Induced Angina', ("0: Absent", "1: Present"), index=None)
        
    with col1:
        oldpeak = st.number_input('ST depression induced by exercise', min_value=0.0, placeholder="Enter the value")
        
    with col2:
        slope = st.selectbox('Slope of the peak exercise ST segment', ("0: Horizontal slope", "1: Unsloping slope", "2: Downsloping slope"), index=None)
        
    with col3:
        ca = st.selectbox('Major vessels colored by flourosopy', ("0: No major blood vessels", "1: One major blood vessels", "2: Two major blood vessels", "3: Three major blood vessels"), index=None)
        
    with col1:
        thal = st.selectbox('Thallium test', ("0: Normal", "1: Fixed defect", "2: Reversable defect"), index=None)
        
             
    _, col_2, _ = st.columns(3)

    with col_2:
        # code for Prediction
        heart_diagnosis = ''
        
        # creating a button for Prediction
        
        if st.button('Heart Disease Test Result'):

            if age is None or sex is None or cp is None or trestbps is None or chol is None or fbs is None or restecg is None or thalach is None or exang is None or oldpeak is None or slope is None or ca is None or thal is None:
                st.warning("Please fill all the details", icon="⚠️") 

            else:
                cp_numeric = int(cp.split(":")[0])

                fbs_numeric = int(fbs.split(":")[0])

                restecg_numeric = int(restecg.split(":")[0])

                exang_numeric = int(exang.split(":")[0])

                slope_numeric = int(slope.split(":")[0])

                ca_numeric = int(ca.split(":")[0])

                thal_numeric = int(thal.split(":")[0])

                heart_prediction = heart_disease_model.predict([[int(age), int(sex), cp_numeric, int(trestbps), int(chol), fbs_numeric, restecg_numeric, int(thalach), exang_numeric, float(oldpeak), slope_numeric, ca_numeric, thal_numeric]])    

                with st.spinner('Wait for it...'):
                    time.sleep(2)                     
            
                if (heart_prediction[0] == 1):
                    heart_diagnosis = 'The person is having heart disease'
                else:
                    heart_diagnosis = 'The person does not have any heart disease'
        
    st.success(heart_diagnosis)

    def get_data():
    # Create a DataFrame with the provided data
        data = pd.read_excel('data.xlsx')
        return data

    # Function to create Altair chart
    def get_chart(data):
        # Create an Altair scatter plot
        chart = alt.Chart(data).mark_point().encode(
            x='age',
            y='thalach',
            color='target:N'  # Color points by the target variable
        ).properties(
            width=600,
            height=400
        )
        return chart

    # Main code
    def main():
        # Get data
        data = get_data()

        # Get chart
        chart = get_chart(data)

        # Display the chart using Streamlit
        st.altair_chart(chart, use_container_width=True)

    if __name__ == "__main__":
        main()

    # chart_data = pd.read_excel('data.xlsx', usecols=['age', 'chol'])
    # st.area_chart(chart_data)

    chart_data = pd.read_excel('data.xlsx', usecols=['age', 'trestbps', 'thalach', 'chol', 'target'])
    with chart_container(chart_data):
        st.write("Here's a cool chart")
        st.area_chart(chart_data)

    
     

        
    
    
if (selected == "📊 Visualization"):
    
    st.title("Heart Disease")

    df = pd.read_csv("data.csv",sep=',' , names=['age','sex','cp','trestbps','chol','fbs','restecg','thalach','exang','oldpeak','slope','ca','thal','target'])

    df = df['age'].str.split(',', expand=True)

    df.columns = df.iloc[0]

    df = df.drop(0)

    df = df.reset_index(drop=True)

    df = df.sample(15)

    st.write(df)

    # Create a bar chart of ages
    st.write("## Age Distribution")
    age_chart = df['age'].value_counts().plot(kind='bar')
    plt.title('Age Distribution')
    plt.xlabel('Age')
    plt.ylabel('Count')
    st.pyplot(age_chart.figure)

    # Create a scatter plot of age vs cholesterol
    st.write("## Age vs Cholesterol")
    plt.figure()
    plt.scatter(df['age'], df['chol'], alpha=0.9)  # Adding transparency
    plt.title('Age vs Cholesterol')
    plt.xlabel('Age')
    plt.ylabel('Cholesterol')
    st.pyplot(plt.gcf(), clear_figure=True)

    # Create a histogram of maximum heart rate achieved
    st.write("## Maximum Heart Rate Achieved Distribution")
    plt.figure()
    plt.hist(df['thalach'], bins=10)
    plt.title('Maximum Heart Rate Achieved Distribution')
    plt.xlabel('Maximum Heart Rate Achieved')
    plt.ylabel('Frequency')
    st.pyplot(plt.gcf(), clear_figure=True) 


    st.write("## Distribution of Target")
    target_counts = df['target'].value_counts()
    labels = ['Healthy', 'Unhealthy']    
    plt.pie(target_counts, labels=labels, autopct='%1.1f%%')
    st.pyplot(plt.gcf())
