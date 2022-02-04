import streamlit as st
import plotly.express as px
import plotly.graph_objects as go
import pandas as pd
import numpy as np
import io

st.title('Acquisition clients')

# Datasets
df1 = pd.read_csv("./assets/Abandoned_Baskets.csv")
df2 = pd.read_csv('./assets/Cancelled_Shop_Orders.csv')
df3 = pd.read_csv('./assets/Customer_Service_Interactions.csv')
df4 = pd.read_csv('./assets/Gross_Adds.csv')
df5 = pd.read_csv('./assets/Payment_Responsibles.csv', sep=';')

st.markdown("Pour effectuer ce projet nous disposons de 5 datasets :")
# Table de description des fichiers
data_files_description = {
     'Nom fichier':
          ['Abandoned_Baskets.csv',
           'Cancelled_Shop_Orders.csv',
           'Customer_Service_Interactions.csv',
           'Gross_Adds.csv',
           'Payment_Responsibles.csv'
           ],
     'Description':
          ['Listing des paniers de produits abandonnés en ligne (site web)',
           'Listing des commandes annulées en boutique physique',
           'Listing des appels auprès du Service Client',
           'Listing des nouveaux contrats mobiles',
           'Listing des factures clients'
           ],
     'Période concernée (début)':
     [
          '25/10/2021',
          '01/01/2021',
          '01/10/2021',
          '25/11/2021',
          '-'
     ],
     'Période concernée (fin)':
     [
          '22/12/2021',
          '08/07/2021',
          '30/11/2021',
          '21/12/2021',
          '-'
     ]
}
table_files_description = pd.DataFrame(data_files_description, index =[np.arange(1,6)])
st.table(table_files_description)



############################################################################################
############################### DF1 Abandoned_Baskets.csv ##################################
############################################################################################
st.header("#1 Abandoned_Baskets.csv")
code = '''
# Lecture des données
df1 = pd.read_csv('Abandoned_Baskets.csv')
df1.head()
'''
st.code(code, language='python')
st.dataframe(df1.head())

# df1.shape
code = '''
# On vérifie la taille de notre dataset
df1.shape
'''
st.code(code, language='python')
st.write(df1.shape)

# df1.info()
code = '''
# On vérifie les infos de notre dataset
df1.info()
'''
st.code(code, language='python')
buffer = io.StringIO()
df1.info(buf=buffer)
s = buffer.getvalue()
st.text(s)

# df1.isna().sum()
code = '''
# On vérifie si on a des valeurs manquantes
df1.isna().sum()
'''
st.code(code, language='python')
st.write(df1.isna().sum())
st.markdown("Nous n'avons aucune valeur manquante.")

code = '''
# Lecture du dictionnaire
f_abandoned_baskets = open("./assets/Dictionnaire-Abandoned_Baskets.txt", "r")
'''
st.code(code, language='python')
f_abandoned_baskets = open("./assets/Dictionnaire-Abandoned_Baskets.txt", "r")
st.text(f_abandoned_baskets.read())

# df1 --> ANALYSE DE DF1 EN L'ETAT
st.subheader("Ajustements à apporter au dataset")
code = '''
# Suppression des colonnes inutiles pour l'analyse
df1.drop(['status', 'reason', 'direction', 'channel_id', 'channel_name', 'relatedparty_referredtype', 'relatedparty_role', 'interactionitem_id', 'interactionitem_type', 'interactiondate_enddatetime', 'receptiontimestamp'], axis=1, inplace=True)
# Reformattage de interaction_startdatetime
df1['interactiondate_startdatetime'] = pd.to_datetime(df1['interactiondate_startdatetime']).dt.date
# Renommage des colonnes
df1.rename(columns={'interactiondate_startdatetime': 'date_action', 'interactionitem_reason': 'item'}, inplace=True)
'''
st.code(code, language='python')
df1['interactiondate_startdatetime'] = pd.to_datetime(df1['interactiondate_startdatetime']).dt.date
df1.drop(['status', 'reason', 'direction', 'channel_id', 'channel_name', 'relatedparty_referredtype', 'relatedparty_role', 'interactionitem_id', 'interactionitem_type', 'interactiondate_enddatetime', 'receptiontimestamp'], axis=1, inplace=True)
df1.rename(columns={'interactiondate_startdatetime': 'date_action', 'interactionitem_reason': 'item'}, inplace=True)

code = '''
# Lecture du jeu de données à jour
df1.head()
'''
st.code(code, language='python')
st.dataframe(df1.head())

# df1 --> VISUALISATION DES DONNEES
st.subheader("Visualisation des données")
st.markdown("Nous avons peu d'informations à notre disposition pour analyser le dataset des paniers abandonnés. Nous pouvons néanmoins lister les produits et la part d'abandon qu'ils représentent par rapport au total des abandons."
            " Etant donné la quantité de produits différents (88) il est préférable de visualiser cela dans une table.")

code = '''
# On crée un dataframe avec le nombre d'occurences de chaque élément unique issu de la colonne item 
df1_products = df1.item.value_counts().rename_axis('item').reset_index(name='counts')
# On ajoute une colonne % pour savoir quelle part cela représente par rapport au total des abandons
df1_products["percent"] = round(df1_products.counts*100/df1_products.counts.sum(), 3).astype(str) + ' %'
])
'''
st.code(code, language='python')

df1_products = df1.item.value_counts().rename_axis('item').reset_index(name='counts')
df1_products["percent"] = round(df1_products.counts*100/df1_products.counts.sum(), 3).astype(str) + ' %'
fig = go.Figure(data=[go.Table(
    header=dict(values=list(df1_products.columns), font=dict(size=16), height=50),
    cells=dict(values=[df1_products.item, df1_products.counts, df1_products.percent], font=dict(size=14), height=30))
])
st.plotly_chart(fig, use_container_width=False, sharing="streamlit")
st.markdown("La plupart des abandons concerne des Smartphones de grandes marques (Samsung, Apple notamment).")



############################################################################################
############################### DF2 Cancelled_Shop_Orders.csv ##############################
############################################################################################
st.header("#2 Cancelled_Shop_Orders.csv")
code = '''
# Lecture des données
df2 = pd.read_csv('Cancelled_Shop_Orders.csv')
df2.head()
'''
st.code(code, language='python')
st.dataframe(df2.head())

# df2.shape
code = '''
# On vérifie la taille de notre dataset
df2.shape
'''
st.code(code, language='python')
st.write(df1.shape)

# df2.info()
code = '''
# On vérifie les infos de notre dataset
df2.info()
'''
st.code(code, language='python')
buffer = io.StringIO()
df2.info(buf=buffer)
s = buffer.getvalue()
st.text(s)

# df2.isna().sum()
code = '''
# On vérifie si on a des valeurs manquantes
df2.isna().sum()
'''
st.code(code, language='python')
st.write(df2.isna().sum())

code = '''
# Lecture du dictionnaire
f_cancelled_shop_orders = open("./assets/Dictionnaire-Cancelled_Shop_Orders.txt", "r")
'''
st.code(code, language='python')
f_cancelled_shop_orders = open("./assets/Dictionnaire-Cancelled_Shop_Orders.txt", "r")
st.text(f_cancelled_shop_orders.read())

# df2 --> ANALYSE DE DF2 EN L'ETAT
st.subheader("Ajustements à apporter au dataset")
code = '''
# Formatage des colonnes contenant des dates au bon format
df2['cancelled_cs_order_date'] = pd.to_datetime(df2['cancelled_cs_order_date']).dt.date
df2['cancelled_cs_order_date_add_2_weeks'] = pd.to_datetime(df2['cancelled_cs_order_date_add_2_weeks']).dt.date
df2['web_order_date'] = pd.to_datetime(df2['web_order_date']).dt.date
# Remplissage des valeurs null
df2['tariff_model'] = df2['tariff_model'].fillna('Unknown')
df2['tariff_plan'] = df2['tariff_plan'].fillna('Unknown')
df2['web_order_date'] = df2['web_order_date'].fillna(0)
'''
st.code(code, language='python')
# Formatage des colonnes contenant des dates au bon format
df2['cancelled_cs_order_date'] = pd.to_datetime(df2['cancelled_cs_order_date']).dt.date
df2['cancelled_cs_order_date_add_2_weeks'] = pd.to_datetime(df2['cancelled_cs_order_date_add_2_weeks']).dt.date
df2['web_order_date'] = pd.to_datetime(df2['web_order_date']).dt.date
# Remplissage des valeurs null
df2['tariff_model'] = df2['tariff_model'].fillna('Unknown')
df2['tariff_plan'] = df2['tariff_plan'].fillna('Unknown')
df2['web_order_date'] = df2['web_order_date'].fillna(0)
code = '''
# Lecture du jeu de données à jour
df2.head()
'''
st.code(code, language='python')
st.dataframe(df2.head())
st.markdown("La colonne _web_order_date_ comporte peu de dates renseignées (seulement 1.6 %), elle sera difficilement exploitable.")

# df2 --> VISUALISATION DES DONNEES
st.subheader("Visualisation des données")

code = '''
# Clients Orange
df2_yes = df2.loc[df2['orange_customer'] == 'YES']
# Clients pas Orange
df2_no = df2.loc[df2['orange_customer'] == 'NO']
# On récupère le nombre d'occurences pour chaque date unique
cancelled_orders_isOrange = df2_yes.cancelled_cs_order_date.value_counts().sort_index()
cancelled_orders_isNotOrange = df2_no.cancelled_cs_order_date.value_counts().sort_index()
'''
st.code(code, language='python')
df2_yes = df2.loc[df2['orange_customer'] == 'YES']
df2_no = df2.loc[df2['orange_customer'] == 'NO']
cancelled_orders_isOrange = df2_yes.cancelled_cs_order_date.value_counts().sort_index()
cancelled_orders_isNotOrange = df2_no.cancelled_cs_order_date.value_counts().sort_index()

fig = go.Figure()
fig.add_trace(go.Scatter(x=cancelled_orders_isOrange.index, y=cancelled_orders_isOrange.values,
                    mode='lines',
                    name='Client Orange = YES'))
fig.add_trace(go.Scatter(x=cancelled_orders_isNotOrange.index, y=cancelled_orders_isNotOrange.values,
                    mode='lines',
                    name='Client Orange = NO'))
fig.update_layout(title='Répartition du nombre de forfaits annulés en boutique entre le 01/01/2021 et le 08/07/2021')
st.plotly_chart(fig, use_container_width=False, sharing="streamlit")

st.markdown("Que les clients soient chez Orange ou non on constate les mêmes tendances : des pics d'annulation en semaine et des creux correspondants aux Dimanches. On voit une grosse période d'annulation en tout début d'année, le **Lundi 4 Janvier**, immédiatement après les fêtes de fin d'année."
            " Entre mi-Janvier et mi-Mai le nombre d'annulations est plutôt constant puis on observe une baisse à partir de Juin jusqu'à la fin de la période analysée.")

code = '''
# Nombre moyen d'annulations par jour concernant le segment de clients Orange
mean_isClient = round(cancelled_orders_isOrange.values.mean())
# Nombre moyen d'annulations par jour concernant le segment de clients NON Orange
mean_isNotClient = round(cancelled_orders_isNotOrange.values.mean())
'''
st.code(code, language='python')
st.write('mean_isClient = ', round(cancelled_orders_isOrange.values.mean()))
st.write('mean_isNotClient =', round(cancelled_orders_isNotOrange.values.mean()))
st.markdown("On a en moyenne **229** annulations de forfaits par jour pour les clients déjà Orange et **112** pour les non-clients.")



############################################################################################
############################### DF3 Customer_Service_Interactions.csv ######################
############################################################################################
st.header("#3 Customer_Service_Interactions.csv")
st.markdown("Appels traités par le Service Client entre le 01/10/2021 et le 30/11/2021.")
code = '''
# Lecture des données
df3 = pd.read_csv('Customer_Service_Interactions.csv')
df3.head()
'''
st.code(code, language='python')
st.dataframe(df3.head())

# df3.shape
code = '''
# On vérifie la taille de notre dataset
df3.shape
'''
st.code(code, language='python')
st.write(df3.shape)

# df3.info()
code = '''
# On vérifie les infos de notre dataset
df3.info()
'''
st.code(code, language='python')
buffer = io.StringIO()
df3.info(buf=buffer)
s = buffer.getvalue()
st.text(s)

# df3.isna().sum()
code = '''
# On vérifie si on a des valeurs manquantes
df3.isna().sum()
'''
st.code(code, language='python')
st.write(df3.isna().sum())
code = '''
# La colonne za_rootcause_dtl contient des valeurs manquantes, nous allons donc les remplir
df3['za_rootcause_dtl'] = df3['za_rootcause_dtl'].fillna('Unknown')
'''
st.code(code, language='python')
df3['za_rootcause_dtl'] = df3['za_rootcause_dtl'].fillna('Unknown')

code = '''
# Lecture du dictionnaire
f_customer_service = open("./assets/Dictionnaire-Customer_Service_Interactions.txt", "r")
'''
st.code(code, language='python')
f_customer_service = open("./assets/Dictionnaire-Customer_Service_Interactions.txt", "r")
st.text(f_customer_service.read())

# ANALYSE DE DF3 EN L'ETAT
st.subheader("Ajustements à apporter au dataset")
st.markdown("Les champs **_month_nr_** et **_creation_date_nr_** sont au format numérique (int64).")
st.markdown("Nous allons formater **_creation_date_nr_** en datetime et supprimer la colonne **_month_nr_** qui est superflu.")
st.markdown("A partir de **_creation_date_nr_** nous allons créer 5 colonnes qui nous aiderons à effectuer une analyse plus simple et plus agréable par la suite :")
st.markdown("- year")
st.markdown("- month")
st.markdown("- day")
st.markdown("- name_month")
st.markdown("- name_day")
st.markdown("Aussi, nous allons renommer les champs **_level2_**, **_level3_** et **_za_rootcause_dtl_** pour un peu plus de clarté.")

code = '''
# Reformattage de creation_date_nr
df3['creation_date_nr'] =  pd.to_datetime(df3['creation_date_nr'], format='%Y%m%d')
# Création des champs year, month et day
df3[["year", "month", "day"]] = df3["creation_date_nr"].astype(str).str.split("-", expand = True)
df3 = df3.astype({"year": int, "month": int, "day": int})
# Création de 2 champs pour récupérer les noms des jours et mois en question
df3['name_day'] = df3['creation_date_nr'].dt.day_name()
df3['name_month'] = df3['creation_date_nr'].dt.month_name()
# Suppression du champ month_nr
df3.drop(['month_nr'], axis=1, inplace=True)
# Renommage des champs détaillant les raisons d'appels
df3.rename(columns={'level2': 'level', 'level3': 'sub_level', 'za_rootcause_dtl': 'root_cause'}, inplace=True)
'''
st.code(code, language='python')
df3['creation_date_nr'] = pd.to_datetime(df3['creation_date_nr'], format='%Y%m%d')
df3[["year", "month", "day"]] = df3["creation_date_nr"].astype(str).str.split("-", expand = True)
df3 = df3.astype({"year": int, "month": int, "day": int})
df3['name_day'] = df3['creation_date_nr'].dt.day_name()
df3['name_month'] = df3['creation_date_nr'].dt.month_name()
df3.drop(['month_nr'], axis=1, inplace=True)
df3.rename(columns={'level2': 'level', 'level3': 'sub_level', 'za_rootcause_dtl': 'root_cause'}, inplace=True)

code = '''
# Lecture du jeu de données à jour
df3.head()
'''
st.code(code, language='python')
st.dataframe(df3.head())

# VISUALISATION DES DONNEES
st.subheader("Visualisation des données")
# df3.shape
code = '''
# On vérifie la taille de notre dataset pour en connaitre le nombre d'appels reçus au Service Client
df3.shape
'''
st.code(code, language='python')
st.write(df3.shape)
st.markdown("On comptabilise **52 031** appels passés au service client sur les mois d'Octobre et Novembre.")

# Nombre uniques de personnes
code = '''
# On peut aussi vérifier le nombre d'appels uniques
len(df3.customer_code_ano.unique())
'''
st.code(code, language='python')
st.write(len(df3.customer_code_ano.unique()))
st.markdown("On comptabilise **43 405** personnes qui ont contactés le service client sur les mois d'Octobre et Novembre.")
st.markdown("On choisi tout d'abord d'anayser la répartition de ces appels dans le temps.")

nb_callsPerDay = df3.creation_date_nr.value_counts().sort_index()
repartition_appels = px.line(nb_callsPerDay, x=nb_callsPerDay.index, y=nb_callsPerDay.values, labels={"index": "Date", "y": "Nombre d'appels"}, title="Répartition du nombre d'appels entre le 31/10/2021 et 30/11/2021")
st.plotly_chart(repartition_appels, use_container_width=False, sharing="streamlit")
st.markdown("On remarque des pics d'appels réguliers aux mêmes jours de la semaine.")
st.markdown("On peut visualiser la répartition cumulée de ces appels la semaine afin de cibler quels jours le Service Client est majoritairement solicité.")
calls_per_dayOfTheWeek = px.histogram(df3, x="name_day", color="name_month", category_orders=dict(name_day=["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]), labels={"name_day": "Jour", "name_month": "Mois"}, title="Nombre d'appels suivant les jours de la semaine")
st.plotly_chart(calls_per_dayOfTheWeek, use_container_width=False, sharing="streamlit")

st.markdown("La plupart des appels sont surtout répartis sur 3 jours : les **Dimanches**, **Lundis** et **Mardis**. La répartition sur ces 3 jours est équitable : **10 000+ appels** sur chacun d'eux.")

st.markdown("On s'intéresse ensuite à la caractérisation de ce appels via un sunburst. Ce graphique va nous permettre de visualiser le nombre d'appels sur Octobre et Novembre ainsi que les catégories de raisons de ces appels.")

call_categories = px.sunburst(df3, values=df3.value_counts(), path=["name_month", "level"], height=500)
call_categories.update_traces(textinfo="label+percent parent")
st.plotly_chart(call_categories, use_container_width=False, sharing="streamlit")

st.markdown("On remarque que pour chacun des mois d'Octobre et Novembre, environ **un quart** des appels concerne de la **prospection** (des clients potentiels donc).")



############################################################################################
############################### DF4 Gross_Adds.csv #########################################
############################################################################################
st.header("#4 Gross Adds.csv")
st.markdown("Tous les nouveaux contrats réalisés entre le 25/11/2021 et le 21/12/2021")
code = '''
# Lecture des données
df4 = pd.read_csv('Gross_Adds.csv')
df4.head()
'''
st.code(code, language='python')
st.dataframe(df4.head())

# df4.shape
code = '''
# On vérifie la taille de notre dataset
df4.shape
'''
st.code(code, language='python')
st.write(df4.shape)

# df4.info()
code = '''
# On vérifie les infos de notre dataset
df4.info()
'''
st.code(code, language='python')
buffer = io.StringIO()
df4.info(buf=buffer)
s = buffer.getvalue()
st.text(s)

# df4.isna().sum()
code = '''
# On vérifie si on a des valeurs manquantes
df4.isna().sum()
'''
st.code(code, language='python')
st.write(df4.isna().sum())

code = '''
# Lecture du dictionnaire
f_gross_adds = open("./assets/Dictionnaire-Gross_adds.txt", "r")
'''
st.code(code, language='python')
f_gross_adds = open("./assets/Dictionnaire-Gross_adds.txt", "r")
st.text(f_gross_adds.read())

# df4 --> ANALYSE DE DF4 EN L'ETAT
st.subheader("Ajustements à apporter au dataset")
code = '''
# Supression des colonnes inutiles pour l'analyse
df4.drop(['contr_comment_desc', 'contr_status_prev_cd', 'company', 'contr_current_status', 'trf_mdl_bus_segm_desc', 'trf_mdl_bus_res_ind'], axis=1, inplace=True)
# Suppression des valeurs Activation takeover dans la colonne contrat_action_desc (car non pertinent pour l'analyse)
df4.drop(df4[df4.contr_action_desc == 'Activation Takeover'].index, inplace=True)
# Mise au bon format des colonnes contenant des dates
df4['contr_activation_dt'] = pd.to_datetime(df4['contr_activation_dt'])
df4['hist_from_dt'] = pd.to_datetime(df4['hist_from_dt']).dt.date
df4['cust_activation_dttm'] = pd.to_datetime(df4['cust_activation_dttm'])
df4['port_dt'] = pd.to_datetime(df4['port_dt'])
# Age et code postal au format int
df4 = df4.astype({"cust_city_cd": int, "customer_age": int})
'''
st.code(code, language='python')

code = '''
# Plusieurs colonnes contiennent des valeurs manquantes, nous allons donc les remplir
df4['port_dt'] = df4['port_dt'].fillna(0)
df4['port_old_operator_id'] = df4['port_old_operator_id'].fillna('Unknown')
df4['sls_agt_macro_segment_desc'] = df4['sls_agt_macro_segment_desc'].fillna('Unknown')
df4['sls_agt_macro_unit_desc'] = df4['sls_agt_macro_unit_desc'].fillna('Unknown')
df4['cust_region_nm'] = df4['cust_region_nm'].fillna('Unknown')
df4['cust_province_nm'] = df4['cust_province_nm'].fillna('Unknown')
df4['gender'] = df4['gender'].fillna('N/A')
df4['cust_city_cd'] = df4['cust_city_cd'].fillna(0)
df4['customer_age'] = df4['customer_age'].fillna(0)
df4['contr_activation_dt'] = df4['contr_activation_dt'].fillna(0)
'''
st.code(code, language='python')

df4['port_dt'] = df4['port_dt'].fillna(0)
df4['port_old_operator_id'] = df4['port_old_operator_id'].fillna('Unknown')
df4['sls_agt_macro_segment_desc'] = df4['sls_agt_macro_segment_desc'].fillna('Unknown')
df4['sls_agt_macro_unit_desc'] = df4['sls_agt_macro_unit_desc'].fillna('Unknown')
df4['cust_region_nm'] = df4['cust_region_nm'].fillna('Unknown')
df4['cust_province_nm'] = df4['cust_province_nm'].fillna('Unknown')
df4['gender'] = df4['gender'].fillna('N/A')
df4['cust_city_cd'] = df4['cust_city_cd'].fillna(0)
df4['customer_age'] = df4['customer_age'].fillna(0)
df4['contr_activation_dt'] = df4['contr_activation_dt'].fillna(0)

df4.drop(['contr_comment_desc', 'contr_status_prev_cd', 'company', 'contr_current_status', 'trf_mdl_bus_segm_desc', 'trf_mdl_bus_res_ind'], axis=1, inplace=True)
df4.drop(df4[df4.contr_action_desc == 'Activation Takeover'].index, inplace=True)
df4['contr_activation_dt'] = pd.to_datetime(df4['contr_activation_dt'])
df4['hist_from_dt'] = pd.to_datetime(df4['hist_from_dt']).dt.date
df4['cust_activation_dttm'] = pd.to_datetime(df4['cust_activation_dttm'])
df4['port_dt'] = pd.to_datetime(df4['port_dt'])
df4 = df4.astype({"cust_city_cd": int, "customer_age": int})

code = '''
# Lecture du jeu de données à jour
df4.head()
'''
st.code(code, language='python')
st.dataframe(df4.head())

# VISUALISATION DES DONNEES
st.subheader("Visualisation des données")

nb_activation_in_time = df4.hist_from_dt.value_counts().sort_index()
fig = px.line(nb_activation_in_time, x=nb_activation_in_time.index, y=nb_activation_in_time.values, labels={"index": "Date", "y": "Nombre de nouveaux contrats"}, title="Répartition du nombre de contrats acquis entre le 25/11/2021 et 21/12/2021")
st.plotly_chart(fig, use_container_width=False, sharing="streamlit")
st.markdown("On remarque des pics d'activation durant les jours de la semaine et Samedis, et des creux correspondants aux Dimanches.")

forfaitXchannelXsegment = px.sunburst(df4, path=["cust_mkt_segm_desc", "sls_agt_macro_segment_desc", "trf_mdl_cat_desc"], values=df4.value_counts(), height=700)
forfaitXchannelXsegment.update_layout(uniformtext=dict(minsize=10, mode='hide'))
st.plotly_chart(forfaitXchannelXsegment, use_container_width=False, sharing="streamlit")
st.markdown("Sans grand surprise, la plupart des acquisitions se font sur le marché MASS (grand public), le segment SOHO (petites entreprises) étant une niche de marché. "
            "Le sunburst nous permet de voir que près de la moitié des ventes s'effectue via le canal **MOBISTAR CENTER**.")
st.markdown("On peut ensuite visualiser, via un bar chart horizontal, les forfaits les plus vendus (car peu lisible sur notre sunburst).")

repartition_forfaits = px.histogram(df4, x=df4.value_counts(), y="trf_mdl_cat_desc", color="cust_mkt_segm_desc", labels={"cust_mkt_segm_desc": "Segment de marché"}, title="Répartition des ventes de forfaits selon les segments de marché", height=800).update_yaxes(categoryorder="total ascending")
repartition_forfaits.update_layout(xaxis_title='Quantité vendue', yaxis_title='Forfaits')
st.plotly_chart(repartition_forfaits, use_container_width=False, sharing="streamlit")
st.markdown("Le forfait **Go Plus** est véritablement le produit phare. "
            "Il est le plus vendu de tous les forfaits sur les 2 segments pour la période de notre dataset. On peut dire que c'est le **produit le plus performant** des forfaits proposés.")
st.markdown("Cependant, avec plus de données (sur la même année ou sur les années précédentes), on pourrait le comparer à lui-même pour savoir s'il est en sur-performance ou en sous-performance.")

st.markdown("Pour approfondir on peut regarder quelle part représente chaque forfait en fonction de où vivent nos clients acquis via le sunburst suivant :")
location = px.sunburst(df4, values=df4.value_counts(), path=["cust_region_nm", "cust_province_nm", "trf_mdl_cat_desc"], height=700).update_layout(uniformtext=dict(minsize=10, mode='hide'))
location.update_traces(textinfo="label+percent parent")
st.plotly_chart(location, use_container_width=False, sharing="streamlit")
st.markdown("L'analyse confirme que le forfait **Go Plus** a été systématiquement le plus vendu dans chaque province de chacune des régions. Globalement, cette logique est la même pour le top 4 des forfaits qui ont été le plus achetés.")

st.markdown("Nous pouvons également regarder parmi les clients qui ont activé un nouveau contrat quelle part était des prospects.")
code = '''
# On récupère les identifiants uniques des clients ayant contacté le service client (Customer_Service_Interactions.csv)
df3_cust_unique = pd.DataFrame(df3['customer_code_ano'])
# On ne garde que les valeurs uniques
df3_cust_unique.drop_duplicates('customer_code_ano', keep='first', inplace=True)
# On les merge au dataset Gross-Adds
converted_prospects = pd.merge(df3_cust_unique, df4, on='customer_code_ano')
'''
st.code(code, language='python')

df3_cust_unique = pd.DataFrame(df3['customer_code_ano'])
df3_cust_unique.drop_duplicates('customer_code_ano', keep='first', inplace=True)
converted_prospects = pd.merge(df3_cust_unique, df4, on='customer_code_ano')

st.dataframe(converted_prospects.head())

# converted_prospects.shape
code = '''
# On regarde la taille de notre dataset
converted_prospects.shape
'''
st.code(code, language='python')
st.write(converted_prospects.shape)
st.markdown("Sur la période courant du 25/11/2021 au 21/12/2021, **14 046** nouveaux contrats ont été réalisés.")

# Nombre unique de clients
code = '''
# On regarde combien cela représente de clients uniques (car 1 client peut avoir souscrit à n contrats :)
len(converted_prospects.customer_code_ano.unique())
'''
st.code(code, language='python')
st.write(len(converted_prospects.customer_code_ano.unique()))
st.markdown("Ils sont détenus par **12 649** clients qui avaient, auparavant, contacté le Service Client dans le cadre de **prospection**.")


############################################################################################
############################### DF5 Payment_Responsibles.csv ###############################
############################################################################################
st.markdown("Ce dernier jeu de données concerne des informations sur la facturation (correspondant à des factures mensuelles).")
st.header("#5 Payment_Responsibles.csv")
code = '''
# Lecture des données
df5 = pd.read_csv('Payment_Responsibles.csv')
df5.head()
'''
st.code(code, language='python')
st.dataframe(df5.head())

# df5.shape
code = '''
# On vérifie la taille de notre dataset
df5.shape
'''
st.code(code, language='python')
st.write(df4.shape)

# df5.info()
code = '''
# On vérifie les infos de notre dataset
df5.info()
'''
st.code(code, language='python')
buffer = io.StringIO()
df5.info(buf=buffer)
s = buffer.getvalue()
st.text(s)

# df5.isna().sum()
code = '''
# On vérifie si on a des valeurs manquantes
df5.isna().sum()
'''
st.code(code, language='python')
st.write(df5.isna().sum())

code = '''
# Lecture du dictionnaire
f_payment_responsibles = open("./assets/Dictionnaire-Payment_Responsibles.txt", "r")
'''
st.code(code, language='python')
f_payment_responsibles = open("./assets/Dictionnaire-Payment_Responsibles.txt", "r")
st.text(f_payment_responsibles.read())

# df5 --> ANALYSE DE DF5 EN L'ETAT
st.subheader("Ajustements à apporter au dataset")
code = '''
# Remplissage des valeurs nulles
df5['subscr_trf_mdl_out_of_pocket_amt'] = df5['subscr_trf_mdl_out_of_pocket_amt'].fillna(0)
df5['subscr_device_manufacturer'] = df5['subscr_device_manufacturer'].fillna('Unknown')
df5['subscr_smartphone_ind'] = df5['subscr_smartphone_ind'].fillna(-1)
df5['subscr_paymode_type_nm'] = df5['subscr_paymode_type_nm'].fillna(-1)
df5['device_chg_days'] = df5['device_chg_days'].fillna(-1)
df5['tariff_chg_days'] = df5['tariff_chg_days'].fillna(-1)
df5['flagcable'] = df5['flagcable'].fillna(-1)
df5['myorangeapp'] = df5['myorangeapp'].fillna(-1)
df5['orange_share_2018'] = df5['mobility'].fillna(-1)
df5['mobility'] = df5['mobility'].fillna(-1)
df5['nb_tm_amt_over_equal_30'] = df5['nb_tm_amt_over_equal_30'].fillna(-1)
df5['multicard'] = df5['multicard'].fillna(-1)
df5['love_duo'] = df5['love_duo'].fillna(-1)
df5['love_trio'] = df5['love_trio'].fillna(-1)
df5['fixed_phone'] = df5['fixed_phone'].fillna(-1)
df5['easy_internet'] = df5['easy_internet'].fillna(-1)
df5['cable_boost'] = df5['cable_boost'].fillna(-1)
df5['insurance'] = df5['insurance'].fillna(-1)
df5['nb_cust_street'] = df5['nb_cust_street'].fillna(-1)
df5['nis9_population_per_sq_km'] = df5['nis9_population_per_sq_km'].fillna(-1)
df5['nis9_inc_median_net'] = df5['nis9_inc_median_net'].fillna(-1)
df5['segment'] = df5['segment'].fillna(-1)
df5['operator_switch_cnt'] = df5['operator_switch_cnt'].fillna(-1)

# Colonnes à passer au format integer
df5['subscr_trf_mdl_out_of_pocket_amt'] = df5['subscr_trf_mdl_out_of_pocket_amt'].astype('Int64')
df5['subscr_smartphone_ind'] = df5['subscr_smartphone_ind'].astype('Int64')
df5['subscr_paymode_type_nm'] = df5['subscr_paymode_type_nm'].astype('Int64')
df5['device_chg_days'] = df5['device_chg_days'].astype('Int64')
df5['tariff_chg_days'] = df5['tariff_chg_days'].astype('Int64')
df5['flagcable'] = df5['flagcable'].astype('Int64')
df5['myorangeapp'] = df5['myorangeapp'].astype('Int64')
df5['mobility'] = df5['mobility'].astype('Int64')
for col in df5[df5.columns[-13:]]:
    df5[col] = df5[col].astype('Int64')
'''
st.code(code, language='python')

df5['subscr_trf_mdl_out_of_pocket_amt'] = df5['subscr_trf_mdl_out_of_pocket_amt'].fillna(0)
df5['subscr_device_manufacturer'] = df5['subscr_device_manufacturer'].fillna('Unknown')
df5['subscr_smartphone_ind'] = df5['subscr_smartphone_ind'].fillna(-1)
df5['subscr_paymode_type_nm'] = df5['subscr_paymode_type_nm'].fillna(-1)
df5['device_chg_days'] = df5['device_chg_days'].fillna(-1)
df5['tariff_chg_days'] = df5['tariff_chg_days'].fillna(-1)
df5['flagcable'] = df5['flagcable'].fillna(-1)
df5['myorangeapp'] = df5['myorangeapp'].fillna(-1)
df5['orange_share_2018'] = df5['mobility'].fillna(-1)
df5['mobility'] = df5['mobility'].fillna(-1)
df5['nb_tm_amt_over_equal_30'] = df5['nb_tm_amt_over_equal_30'].fillna(-1)
df5['multicard'] = df5['multicard'].fillna(-1)
df5['love_duo'] = df5['love_duo'].fillna(-1)
df5['love_trio'] = df5['love_trio'].fillna(-1)
df5['fixed_phone'] = df5['fixed_phone'].fillna(-1)
df5['easy_internet'] = df5['easy_internet'].fillna(-1)
df5['cable_boost'] = df5['cable_boost'].fillna(-1)
df5['insurance'] = df5['insurance'].fillna(-1)
df5['nb_cust_street'] = df5['nb_cust_street'].fillna(-1)
df5['nis9_population_per_sq_km'] = df5['nis9_population_per_sq_km'].fillna(-1)
df5['nis9_inc_median_net'] = df5['nis9_inc_median_net'].fillna(-1)
df5['segment'] = df5['segment'].fillna(-1)
df5['operator_switch_cnt'] = df5['operator_switch_cnt'].fillna(-1)

# Colonnes à passer au format integer
df5['subscr_trf_mdl_out_of_pocket_amt'] = df5['subscr_trf_mdl_out_of_pocket_amt'].astype('Int64')
df5['subscr_smartphone_ind'] = df5['subscr_smartphone_ind'].astype('Int64')
df5['subscr_paymode_type_nm'] = df5['subscr_paymode_type_nm'].astype('Int64')
df5['device_chg_days'] = df5['device_chg_days'].astype('Int64')
df5['tariff_chg_days'] = df5['tariff_chg_days'].astype('Int64')
df5['flagcable'] = df5['flagcable'].astype('Int64')
df5['myorangeapp'] = df5['myorangeapp'].astype('Int64')
df5['mobility'] = df5['mobility'].astype('Int64')

for col in df5[df5.columns[-13:]]:
    df5[col] = df5[col].astype('Int64')

code = '''
# Lecture du jeu de données à jour
df5.head()
'''
st.code(code, language='python')
st.dataframe(df5.head())

# VISUALISATION DES DONNEES
st.subheader("Visualisation des données")

code = '''
# On commence par regarder combien on a de factures
df5.customer_code_ano.count()
# Puis combien de clients uniques
len(df5.customer_code_ano.unique())
'''
st.code(code, language='python')
st.write('Nombre de factures : ', df5.customer_code_ano.count())
st.write('Nombre de clients uniques : ', len(df5.customer_code_ano.unique()))
st.markdown("Pour sortir des analyses de ce dataset il semble pertinent de le croiser avec le dataframe df4 **_Gross_Adds._**"
            " Cependant, si on prend par exemple le _customer_code_ano_ **70** voici ce que l'on trouve dans les dataframes 4 (Gross-Adds) et 5 (Payment_Responsibles :)")
code = '''
# Dataframe Gross_Adds
df4.loc[df4['customer_code_ano'] == 70]
'''
st.code(code, language='python')
st.write(df4.loc[df4['customer_code_ano'] == 70])
st.markdown("Ce client a souscrit à un forfait **Go Plus Smart Data C**.")

code = '''
# Maintenant on regarde ce que l'on a dans df5
df5.loc[df5['customer_code_ano'] == 70]
'''
st.code(code, language='python')
st.dataframe(df5.loc[df5['customer_code_ano'] == 70])
st.markdown("On a 2 résultats. La seule chose qui différencie ces 2 lignes est le forfait. On a bien une ligne (la première) qui correspond à **Go Plus Smart Data C**."
            " L'autre ligne est associée à un autre forfait mais pour autant toutes les données dans les autres colonnes sont identiques. A ce stade nous ne savon pas expliquer cette ambigüité.")
st.markdown("Nous allons donc utiliser 2 clés afin de ne garder que les nouveaux contrats issus de Gross-Adds :")
st.markdown("- **_customer_code_ano_**")
st.markdown("- **_trf_mdl_cat_desc_**")

code = '''
# On trie les données par customer_code_ano et surtout par date d'activation
df4_sorted = df4.sort_values(by=['customer_code_ano'])
# On supprime les doublons selon le couple customer_code_ano + trf_mdl_cat_desc et on ne garde que la dernière ligne (la plus récente)
df4_sorted.drop_duplicates(subset=['customer_code_ano', 'trf_mdl_cat_desc'], keep='last', inplace=True)
# On crée un dataframe à 2 colonnes
df4_cust_forfait = df4_sorted[['customer_code_ano','trf_mdl_cat_desc']]
# On merge les 2 datasets
df4CustForfait_in_df5 = pd.merge(df5, df4_cust_forfait, on=['customer_code_ano', 'trf_mdl_cat_desc'], how='right')
df4CustForfait_in_df5.sort_values(by=['customer_code_ano'])
'''
st.code(code, language='python')

df4_sorted = df4.sort_values(by=['customer_code_ano'])
df4_sorted.drop_duplicates(subset=['customer_code_ano', 'trf_mdl_cat_desc'], keep='last', inplace=True)
df4_cust_forfait = df4_sorted[['customer_code_ano','trf_mdl_cat_desc']]
df4CustForfait_in_df5 = pd.merge(df5, df4_cust_forfait, on=['customer_code_ano', 'trf_mdl_cat_desc'], how='inner')
df4CustForfait_in_df5.sort_values(by=['customer_code_ano'])

st.dataframe(df4CustForfait_in_df5)
st.markdown("On peut désormais travailler sur notre nouveau dataframe qui contient les informations de facturation des nouveaux contrats acquis entre le 25/11/2021 et le 21/12/2021.")
st.markdown("Il y a un grand écart entre le nombre de nouveaux contrats acquis dans le dataset Gross-Adds et celui-ci (Payment Responsibles). Notre jeu de données **df4CustForfait_in_df5** est donc une petite partie des nouveaux contrats acquis et que l'on retrouve dans Payment_responsibles. De fait nous choississon de faire quelques analyses basiques.")
#fig = px.bar(df4CustForfait_in_df5, x='trf_mdl_cat_desc', y=df4CustForfait_in_df5.trf_mdl_cat_desc.value_counts())

code = '''
# On récupère quelques infos qui nous servirons à élaborer nos graphiques
cust_info = df4CustForfait_in_df5[["customer_code_ano", "subscr_device_manufacturer", "current_month_total_rev", "nis9_inc_median_net"]]
'''
st.code(code, language='python')

code = '''
# On s'intérresse aux smartphones des clients
smartphones = cust_info[cust_info.subscr_device_manufacturer != 'Unknown']
# On prend le top 10 des smartphones les plus utilisés
top10_smartphones = smartphones.subscr_device_manufacturer.value_counts().nlargest(10).to_frame()
'''
st.code(code, language='python')

cust_info = df4CustForfait_in_df5[["customer_code_ano", "subscr_trf_mdl_out_of_pocket_amt", "subscr_device_manufacturer", "current_month_total_rev", "nis9_inc_median_net"]]
smartphones = cust_info[cust_info.subscr_device_manufacturer != 'Unknown']
top10_smartphones = smartphones.subscr_device_manufacturer.value_counts().nlargest(10).to_frame()

repartition_smartphones = px.pie(top10_smartphones, values=top10_smartphones.subscr_device_manufacturer, names=top10_smartphones.index, title="Smartphones utilisés par nos clients", height=700)
repartition_smartphones.update_traces(textposition='inside', textinfo='percent+label')
st.plotly_chart(repartition_smartphones, use_container_width=False, sharing="streamlit")

st.markdown("Nos nouveaux clients ont majoritairement un mobile de marque Samsung ou Apple. S'en suivent 2 constructeurs Chinois, Xiaomi et Huawei. Les autres marques sont à leur image sur le marché: moins répandues.")

st.markdown("Répartition des forfaits :")
fig = px.box(cust_info, y="subscr_trf_mdl_out_of_pocket_amt")
st.plotly_chart(fig, use_container_width=False, sharing="streamlit")
st.markdown("En général les nouveaux contrats ont un forfait qui s'élève à **30€.**")

fig = px.box(cust_info, y="current_month_total_rev")
st.plotly_chart(fig, use_container_width=False, sharing="streamlit")
st.markdown("Mais rééllement la facture s'élève à moins chère, ce qui peut paraître curieux puisque _current_month_total_rev_ correspond au total de la facture avec les options et nous avons pas mal de valeurs abberrantes qui auraient été censées tirer les chiffres vers le haut.")

st.markdown("Enfin, on peut s'intéresser au revenu médian net par habitant dans la zone de résidence du client.")
fig = px.box(cust_info, y="nis9_inc_median_net")
st.plotly_chart(fig, use_container_width=False, sharing="streamlit")
st.markdown("En général les clients sont issus de zones géographiques où le revenu médian net est autour de **22,300 K€**.")