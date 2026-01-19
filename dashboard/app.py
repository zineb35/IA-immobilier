# =============================================================================
# 🏠 DASHBOARD IA IMMOBILIER - STREAMLIT
# =============================================================================
# Application interactive pour visualiser et utiliser le modèle de prédiction

import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
import plotly.graph_objects as go
from plotly.subplots import make_subplots
import joblib
import os

# Configuration de la page
st.set_page_config(
    page_title="🏠 IA Immobilier - Estimation Prix",
    page_icon="🏠",
    layout="wide",
    initial_sidebar_state="expanded"
)

# =============================================================================
# CHARGEMENT DES DONNÉES ET MODÈLE
# =============================================================================

@st.cache_data
def load_data():
    """Charger les données prétraitées"""
    df = pd.read_csv('../Data/raw/data_tableau.csv')
    return df

@st.cache_resource
def load_model():
    """Charger le modèle entraîné"""
    model = joblib.load('../N/random_forest_model.pkl')
    return model

# Charger les données
try:
    df = load_data()
    model = load_model()
    model_loaded = True
except Exception as e:
    st.error(f"Erreur de chargement : {e}")
    model_loaded = False
    df = None

# =============================================================================
# SIDEBAR - NAVIGATION
# =============================================================================

st.sidebar.title("🏠 IA Immobilier")
st.sidebar.markdown("---")

page = st.sidebar.radio(
    "Navigation",
    ["📊 Vue d'ensemble", "🔮 Prédiction de Prix", "📈 Analyse du Modèle", "🗺️ Carte Interactive"]
)

st.sidebar.markdown("---")
st.sidebar.markdown("### 📋 Informations Modèle")
st.sidebar.metric("Modèle", "Random Forest")
st.sidebar.metric("MAE", "55,936 €")
st.sidebar.metric("R² Score", "0.62")

st.sidebar.markdown("---")
st.sidebar.markdown("*Projet IA Immobilier - 2025*")

# =============================================================================
# PAGE 1 : VUE D'ENSEMBLE
# =============================================================================

if page == "📊 Vue d'ensemble":
    st.title("📊 Vue d'ensemble du Marché Immobilier")
    st.markdown("---")
    
    if df is not None:
        # KPIs en haut
        col1, col2, col3, col4 = st.columns(4)
        
        with col1:
            st.metric(
                label="🏠 Nombre de Biens",
                value=f"{len(df):,}",
                delta=None
            )
        
        with col2:
            st.metric(
                label="💰 Prix Moyen",
                value=f"{df['prix'].mean():,.0f} €",
                delta=None
            )
        
        with col3:
            st.metric(
                label="📐 Surface Moyenne",
                value=f"{df['surface_habitable'].mean():.0f} m²",
                delta=None
            )
        
        with col4:
            st.metric(
                label="💵 Prix/m² Moyen",
                value=f"{df['prix_m2'].mean():,.0f} €/m²",
                delta=None
            )
        
        st.markdown("---")
        
        # Graphiques
        col1, col2 = st.columns(2)
        
        with col1:
            st.subheader("📊 Distribution des Prix")
            fig = px.histogram(
                df, x='prix', nbins=20,
                color_discrete_sequence=['#1f77b4'],
                labels={'prix': 'Prix (€)', 'count': 'Nombre de biens'}
            )
            fig.update_layout(showlegend=False)
            st.plotly_chart(fig, use_container_width=True)
        
        with col2:
            st.subheader("🏠 Répartition par Type")
            type_counts = df['type_batiment'].value_counts()
            fig = px.pie(
                values=type_counts.values,
                names=type_counts.index,
                color_discrete_sequence=['#1f77b4', '#ff7f0e']
            )
            st.plotly_chart(fig, use_container_width=True)
        
        col1, col2 = st.columns(2)
        
        with col1:
            st.subheader("📈 Prix vs Surface")
            fig = px.scatter(
                df, x='surface_habitable', y='prix',
                color='type_batiment',
                hover_data=['ville', 'n_pieces'],
                labels={'surface_habitable': 'Surface (m²)', 'prix': 'Prix (€)'},
                color_discrete_sequence=['#1f77b4', '#ff7f0e']
            )
            st.plotly_chart(fig, use_container_width=True)
        
        with col2:
            st.subheader("🌍 Prix/m² par Région")
            prix_region = df.groupby('region')['prix_m2'].mean().sort_values(ascending=True)
            fig = px.bar(
                x=prix_region.values,
                y=prix_region.index,
                orientation='h',
                color=prix_region.values,
                color_continuous_scale='Blues',
                labels={'x': 'Prix/m² (€)', 'y': 'Région'}
            )
            fig.update_layout(showlegend=False)
            st.plotly_chart(fig, use_container_width=True)
        
        # Tableau des données
        st.markdown("---")
        st.subheader("📋 Données Détaillées")
        
        # Filtres
        col1, col2, col3 = st.columns(3)
        with col1:
            region_filter = st.multiselect("Région", df['region'].unique(), default=df['region'].unique())
        with col2:
            type_filter = st.multiselect("Type de bien", df['type_batiment'].unique(), default=df['type_batiment'].unique())
        with col3:
            prix_range = st.slider("Fourchette de prix (€)", 0, int(df['prix'].max()), (0, int(df['prix'].max())))
        
        # Appliquer filtres
        df_filtered = df[
            (df['region'].isin(region_filter)) &
            (df['type_batiment'].isin(type_filter)) &
            (df['prix'] >= prix_range[0]) &
            (df['prix'] <= prix_range[1])
        ]
        
        st.dataframe(
            df_filtered[['ville', 'type_batiment', 'surface_habitable', 'n_pieces', 'prix', 'prix_m2', 'region']].rename(columns={
                'ville': 'Ville',
                'type_batiment': 'Type',
                'surface_habitable': 'Surface (m²)',
                'n_pieces': 'Pièces',
                'prix': 'Prix (€)',
                'prix_m2': 'Prix/m² (€)',
                'region': 'Région'
            }),
            use_container_width=True
        )

# =============================================================================
# PAGE 2 : PRÉDICTION DE PRIX
# =============================================================================

elif page == "🔮 Prédiction de Prix":
    st.title("🔮 Estimation du Prix d'un Bien")
    st.markdown("Entrez les caractéristiques du bien pour obtenir une estimation de prix.")
    st.markdown("---")
    
    if model_loaded:
        col1, col2 = st.columns(2)
        
        with col1:
            st.subheader("📝 Caractéristiques du Bien")
            
            surface = st.number_input("Surface habitable (m²)", min_value=10, max_value=500, value=100)
            n_pieces = st.number_input("Nombre de pièces", min_value=1, max_value=15, value=4)
            type_batiment = st.selectbox("Type de bien", ["Maison", "Appartement"])
            vefa = st.selectbox("État", ["Ancien", "Neuf (VEFA)"])
            
        with col2:
            st.subheader("📍 Localisation")
            
            is_idf = st.selectbox("Région", ["Île-de-France", "Province"])
            loyer_m2 = st.slider("Loyer moyen au m² (€)", 5.0, 30.0, 12.0)
            revenu_fiscal = st.slider("Revenu fiscal moyen (€)", 15000, 50000, 25000)
            
            # Coordonnées simplifiées
            if is_idf == "Île-de-France":
                lat, lon = 48.85, 2.35
            else:
                lat, lon = 45.75, 4.85
        
        st.markdown("---")
        
        # Bouton de prédiction
        if st.button("🎯 Estimer le Prix", type="primary", use_container_width=True):
            # Préparer les features
            features = {
                'surface_habitable': surface,
                'n_pieces': n_pieces,
                'type_batiment_encoded': 1 if type_batiment == "Maison" else 0,
                'vefa_encoded': 1 if vefa == "Neuf (VEFA)" else 0,
                'loyer_m2_local': loyer_m2,
                'revenu_fiscal_moyen': revenu_fiscal,
                'surface_par_piece': surface / n_pieces,
                'is_idf': 1 if is_idf == "Île-de-France" else 0,
                'latitude': lat,
                'longitude': lon
            }
            
            X_pred = pd.DataFrame([features])
            
            # Prédiction
            prix_estime = model.predict(X_pred)[0]
            prix_m2_estime = prix_estime / surface
            
            # Affichage des résultats
            st.markdown("---")
            st.subheader("💰 Résultat de l'Estimation")
            
            col1, col2, col3 = st.columns(3)
            
            with col1:
                st.metric(
                    label="Prix Estimé",
                    value=f"{prix_estime:,.0f} €"
                )
            
            with col2:
                st.metric(
                    label="Prix au m²",
                    value=f"{prix_m2_estime:,.0f} €/m²"
                )
            
            with col3:
                st.metric(
                    label="Marge d'erreur (MAE)",
                    value="± 55,936 €"
                )
            
            # Fourchette de prix
            st.markdown("---")
            st.subheader("📊 Fourchette de Prix")
            
            prix_min = max(0, prix_estime - 55936)
            prix_max = prix_estime + 55936
            
            fig = go.Figure()
            
            fig.add_trace(go.Indicator(
                mode="gauge+number",
                value=prix_estime,
                domain={'x': [0, 1], 'y': [0, 1]},
                title={'text': "Prix Estimé (€)"},
                gauge={
                    'axis': {'range': [prix_min * 0.8, prix_max * 1.2]},
                    'bar': {'color': "#1f77b4"},
                    'steps': [
                        {'range': [prix_min * 0.8, prix_min], 'color': "#e8e8e8"},
                        {'range': [prix_min, prix_max], 'color': "#b8d4e8"},
                        {'range': [prix_max, prix_max * 1.2], 'color': "#e8e8e8"}
                    ],
                    'threshold': {
                        'line': {'color': "red", 'width': 4},
                        'thickness': 0.75,
                        'value': prix_estime
                    }
                }
            ))
            
            st.plotly_chart(fig, use_container_width=True)
            
            st.info(f"""
            📌 **Interprétation** :
            - Fourchette basse : **{prix_min:,.0f} €**
            - Estimation centrale : **{prix_estime:,.0f} €**
            - Fourchette haute : **{prix_max:,.0f} €**
            
            ⚠️ Cette estimation est basée sur un modèle ML avec un R² de 0.62. 
            La décision finale doit être validée par un expert immobilier.
            """)
    else:
        st.error("Le modèle n'a pas pu être chargé. Veuillez vérifier les fichiers.")

# =============================================================================
# PAGE 3 : ANALYSE DU MODÈLE
# =============================================================================

elif page == "📈 Analyse du Modèle":
    st.title("📈 Analyse des Performances du Modèle")
    st.markdown("---")
    
    if df is not None:
        # Métriques du modèle
        col1, col2, col3, col4 = st.columns(4)
        
        with col1:
            st.metric("R² Score", "0.62", help="Coefficient de détermination")
        with col2:
            st.metric("MAE", "55,936 €", help="Mean Absolute Error")
        with col3:
            st.metric("RMSE", "73,602 €", help="Root Mean Square Error")
        with col4:
            st.metric("Erreur Relative", "27%", help="MAE / Prix moyen")
        
        st.markdown("---")
        
        # Graphiques d'analyse
        col1, col2 = st.columns(2)
        
        with col1:
            st.subheader("🎯 Prédictions vs Valeurs Réelles")
            
            fig = px.scatter(
                df, x='prix', y='prix_predit',
                color='erreur_pct',
                color_continuous_scale='RdYlGn_r',
                labels={'prix': 'Prix Réel (€)', 'prix_predit': 'Prix Prédit (€)', 'erreur_pct': 'Erreur (%)'},
                hover_data=['ville', 'type_batiment']
            )
            
            # Ligne parfaite
            fig.add_trace(go.Scatter(
                x=[df['prix'].min(), df['prix'].max()],
                y=[df['prix'].min(), df['prix'].max()],
                mode='lines',
                name='Prédiction parfaite',
                line=dict(color='red', dash='dash')
            ))
            
            st.plotly_chart(fig, use_container_width=True)
        
        with col2:
            st.subheader("📊 Distribution des Erreurs")
            
            fig = px.histogram(
                df, x='erreur',
                nbins=20,
                color_discrete_sequence=['#1f77b4'],
                labels={'erreur': 'Erreur (€)', 'count': 'Fréquence'}
            )
            fig.add_vline(x=0, line_dash="dash", line_color="red", annotation_text="Erreur = 0")
            fig.add_vline(x=df['erreur'].mean(), line_dash="solid", line_color="green", 
                         annotation_text=f"Moyenne = {df['erreur'].mean():,.0f}€")
            
            st.plotly_chart(fig, use_container_width=True)
        
        # Importance des features
        st.markdown("---")
        st.subheader("🔑 Importance des Features")
        
        # Données d'importance (basées sur les résultats du modèle)
        importance_data = pd.DataFrame({
            'Feature': ['loyer_m2_local', 'surface_habitable', 'revenu_fiscal_moyen', 
                       'n_pieces', 'longitude', 'latitude', 'surface_par_piece',
                       'is_idf', 'type_batiment_encoded', 'vefa_encoded'],
            'Importance': [0.491, 0.178, 0.136, 0.074, 0.040, 0.039, 0.038, 0.002, 0.001, 0.001]
        }).sort_values('Importance', ascending=True)
        
        fig = px.bar(
            importance_data, 
            x='Importance', 
            y='Feature',
            orientation='h',
            color='Importance',
            color_continuous_scale='Blues',
            labels={'Importance': 'Importance (Gini)', 'Feature': 'Variable'}
        )
        fig.update_layout(showlegend=False)
        st.plotly_chart(fig, use_container_width=True)
        
        # Interprétation
        st.markdown("---")
        st.subheader("📋 Interprétation des Résultats")
        
        col1, col2 = st.columns(2)
        
        with col1:
            st.success("""
            **✅ Points Forts :**
            - R² de 0.62 : modèle acceptable
            - MAE de 27% : erreur relative correcte
            - Top feature identifiée : loyer_m2_local (49%)
            - Modèle explicable et interprétable
            """)
        
        with col2:
            st.warning("""
            **⚠️ Points d'Amélioration :**
            - Dataset limité (100 observations)
            - Validation croisée instable
            - Features manquantes (DPE, année...)
            - Nécessite plus de données
            """)

# =============================================================================
# PAGE 4 : CARTE INTERACTIVE
# =============================================================================

elif page == "🗺️ Carte Interactive":
    st.title("🗺️ Carte des Biens Immobiliers")
    st.markdown("---")
    
    if df is not None:
        # Filtres
        col1, col2 = st.columns(2)
        with col1:
            color_by = st.selectbox("Colorier par", ['prix_m2', 'prix', 'erreur_pct', 'type_batiment'])
        with col2:
            size_by = st.selectbox("Taille par", ['surface_habitable', 'prix', 'n_pieces'])
        
        # Carte
        fig = px.scatter_mapbox(
            df,
            lat='latitude',
            lon='longitude',
            color=color_by,
            size=size_by,
            hover_name='ville',
            hover_data=['prix', 'surface_habitable', 'type_batiment', 'prix_m2'],
            color_continuous_scale='Viridis' if color_by != 'type_batiment' else None,
            zoom=5,
            height=600,
            title="Localisation des Biens"
        )
        
        fig.update_layout(mapbox_style="open-street-map")
        st.plotly_chart(fig, use_container_width=True)
        
        # Statistiques par région
        st.markdown("---")
        st.subheader("📊 Statistiques par Région")
        
        stats_region = df.groupby('region').agg({
            'prix': ['mean', 'median', 'count'],
            'prix_m2': 'mean',
            'surface_habitable': 'mean'
        }).round(0)
        
        stats_region.columns = ['Prix Moyen (€)', 'Prix Médian (€)', 'Nb Biens', 'Prix/m² (€)', 'Surface Moy. (m²)']
        stats_region = stats_region.reset_index()
        
        st.dataframe(stats_region, use_container_width=True)

# =============================================================================
# FOOTER
# =============================================================================

st.markdown("---")
st.markdown(
    """
    <div style='text-align: center; color: gray;'>
        🏠 Dashboard IA Immobilier | Modèle Random Forest | R² = 0.62 | MAE = 55,936€
        <br>
        Projet Data Science - 2025
    </div>
    """,
    unsafe_allow_html=True
)
