# -*- coding: utf-8 -*-
"""kassegneEtoudo_GRP521.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1TEu80kPe-a4IbyR8uGXzqnEpEKkQtbKl
"""

import pandas as pd

from google.colab import files
uploaded = files.upload()

df = pd.read_csv('fichierFinal_csv.txt')

print(df)

print("Taille du DataFrame :", df.shape)



#4) LA TAILLE DU DATAFRAME

print("Noms des colonnes :", df.columns)



#5)Le nom des colonnes du data frame

df['gender'].value_counts()




#6)Nombre de clients hommes et de clients femmes

df.columns = df.columns.str.upper()



# 7)Transformer les noms des colonnes en majuscules

df.head(7)
df.tail(3)
# 8) Affiche les 7 premieres lignes et 3 derniere lignes

df['TotalMonthlyCharges'] = df['MONTHLYCHARGES'] * df['TENURE']
print(df['TotalMonthlyCharges'])

# 9) Calcule la charge totale mensuelle facturée aux clients Et affiche la colonne

monthly_payment = df['MONTHLYCHARGES'].mean()
monthly_payment

# 10) Calculer la moyenne des paiements mensuels

payment_methods = df['PAYMENTMETHOD'].unique()
payment_methods

#11) Les différentes méthodes paiements qui existent

paper_billing_count = df[df['PAPERLESSBILLING'] == 'Non'].shape[0]
print("Nombre de clients utilisant la facturation papier:", paper_billing_count)

#12) Afficher le nombre de clients utilisant la facturation papier



streaming_movies_count = df[df['STREAMINGMOVIES'] == 'Yes'].shape[0]
print("Nombre de clients faisant du streaming de films :", streaming_movies_count)

#13) Afficher le nombre de clients faisant du streaming de films

total_annual_revenue = (df['MONTHLYCHARGES'] * df['TENURE']).sum()
print("Chiffre d'affaires annuel de la compagnie :", total_annual_revenue)

#14) Afficher le chiffre d'affaires annuel

filtered_customers = df[(df['MULTIPLELINES'] == 'Yes') & (df['STREAMINGMOVIES'] == 'Yes') & (df['CONTRACT'] == 'Two year')]
print("Noms des clients qui ont plusieurs lignes téléphoniques, font du streaming et ont un contrat de deux ans :")
print(filtered_customers['CUSTOMERID'])



#15) Afficher les noms des clients qui répondent aux critères

import matplotlib.pyplot as plt

plt.figure(figsize=(10, 6))
plt.hist(df['TotalMonthlyCharges'], bins=20, color='skyblue', edgecolor='black')
plt.title("Histogramme de la charge totale mensuelle")
plt.xlabel("Charge totale mensuelle")
plt.ylabel("Nombre de clients")
plt.grid(True)
plt.show()
#16) Tracer l'histogramme de la charge totale mensuelle
