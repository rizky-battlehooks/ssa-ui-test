import streamlit as st
import requests
import json

st.markdown("""
# SSA Algorithm Testing

This application is designed to test the SSA Office Finding Algorithm. This will not affect production that will be deployed by Horea as this runs in separate VPS.

## Data Fields

Each input object should contain the following fields:

- **zipcode**: String (format: 5 digit zipcode)
- **area_code**: String (example `254`)
- **timestamp** : (Optional) String (format: mm/dd/YYYY HH:MM:SS)

""")

url = 'http://62.72.5.242:5000/predict-phone-ssa'

st.title('SSA Office Prediction')

with st.form(key='input_form') :
    col1, col2 = st.columns(2)

    with col1 :
        area_code = st.text_input('Area Code :', placeholder="208")
    
    with col2 :
        zipcode = st.text_input('Zip Code :', placeholder="60216")
    
    timestamp = st.text_input('Datetime in PT (mm/dd/yyyy HH\:MM\:SS) :', placeholder='06/23/2024 14:00:05')
    btn_submit = st.form_submit_button(label = 'Submit')

if btn_submit :
    payload = {
        "area_code" : str(area_code),
        "zipcode" : str(zipcode),
        "timestamp" : str(timestamp)
    }

    response = requests.post(url=url, headers={'content-type' : 'application/json'}, json=payload)
    response_json = response.json()

    if response_json['Response Code'] == '200' :
        st.write(f'SSA Office Number : {response_json["SSA Number"]}')
        st.write(f'SSA Timezone : {response_json["SSA Timezone"]}')
        st.write(f'SSA State : {response_json["SSA State"]}')
        st.write(f'SSA City : {response_json["SSA City"]}')
        st.write(f'SSA Zip Code : {response_json["SSA Zipcode"]}')
    else :
        st.write('Cannot find Lead/SSA Office')
        st.write(f'Detailed Error : {response_json["Message"]}')