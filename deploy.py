import pandas as pd 
import numpy as np 
import pickle 
import streamlit as st 
from PIL import Image 

pickle_in = open('/Users/oliverpan/Desktop/catboost.pkl', 'rb') 
classifier = pickle.load(pickle_in) 
  
def welcome(): 
    return 'welcome all'

def prediction(overall_qual, area, year_built):   
   
    prediction = classifier.predict( 
        [[overall_qual, area, year_built]]) 
    print(prediction) 
    return prediction 

def main(): 
    st.title("Prediction House Prices in Iowa") 
      
    html_temp = """ 
    <div style ="background-color:red;padding:13px"> 
    <h1 style ="color:black;text-align:center;">Streamlit App</h1> 
    </div> 
    """
      
    # this line allows us to display the front end aspects we have  
    # defined in the above code 
    st.markdown(html_temp, unsafe_allow_html = True) 
      
    # the following lines create text boxes in which the user can enter  
    # the data required to make the prediction 
    overall_qual = st.text_input("Overall Qual", "") 
    area = st.text_input("Area", "") 
    year_built = st.text_input("Year Built", "") 
    result ="" 
      
    # the below line ensures that when the button called 'Predict' is clicked,  
    # the prediction function defined above is called to make the prediction  
    # and store it in the variable result 
    if st.button("Predict"): 
        result = prediction(overall_qual, area, year_built) 
    st.success('The output is {}'.format(result)) 
     
if __name__=='__main__': 
    main() 