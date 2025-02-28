import streamlit as st
import pandas as pd 
import datetime

titanic_link = 'https://raw.githubusercontent.com/mwaskom/seaborn-data/master/titanic.csv'
titanic_data = pd.read_csv(titanic_link)

# Create the title for the web app
st.title("Titanic App")
# Creamos sidebar
sidebar = st.sidebar
# Agregamos title y texto en sidebar
sidebar.title("This is the sidebar.")
sidebar.write("You can add any elements to the sidebar.")

# ask user the current date
today = datetime.date.today()
today_date = sidebar.date_input('Cual es tu cumple : ', today)
#st.success('tu cumple es : `%s` felicidades ...' % (today_date))
st.success(f'tu cumple es: {today_date} felicidades...') 

# Display the content of the dataset if checkbox is true
st.header("Titanic Dataset")

agree = sidebar.checkbox("show DataSet Overview ? ")
if agree:
  st.dataframe(titanic_data)

st.header("Class Description")
selected_class = sidebar.radio("Select Class", titanic_data['class'].unique())

#st.write("Selected Class:", selected_class)
st.success(f'Selected Class: {selected_class}') 

st.markdown("___")

selected_sex = sidebar.selectbox("Select Sex", titanic_data['sex'].unique())
#st.write(f"Selected sex: {selected_sex}")
st.success(f'Selected sex: {selected_sex}') 

st.markdown("___")

optionals = sidebar.expander("Optional Configurations", True)

fare_select = optionals.slider( 
  "Select the Fare",
  min_value = float(titanic_data['fare'].min()),
  max_value = float(titanic_data['fare'].max())
)

subset_fare = titanic_data[(titanic_data['fare'] >= fare_select)]

st.write(f"Number of Records With this Fare {fare_select}: {subset_fare.shape[0]}")
st.dataframe(subset_fare)

st.markdown("___")