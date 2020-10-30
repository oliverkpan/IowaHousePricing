import pandas as pd 
import numpy as np 
import pickle 
import streamlit as st 
from PIL import Image 

pickle_in = open('/Users/oliverpan/Desktop/catboost_updated3.pkl', 'rb') 
classifier = pickle.load(pickle_in) 
  
def welcome(): 
    return 'welcome all'

def prediction(overall_qual, lot_area, garage_yr, garage_cars, bsmt_qual, sale_condition):   
   
    prediction = classifier.predict( 
        [[overall_qual, lot_area, garage_yr, garage_cars, bsmt_qual, sale_condition]]) 
    print(prediction) 
    return prediction 

def main(): 
    st.title("Predicting House Prices in Iowa") 
      
    html_temp = """ 
    <div style ="background-color:green;padding:13px"> 
    <h1 style ="color:black;text-align:center;">Iowatch</h1> 
    </div> 
    """
      
    # this line allows us to display the front end aspects we have  
    # defined in the above code 
    st.markdown(html_temp, unsafe_allow_html = True) 
      
    # the following lines create text boxes in which the user can enter  
    # the data required to make the prediction 
    overall_qual = st.slider('Overall Qual', min_value = 0, max_value = 10, key = '1')
    bsmt_qual = st.slider('Basement Quality', min_value = 0, max_value = 10, key = '2')
    sale_condition = st.slider('Sale Quality', min_value = 0, max_value = 10, key = '3')
    lot_area = st.text_input("Lot Area", "") 
    garage_yr = st.text_input("Year Built", "")
    garage_cars = st.selectbox('Number of Garages', options = ['1','2','3','4'])
    result = "" 
      
    # the below line ensures that when the button called 'Predict' is clicked,  
    # the prediction function defined above is called to make the prediction  
    # and store it in the variable result 
    if st.button("Predict"): 
        result = prediction(overall_qual, lot_area, garage_yr, garage_cars, bsmt_qual, sale_condition) 
    st.success('The predicted house price is {}'.format(result)) 
     
if __name__=='__main__': 
    main() 