# Projet IA Immobilier - Estimation des Prix

Modèle de Machine Learning pour estimer les prix immobiliers en France.

## Installation

### 1. Cloner le projet

```bash
git clone https://github.com/zineb35/IA-immobilier.git
cd IA-immobilier
```

### 2. Installer les dépendances

```bash
pip install pandas numpy scikit-learn matplotlib seaborn plotly streamlit joblib
```

Ou avec le fichier requirements :

```bash
pip install -r dashboard/requirements.txt
```

## Lancer le Dashboard

```bash
cd dashboard
streamlit run app.py
```

Le dashboard s'ouvre automatiquement sur http://localhost:8501

## Structure du Projet

```
├── Data/raw/           # Données CSV
├── N/                  # Documentation
├── dashboard/          # Application Streamlit
│   ├── app.py
│   └── requirements.txt
└── test/
    └── modelisation.ipynb  # Notebook de modélisation
```

## Données

**Source** : https://www.kaggle.com/datasets/benoitfavier/immobilier-france

## Auteur

Projet réalisé dans le cadre d'une formation en Data.
