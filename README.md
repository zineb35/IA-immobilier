# Projet IA Immobilier - Estimation des Prix

## Vue d'ensemble

Ce projet développe un modèle de Machine Learning pour estimer les prix immobiliers en France, permettant aux agents immobiliers d'automatiser et d'améliorer leurs estimations.

## Source des Données

Les données utilisées proviennent de Kaggle :  
**https://www.kaggle.com/datasets/benoitfavier/immobilier-france**

---

## Objectifs du Projet

1. **Exploration des données** - Analyse complète du marché immobilier
2. **Preprocessing** - Nettoyage, enrichissement et feature engineering
3. **Modélisation ML** - Comparaison de 5 algorithmes
4. **Évaluation** - Métriques et KPIs business
5. **Dashboard** - Visualisation Tableau Public
6. **Documentation** - Note technique reproductible
7. **Conformité** - Analyse RGPD et IA Act
8. **Coûts Azure** - Estimation déploiement cloud

---

## Résultats Clés

| Métrique | Valeur |
|----------|--------|
| **Modèle retenu** | Random Forest |
| **MAE** | 55,936 € |
| **R² Score** | 0.62 |
| **Feature #1** | loyer_m2_local (49%) |
| **Dataset** | 100 transactions |

---

## Structure du Projet

```
data ia immobilier/
│
├── Data/
│   └── raw/
│       ├── transactions_sample.csv      # Données brutes
│       ├── transactions_preprocessed.csv # Données nettoyées
│       ├── data_tableau.csv             # Export pour Tableau
│       ├── loyers.csv                   # Loyers par département
│       ├── foyers_fiscaux.csv           # Revenus fiscaux
│       ├── taux_interet.csv             # Taux d'intérêt
│       └── ...
│
├── N/
│   ├── exploration.ipynb      # Notebook EDA
│   ├── preprocessing.ipynb    # Notebook preprocessing
│   ├── random_forest_model.pkl # Modèle entraîné
│   ├── scaler.pkl             # StandardScaler
│   ├── model_results.txt      # Résultats
│   ├── evaluation_kpis.md     # KPIs et métriques
│   ├── guide_tableau.md       # Guide Tableau Public
│   ├── note_technique.md      # Documentation technique
│   ├── conformite_rgpd.md     # Conformité légale
│   ├── estimation_azure.md    # Coûts Azure
│   └── *.png                  # Graphiques générés
│
├── dashboard/
│   ├── app.py                 # Dashboard Streamlit
│   └── requirements.txt       # Dépendances
│
├── test/
│   └── modelisation.ipynb     # Notebook modélisation
│
└── README.md                  # Ce fichier
```

---

## Guide de Démarrage

### 1. Prérequis

```bash
Python 3.11+
pandas
numpy
scikit-learn
matplotlib
seaborn
joblib
streamlit
plotly
```

### 2. Exécution des Notebooks

```bash
# 1. Exploration
jupyter notebook N/exploration.ipynb

# 2. Preprocessing
jupyter notebook N/preprocessing.ipynb

# 3. Modélisation
jupyter notebook test/modelisation.ipynb
```

### 3. Lancer le Dashboard

```bash
cd dashboard
pip install -r requirements.txt
streamlit run app.py
```

### 4. Utilisation du Modèle

```python
import joblib
import pandas as pd

# Charger le modèle
model = joblib.load('N/random_forest_model.pkl')
scaler = joblib.load('N/scaler.pkl')

# Prédire un prix
nouveau_bien = {
    'surface_habitable': 100,
    'n_pieces': 4,
    'type_batiment_encoded': 1,  # Maison
    'vefa_encoded': 0,
    'loyer_m2_local': 12.5,
    'revenu_fiscal_moyen': 25000,
    'surface_par_piece': 25,
    'is_idf': 1,
    'latitude': 48.85,
    'longitude': 2.35
}

X = pd.DataFrame([nouveau_bien])
prix_estime = model.predict(X)[0]
print(f"Prix estimé : {prix_estime:,.0f} €")
```

---

## Features Importantes

| Rang | Feature | Importance |
|------|---------|------------|
| 1 | loyer_m2_local | 49.1% |
| 2 | surface_habitable | 17.8% |
| 3 | revenu_fiscal_moyen | 13.6% |
| 4 | n_pieces | 7.4% |
| 5 | longitude | 4.0% |

---

## Livrables

| Document | Description |
|----------|-------------|
| `exploration.ipynb` | Analyse exploratoire complète |
| `preprocessing.ipynb` | Pipeline de préparation des données |
| `modelisation.ipynb` | Entraînement et comparaison des modèles |
| `note_technique.md` | Documentation technique complète |
| `evaluation_kpis.md` | KPIs et métriques d'évaluation |
| `conformite_rgpd.md` | Analyse de conformité légale |
| `estimation_azure.md` | Estimation des coûts de déploiement |
| `guide_tableau.md` | Guide pour créer le dashboard |
| `data_tableau.csv` | Données prêtes pour Tableau Public |
| `app.py` | Dashboard Streamlit interactif |

---

## Limites Connues

- Dataset limité (100 observations)
- Forte variance en cross-validation
- Absence de DPE et année de construction
- Modèle à retrainer régulièrement

---

## Améliorations Futures

1. Augmenter le dataset (objectif : 1000+ transactions)
2. Ajouter features : DPE, année construction, état
3. Segmenter par type de bien et région
4. Tester Deep Learning (TabNet, MLP)
5. Intégrer données temps réel DVF

---

## Coûts de Déploiement

| Option | Coût mensuel | Cas d'usage |
|--------|--------------|-------------|
| Minimale | ~30€ | POC / Tests |
| Standard | ~150€ | Production PME |
| Enterprise | ~500€ | Grande entreprise |

---

*Projet IA Immobilier - 2025*
