# Prediction du taux de churn des clients

Le taux de churn est un indicateur efficace pour les entreprises qui proposent des abonnements. L'identification des clients qui ne sont pas satisfaits des solutions fournies permet aux entreprises de connaître les points faibles des produits ou des plans tarifaires, les problèmes de fonctionnement, ainsi que les préférences et les attentes des clients, afin de réduire de manière proactive les motifs de désabonnement.


Conception d'un flux de travail de prédiction du churn. La portée globale de la construction d'une application basée sur la ML pour prévoir le churn des clients est générique à la structure de projet ML standardisée qui comprend les étapes suivantes :

1. Définir le problème et l'objectif : il est essentiel de comprendre les informations que l'on doit tirer de l'analyse et de la prédiction. Comprendre le problème et recueillir les exigences des parties prenantes en ce qui concerne leurs points faibles et leurs attentes.

2. Établir la source des données : Ensuite, la spécification des sources de données est nécessaire pour l'étape suivante de la modélisation. Les systèmes de gestion de la relation client (CRM), les services d'analyse et le retour d'information des clients sont des sources courantes de données sur le taux de désabonnement.

3. Préparation, exploration et prétraitement des données : Les données historiques brutes sélectionnées pour résoudre le problème et construire des modèles prédictifs doivent être transformées dans un format adapté aux algorithmes d'apprentissage automatique. Cette étape peut également contribuer à l'amélioration des résultats globaux grâce à l'augmentation de la qualité des données.

4. Modélisation et essais : Cette étape couvre le développement et la validation des performances des modèles de prédiction du désabonnement des clients à l'aide de divers algorithmes d'apprentissage automatique.

5. Déploiement et surveillance : Il s'agit de la dernière étape du cycle de vie du développement de l'apprentissage automatique pour les prévisions de taux de désabonnement. C'est à ce stade que le modèle le plus approprié est mis en production. Il peut être intégré dans un logiciel existant ou devenir le noyau d'une nouvelle application.




# Activation de l'Environment virtuel

* Installation de l'environnement

Install pipenv
!pip3 install pipenv  

* Create a new Pipenv environment in that folder and activate that environment
 pipenv shell

* Install Streamlit in pipenv
pipenv install streamlit

Install joblib in pipenv
* pipenv install joblib 

# Run APP

* streamlit run App.py



L'application à déployer fonctionnera par le biais de cas d'utilisation opérationnels : Prédiction en ligne : Ce cas d'utilisation génère des prédictions une par une pour chaque point de données (dans le contexte de cet article, un client). Prédiction par lots : Ce cas d'utilisation permet de générer des prédictions pour un ensemble d'observations de manière instantanée.


<videao scr = "streamlit_app.mp4" />

