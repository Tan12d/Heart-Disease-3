import pandas as pd
import plotly.express as px
import streamlit as st
from streamlit_extras.stylable_container import stylable_container
from streamlit_extras.dataframe_explorer import dataframe_explorer
from streamlit_extras.switch_page_button import switch_page

st.set_page_config(page_title="Streamlit Visualization", 
                   page_icon="::")

df = pd.read_excel(
    io='data.xlsx',
    engine='openpyxl'    
)



st.title(":bar_chart: Heart Disease Dashboard")

total_number_of_patients = len(df)
no_of_male_patients = df['sex'].value_counts().get(1,0)
no_of_female_patients = df['sex'].value_counts().get(0,0)

left_col, middle_col, right_col = st.columns(3)
with left_col:
    st.subheader("Total no. of patients:")
    st.subheader(total_number_of_patients)
with middle_col:
    st.subheader("No. of Male patients:")
    st.subheader(f"{no_of_female_patients}")
with right_col:
    st.subheader("No. of female patients:")
    st.subheader(f"{no_of_male_patients}")


with stylable_container(
    key="container_with_border",
    css_styles=[
        """
        {    
            
            # left:12vw;
        }
        """,
        """
        .stDataFrame {

        }
        """,
    ],
):
    dataframe = pd.read_excel('data.xlsx')

        # Perform data exploration/filtering
    filtered_df = dataframe_explorer(dataframe)

        # Display the filtered DataFrame using Streamlit
    st.dataframe(filtered_df, use_container_width=True)

st.sidebar.header("Please Filter Here: ");
top_5_ages = df['age'].value_counts().head(5).index.tolist()
age = st.sidebar.multiselect(
    "Select the preffered age:",
    options=top_5_ages,
    default=top_5_ages
)

sex = st.sidebar.multiselect(
    "Select the sex:  \n0 👩‍💼 \n1 👨‍💼",
    options=df['sex'].unique(),
    default=df['sex'].unique()
)

target = st.sidebar.multiselect(
    "Choose target variable to display in chart: \n\n0 🤒 \n1 🫀",
    options=df['target'].unique(),
    default=df['target'].unique()
)

df_selection = df.query(
    "age == @age & sex == @sex & target == @target"
)

# st.dataframe(df_selection)

# st.title(":bar_chart: Heart Disease Dashboard")
st.markdown("##")

# total_number_of_patients = len(df)
# no_of_male_patients = df['sex'].value_counts().get(1,0)
# no_of_female_patients = df['sex'].value_counts().get(0,0)
average_age = round(df['age'].mean(),2)
average_blood_pressure = round(df['trestbps'].mean(),2)
average_blood_sugar = round(df['fbs'].mean(),2)
average_heart_rate = round(df['thalach'].mean(),2)

# left_col, middle_col, right_col = st.columns(3)
# with left_col:
#     st.subheader("Total no. of patients:")
#     st.subheader(total_number_of_patients)
# with middle_col:
#     st.subheader("No. of Male patients:")
#     st.subheader(f"{no_of_female_patients}")
# with right_col:
#     st.subheader("No. of female patients:")
#     st.subheader(f"{no_of_male_patients}")

st.markdown("---")

col1, col2, col3= st.columns(3)
# with col1:
#     st.markdown(f"### Average Age: {average_age} ###")
#     # st.subheader(f"{average_age}")

with col1:
    st.markdown(f"### Average Blood Pressure: {average_blood_pressure} ###")
    # st.subheader(f"{average_blood_pressure}")

with col2:
    st.markdown(f"### Average Blood Sugar: {average_blood_sugar} ###")
    # st.subheader(f"{average_blood_sugar}")

with col3:
    st.markdown(f"### Average Heart Rate: {average_heart_rate} ###")
    # st.subheader(f"{average_heart_rate}")

# st.balloons()
# st.camera_input("Take a pic")
# st.snow()
# st.toast('Your edited image was saved!', icon='😍')

# with st.spinner('Wait for it...'):
#     time.sleep(5)
# st.success('Done!')


# ---

count_targets_by_age = df_selection.groupby(["age", "target"]).size().reset_index(name="count")


# Now, create the bar chart
with stylable_container(
    key="container",
    css_styles=[
        """
        {
            # left:17vw;
        }
        """,
    ],
):
    fig_age_target = px.bar(
    count_targets_by_age,
    x="age",
    y="count",
    color="target",  # Color by the target value (0 or 1)
    title="<b>Age vs Count of Targets</b>",
    barmode="group",  # Group bars by age
    template="plotly_white"
    )

    st.plotly_chart(fig_age_target)



# -----


average_cholesterol_by_sex = df_selection.groupby("sex")["chol"].mean().reset_index()

# Map sex values to meaningful labels

with stylable_container(
    key="container1",
    css_styles=[
        """
        {
            # left:17vw;
        }
        """,
    ],
):
    average_cholesterol_by_sex["sex"] = average_cholesterol_by_sex["sex"].map({0: "Female", 1: "Male"})

# Now, create the bar chart

with stylable_container(
    key="container2",
    css_styles=[
        """
        {
            # left:17vw;
        }
        """,
        
    ],
):
    fig_sex_cholesterol = px.bar(
    average_cholesterol_by_sex,
    x="sex",
    y="chol",
    title="<b>Sex vs Average Cholesterol</b>",
    color="sex",  # Color by sex
    color_continuous_scale="Rainbow",
    template="plotly_white"
    )

    st.plotly_chart(fig_sex_cholesterol)

# -----

with stylable_container(
    key="container3",
    css_styles=[
        """
        {
            # left:17vw;
        }
        """,
        """
        .stDataFrame {

        }
        """,
    ],
):

    fig = px.scatter(df, x="age", y="chol", color="sex", title="Scatter plot of Age vs Cholesterol by Sex")
    st.plotly_chart(fig)



corr_matrix = df.corr()

with stylable_container(
    key="container4",
    css_styles=[
        """
        {
            # left:10vw;
        }
        """,
        """
        .stDataFrame {

        }
        """,
    ],
):

    fig = px.imshow(df.corr(), title='Correlation Heatmap', color_continuous_scale='Inferno')
    fig.update_layout(width=800, height=600)
    st.plotly_chart(fig)

_, col2, _ = st.columns(3)

with col2:
    if st.button("Back to Home 🏠"):
        switch_page("Homepage")