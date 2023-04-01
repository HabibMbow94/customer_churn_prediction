#Import libraries
import streamlit as st
import pandas as pd
import numpy as np
from PIL import Image

#load the model from disk
import joblib
model = joblib.load(r"./save_model/model.sav")

#Import python scripts
from preprocessing import preprocess

def main():
    #Setting Application title
    
    st.title('Application pour la prediction du churn client de la telecom.')
    
    st.markdown("**Le churn (Attrition)** exprime le taux de la perdition des clients pour une entreprise")

    # image = Image.open('images/target.png')
    # st.image(image) 
    # image = Image.open('images/newplot.png')
    # st.image(image) 
    
      #Setting Application description
    st.markdown("""
     L'objectif de l'application sur le churn est la detection des individus qui ont l'intention de quitter l'entreprise afin d'ameliorer la prise de decision
     et de mettre en place des action de retention". L'application est fonctionnelle pour la prédiction en ligne et la prédiction de données par Lots.
    """)
    st.markdown("<h3></h3>", unsafe_allow_html=True)

    #Setting Application sidebar default
    
    image = Image.open('App.jpg')
    add_selectbox = st.sidebar.selectbox(
	"Comment voulez-vous prédire?", ("En Ligne", "Par Lots"))
    st.sidebar.info('Cette application est créée pour prédire les taux de perte de clientèle.')
    st.sidebar.image(image)

    if add_selectbox == "En Ligne":
        #Based on our optimal features selection
        st.subheader("Données démographiques")
        seniorcitizen = st.selectbox('Senior Citizen:', ('Yes', 'No'))
        dependents = st.selectbox('Dépendent:', ('Yes', 'No'))


        st.subheader("Données de Paiement")
        tenure = st.slider('Nombre de mois pendant lesquels le client est resté dans l’entreprise', min_value=0, max_value=72, value=0)
        contract = st.selectbox('Contrat', ('Month-to-month', 'One year', 'Two year'))
        paperlessbilling = st.selectbox('Facturation Sans papier', ('Yes', 'No'))
        PaymentMethod = st.selectbox('Méthode Paiement',('Electronic check', 'Mailed check', 'Bank transfer (automatic)','Credit card (automatic)'))
        monthlycharges = st.number_input('Montant mensuel facturé au client', min_value=0, max_value=150, value=0)
        totalcharges = st.number_input('Le montant total facturé au client',min_value=0, max_value=10000, value=0)

        st.subheader("Services Souscrits")
        mutliplelines = st.selectbox("Est-ce que le client possède plusieurs lignes?",('Yes','No','No phone service'))
        phoneservice = st.selectbox('Service Téléphonique:', ('Yes', 'No'))
        internetservice = st.selectbox("Est-ce-que le client dispose d'un service internet", ('DSL', 'Fiber optic', 'No'))
        onlinesecurity = st.selectbox("Le client est-il protégé en ligne?",('Yes','No','No internet service'))
        onlinebackup = st.selectbox("Est-ce que le client a une sauvegarde en ligne?",('Yes','No','No internet service'))
        techsupport = st.selectbox("Le client dispose-t-il d'une assistance technologique?", ('Yes','No','No internet service'))
        streamingtv = st.selectbox("Le client dispose-t-il d'un stream TV", ('Yes','No','No internet service'))
        streamingmovies = st.selectbox("Le client dispose-t-il d'un stream movies", ('Yes','No','No internet service'))

        data = {
                'SeniorCitizen': seniorcitizen,
                'Dependents': dependents,
                'tenure':tenure,
                'PhoneService': phoneservice,
                'MultipleLines': mutliplelines,
                'InternetService': internetservice,
                'OnlineSecurity': onlinesecurity,
                'OnlineBackup': onlinebackup,
                'TechSupport': techsupport,
                'StreamingTV': streamingtv,
                'StreamingMovies': streamingmovies,
                'Contract': contract,
                'PaperlessBilling': paperlessbilling,
                'PaymentMethod':PaymentMethod, 
                'MonthlyCharges': monthlycharges, 
                'TotalCharges': totalcharges
                }
        features_df = pd.DataFrame.from_dict([data])
        st.markdown("<h3></h3>", unsafe_allow_html=True)
        st.write('Aperçu des données de prédiction')
        st.markdown("<h3></h3>", unsafe_allow_html=True)
        st.dataframe(features_df)


        #Preprocess inputs
        preprocess_df = preprocess(features_df, 'En Ligne')

        prediction = model.predict(preprocess_df)

        if st.button('Prédire'):
            if prediction == 1:
                st.warning('Yes, le client mettra fin au service')
            else:
                st.success('No, le client est satisfait des services.')
        

    else:
        st.subheader("Chargement de données")
        uploaded_file = st.file_uploader("Sélectionner un fichier")
        if uploaded_file is not None:
            data = pd.read_csv(uploaded_file)
            #Get overview of data
            st.write(data.head())
            st.markdown("<h3></h3>", unsafe_allow_html=True)
            #Preprocess inputs
            preprocess_df = preprocess(data, "Par Lots")
            if st.button('Prédiction'):
                #Get batch prediction
                prediction = model.predict(preprocess_df)
                prediction_df = pd.DataFrame(prediction, columns=["Prédictions"])
                prediction_df = prediction_df.replace({1:'Yes, le client mettra fin au service', 
                                                    0:'No, le client est satisfait des services.'})

                st.markdown("<h3></h3>", unsafe_allow_html=True)
                st.subheader('Prédiction')
                st.write(prediction_df)
            
if __name__ == '__main__':
        main()