#Basic libraries Package
import streamlit as st
import os
from PIL import Image
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import pickle
# import joblib

#################################################################
@st.cache

def load_data(dataset):
    data = pd.read_csv(dataset)
    return data

NewExist_label  = {'Yes':1, 'No':0}
RevLineCr_label = {'Yes':1, 'No':0}
State_label    = {'Alaska': 0.1,'Alabama': 0.2, 'Arkansas': 0.2, 'Arizona': 0.2,'California': 0.2, 'Colorado': 0.2, 'Connecticut': 0.1,
                   'District of Columbia': 0.2, 'Delaware': 0.2, 'Florida': 0.3, 'Georgia': 0.2, 'Hawaii': 0.2, 'Iowa': 0.1,
                   'Idaho': 0.1, 'Illinois': 0.2, 'Indiana': 0.2, 'Kansas': 0.1, 'Kentucky': 0.2, 'Louisiana': 0.2, 'Massachusetts': 0.1,
                   'Maryland': 0.2, 'Maine': 0.1, 'Michigan': 0.2, 'Minnesota': 0.1, 'Missouri': 0.2, 'Mississippi': 0.2, 'Montana': 0.1,
                   'North Carolina': 0.2, 'North Dakota': 0.1, 'Nebraska': 0.1, 'New Hampshire': 0.1, 'New Jersey': 0.2, 'New Mexico': 0.1,
                   'Nevada': 0.2, 'New York': 0.2, 'Ohio': 0.2, 'Oklahoma': 0.2, 'Oregon': 0.2, 'Pennsylvania': 0.1, 'Rhode Island': 0.1,
                   'South Carolina': 0.2, 'South Dakota': 0.1, 'Tennessee': 0.2, 'Texas': 0.2, 'Utah': 0.2, 'virginia': 0.2, 'Vermont': 0.1,
                   'Washington': 0.1, 'Wisconsin': 0.1, 'West Virginia': 0.2, 'Wyoming': 0.1}

Sector_label    = {'Agriculture, Forestry, Fishing & Hunting': 0.09, 'Mining, Quarying, Oil & Gas': 0.08,
                   'Utilities': 0.14, 'Constuction': 0.23, 'Manufacturing': 0.14, 'Manufacturing': 0.16, 'Manufacturing': 0.19,
                   'Wholesale Trade': 0.19, 'Retail Trade': 0.22, 'Retail Trade': 0.23, 'Transportation & Warehousing': 0.23,
                   'Transportation & Warehousing': 0.27, 'Information': 0.25, 'Finance & Insurance': 0.28, 
                   'Real Estate, Rental & Leasing': 0.29, 'Professional, Scientific & Technical Service': 0.19,
                   'Management of Companies & Enterprise': 0.10, 'Administrative, Support, Waste Management & Remediation Service': 0.24,
                   'Educational Service': 0.24, 'Health Care & Social Assistance': 0.10, 'Arts, Entertainment & Recreation': 0.21, 
                   'Accomodation & Food Service': 0.22, 'Other Servieces': 0.20, 'Public Administration':0.15}
Recession_label = {'Yes':1, 'No':0}
Retained_label  = {'Yes':1, 'No':0}

img = Image.open('loan_image.jpeg')

Context = """The objective about this project is to predict which loan will be default based on several parameters. Because I am not an expert in banking or finance domain, to prevent bias in choosing the threshold, I will change little bit about the result of this app from binary classification to percentage of posibilty default. With this simple app, the banker or guarantor will be more efficient to predict which application should be accepted or declined.

The dataset is from the U.S. Small Business Administration (SBA) The U.S. SBA was founded in 1953 on the principle of promoting and assisting small enterprises in the U.S. credit market (SBA Overview and History, US Small Business Administration (2015)). Small businesses have been a primary source of job creation in the United States; therefore, fostering small business formation and growth has social benefits by creating job opportunities and reducing unemployment. 

There have been many success stories of start-ups receiving SBA loan guarantees such as FedEx and Apple Computer. However, there have also been stories of small businesses or start-ups that have defaulted on their SBA guaranteed loans. \n Small business owners often seek out SBA (Small Business Association) loans because they guarantee part of the loan. Without going into too much detail, this basically means that the SBA will cover some of the losses should the business default on the loan, which lowers the risk involved for the business owner(s). This increases the risk to the SBA however, which can sometimes make it difficult to get accepted for one of their loan programs.

This project is end to end data science projcet (kinda), from Data Preparation, Modeling, Evaluating, Tunning until Deployment. If you want to see more detail about this project, click this link below:"""

Link = 'https://github.com/farrasalyafi/sba_loan_default_prediction'

Linkedin = 'https://www.linkedin.com/in/muhammad-farras/'

# Get the Keys
def get_value(val,my_dict):
    for key ,value in my_dict.items():
        if val == key:
            return value

# Find the Key From Dictionary
def get_key(val,my_dict):
    for key ,value in my_dict.items():
        if val == value:
            return key

#Main apps
def main():
    """Loan Deault Prediction"""
    st.title('Loan Default Prediction App')
    st.write('By: M. Farras Al-Yafi')
    
    #Menu
    menu = ['Prediction', 'About']
    choice = st.sidebar.selectbox('Select Activities', menu)
    
    if choice == 'Prediction':
        #data = load_data('SbaDataClean.csv')
        st.image(img, width=700)
        #Making Widget Input
        RevLineCr = st.radio('Is It Revolving Line of Credit?', tuple(RevLineCr_label.keys()))
        Term      = st.slider("How Long Is The Loan? (Month)", 0, 300 )
        Portion   = st.slider("How Much Portion SBA Guarantee?", 0.0,1.0)
        GrAppv    = st.slider("How Much Loan From The Bank? (10K)", 0.0, 15.)
        State     = st.selectbox('Where Is The Business Located?', tuple(State_label.keys()))
        DisGross  = st.slider("How Much The Amount Disbursed? (10k)",0.0, 15.0)
        Retained  = st.radio('Is The Employe Retained?', tuple(Retained_label.keys()))
        Sector    = st.selectbox('What Is The Business Sector?', tuple(Sector_label.keys()))
        Recession = st.radio('Is It Active When Recession?', tuple(Recession_label.keys()))
        NewExist  = st.radio('Is It New Business?', tuple(NewExist_label.keys()))
        
        #Encoding Input
        V_NewExist  = get_value(NewExist, NewExist_label)
        V_RevLineCr = get_value(RevLineCr, RevLineCr_label)
        V_State     = get_value(State, State_label)
        V_Sector    = get_value(Sector, Sector_label)
        V_Recession = get_value(Recession, Recession_label)
        V_Retained  = get_value(Retained, Retained_label)
        
        
        #Data That Will Use For Prediction
        input_data = [V_RevLineCr, Term, Portion, GrAppv, V_State, DisGross, V_Retained, V_Sector, V_Recession, V_NewExist]
        input_data = np.array(input_data).reshape(1, -1)
        #st.write(input_data)
        
        #Prediction
        if st.button("Predict!"):
            predictor = pickle.load(open("xgb_model.pkl", 'rb'))
            prediction = predictor.predict(input_data)
            predict_proba = predictor.predict_proba(input_data)[:,1]
            hasil = (str((np.around(float(predict_proba),3) * 100)) + '%')
                
            st.subheader('The Probability This Loan Will Be Default is: ' + hasil)
            
    
    if choice == 'About':
        st.header('About This Project')
        st.image(img, width=700)
        st.write(Context)
        st.write(Link)
        st.write("Let's Connect!")
        st.write(Linkedin)

    
if __name__ == '__main__':
    main()
