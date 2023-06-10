import os
import numpy as np
from keras.models import load_model
import streamlit as st
import cv2 as cv
from PIL import Image


categories = ['COVID Virus Detected', 'Normal Chest X-ray Scan', 'Pneumonia Virus Detected']
st.title('Virus Detection And Diagnosis Application')
st.text('upload the image')

uploaded_file = st.file_uploader('Choose an image...')

model = load_model('/home/user/Documents/PROJECT/Karare Project/CovidModel.h5')

if uploaded_file is not None:
    image = Image.open(uploaded_file)
    st.image(image, caption='uploaded image')

    if st.button('DETECT'):
        st.write('result...')
        image = np.array(image)
        image = cv.cvtColor(image, cv.COLOR_BGR2GRAY)
        image = cv.resize(image, (224, 224))
        image = np.expand_dims(image/255, axis=0)

        result = model.predict(image)
        result = np.argmax(result)
        result = int(result)
        prediction = categories[result]
        st.title('Patient has: ')
        st.title(prediction)
        if result == 0:
            st.write('COVID-19, also known as the novel coronavirus, is a highly contagious respiratory illness caused by the severe acute respiratory syndrome coronavirus 2 (SARS-CoV-2). It was first identified in December 2019 in Wuhan, China, and has since become a global pandemic.')
            st.title('Symptoms')
            st.write('Symptoms include:')
            st.write('1. Fever or chills.')
            st.write('2. Cough (usually dry)')
            st.write('3. Shortness of breath or difficulty breathing')
            st.write('4. Fatigue or tiredness')
            st.write('5. Muscle or body aches')
            st.write('6. Headache')
            st.write('7. Sore throat')
            st.write('8. Loss of taste or smell')
            st.write('9. Congestion or runny nose')
            st.write('10. Nausea or vomiting')
            st.write('11. Diarrhea')
            st.title('Prevention Methods')
            st.write('Prevention methods include:')
            st.write('1. Vaccination: Get vaccinated with a COVID-19 vaccine authorized by regulatory authorities.')
            st.write('2. Mask-wearing: Wear a mask that covers your nose and mouth in public settings, especially when social distancing is not possible.')
            st.write('3. Hand hygiene: Wash your hands frequently with soap and water for at least 20 seconds or use hand sanitizer containing at least 60% alcohol.')
            st.write('4. Social distancing: Maintain a distance of at least 6 feet (about 2 meters) from others who are not from your household.')
            st.write('5. Avoid close contact: Limit close contact with individuals showing symptoms or those who have been exposed to the virus.')
            st.write('6. Indoor ventilation: Ensure proper ventilation in enclosed spaces to reduce the risk of viral transmission.')
            st.write('7. Stay home when sick: If you experience any symptoms or have been in close contact with an infected person, stay at home, and seek medical advice.')
            st.title('Treatment Methods')
            st.write('Treatment for COVID-19 primarily focuses on managing symptoms and providing supportive care. Mild cases can often be treated at home with rest, fluids, and over-the-counter pain relievers to reduce fever and discomfort. However, severe cases may require hospitalization and more intensive medical interventions, such as oxygen therapy, antiviral medications, or treatments to support organ function. In some cases, individuals with severe illness may need mechanical ventilation or other forms of life support.Its important to consult healthcare professionals or follow guidelines provided by reputable health organizations for accurate and up-to-date information on COVID-19 symptoms, prevention, and treatment methods, as the understanding of the virus continues to evolve.')
        elif result ==1:
            st.title('Patient is healthy')
            st.write('Patient has no viral infaction and is in perfect health')
        elif result == 2:
            st.write('Pneumonia is an infection that causes inflammation in one or both lungs. It can be caused by various pathogens, including bacteria, viruses, and fungi. Pneumonia can range from mild to severe, and it can be particularly dangerous for older adults, young children, and individuals with weakened immune systems.')
            st.title('Symptoms')
            st.write('Symptoms include:')
            st.write('1. Cough: Pneumonia often presents with a persistent cough that may produce phlegm or mucus.')
            st.write('2. Fever: A high fever, often accompanied by sweating and chills, is a typical symptom.')
            st.write('3. Shortness of breath: Difficulty breathing or shortness of breath may occur, especially during physical activity.')
            st.write('4. Chest pain: Some individuals experience chest pain that worsens when breathing deeply or coughing.')
            st.write('5. Fatigue: Feeling excessively tired or experiencing a general sense of weakness can be symptoms of pneumonia.')
            st.write('6. Rapid breathing: Rapid and shallow breathing, also known as tachypnea, may occur.')
            st.write('7. Bluish coloration: In severe cases, lips and fingertips may turn bluish due to a lack of oxygen.')
            st.title('Prevention Methods')
            st.write('Prevention Methods include:')
            st.write('1. Vaccination: Immunization against common bacterial and viral causes of pneumonia, such as the pneumococcal vaccine and the influenza vaccine, can significantly reduce the risk.')
            st.write('2. Hand hygiene: Frequent handwashing with soap and water or using hand sanitizer helps prevent the spread of infectious pathogens.')
            st.write('3. Respiratory hygiene: Covering your mouth and nose with a tissue or your elbow when coughing or sneezing can prevent the release of respiratory droplets.')
            st.write('4. Avoid smoking: Smoking damages the lungs and weakens the immune system, making individuals more susceptible to respiratory infections like pneumonia.')
            st.write('5. Good ventilation: Ensuring proper ventilation in indoor spaces helps reduce the concentration of airborne pathogens.')
            st.write('6. Healthy lifestyle: Maintaining overall good health through regular exercise, a balanced diet, and adequate sleep can strengthen the immune system.')
            st.title('Treatment Methods')
            st.write('Treatment methods include:')
            st.write('1. Antibiotics: If the pneumonia is bacterial, antibiotics are prescribed to target and eliminate the specific bacteria causing the infection.')
            st.write('2. Antiviral medications: For viral pneumonia, antiviral drugs may be used to treat the underlying viral infection.')
            st.write('3. Antifungal medications: Fungal pneumonia requires treatment with antifungal medications.')
            st.write('4. Supportive care: Rest, hydration, and over-the-counter pain relievers can help manage symptoms. Severe cases may require hospitalization for additional treatments, such as oxygen therapy or intravenous fluids.')