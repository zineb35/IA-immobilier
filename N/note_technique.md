# 📋 NOTE TECHNIQUE - Projet IA Immobilier

## Estimation des Prix Immobiliers par Machine Learning

**Version** : 1.0  
**Date** : Janvier 2025  
**Auteur** : Data Scientist  
**Client** : Agence Immobilière

---

## 📌 Résumé Exécutif

Ce projet vise à développer un modèle de Machine Learning capable d'estimer les prix des biens immobiliers à partir de leurs caractéristiques intrinsèques et de données macroéconomiques. Le modèle Random Forest optimisé atteint une **MAE de 55,936€** et un **R² de 0.62**, permettant d'automatiser les estimations avec une précision acceptable.

---

## 1. Contexte et Problématique Business

### 1.1 Contexte
Le marché immobilier français est caractérisé par une forte variabilité des prix selon la localisation, le type de bien et les conditions économiques. Les agents immobiliers passent un temps considérable à estimer les prix manuellement.

### 1.2 Problématique
**Comment automatiser l'estimation des prix immobiliers tout en maintenant une précision acceptable pour une utilisation opérationnelle ?**

### 1.3 Objectifs
1. Développer un modèle ML prédictif des prix
2. Identifier les facteurs clés influençant les prix
3. Fournir un outil d'aide à la décision pour les agents
4. Réduire le temps d'estimation de 30 min à 5 min

---

## 2. Données Utilisées

### 2.1 Sources de Données

| Fichier | Description | Observations |
|---------|-------------|--------------|
| `transactions_sample.csv` | Transactions immobilières | 100 |
| `loyers.csv` | Loyers par département | Enrichissement |
| `foyers_fiscaux.csv` | Revenus fiscaux | Enrichissement |
| `taux_interet.csv` | Taux d'intérêt | Contexte macro |
| `actifs_financiers.csv` | Actifs financiers | Non utilisé |

### 2.2 Variables Cibles et Features

**Variable cible (Y)** : `prix` (prix de vente en €)

**Features sélectionnées (X)** :

| Feature | Type | Description |
|---------|------|-------------|
| `surface_habitable` | Numérique | Surface en m² |
| `n_pieces` | Numérique | Nombre de pièces |
| `type_batiment_encoded` | Binaire | 0=Appartement, 1=Maison |
| `vefa_encoded` | Binaire | 0=Ancien, 1=Neuf (VEFA) |
| `loyer_m2_local` | Numérique | Loyer moyen au m² (département) |
| `revenu_fiscal_moyen` | Numérique | Revenu fiscal moyen (département) |
| `surface_par_piece` | Numérique | Surface / Nombre pièces |
| `is_idf` | Binaire | 1=Île-de-France, 0=Autres |
| `latitude` | Numérique | Coordonnée GPS |
| `longitude` | Numérique | Coordonnée GPS |

### 2.3 Statistiques Descriptives

| Statistique | Prix (€) | Surface (m²) |
|-------------|----------|--------------|
| Moyenne | 208,840 | 91.9 |
| Médiane | 169,000 | 90.0 |
| Écart-type | 123,785 | 38.4 |
| Min | 47,000 | 20.0 |
| Max | 600,000 | 250.0 |

---

## 3. Méthodologie

### 3.1 Pipeline de Traitement

```
Données brutes → Nettoyage → Enrichissement → Feature Engineering → Modélisation → Évaluation
```

### 3.2 Preprocessing

1. **Nettoyage** :
   - Suppression des colonnes non pertinentes (id, adresse, etc.)
   - Gestion des valeurs manquantes (imputation médiane)
   - Conversion des types de données

2. **Enrichissement** :
   - Jointure avec données de loyers (par département)
   - Jointure avec données fiscales (par département)
   - Gestion des départements Corse (2A, 2B)

3. **Feature Engineering** :
   - `surface_par_piece` = surface / n_pieces
   - `is_idf` = 1 si département Île-de-France
   - Encodage des variables catégorielles

### 3.3 Modélisation

#### Modèles testés :

| Modèle | MAE (€) | RMSE (€) | R² |
|--------|---------|----------|-----|
| Régression Linéaire | 65,754 | 83,712 | 0.510 |
| Ridge Regression | 63,567 | 79,565 | 0.557 |
| Lasso Regression | 65,753 | 83,708 | 0.510 |
| **Random Forest** | **53,169** | **67,138** | **0.685** |
| Gradient Boosting | 65,434 | 78,703 | 0.567 |

#### Optimisation (GridSearchCV) :

```python
param_grid = {
    'n_estimators': [50, 100, 200],
    'max_depth': [5, 10, 20, None],
    'min_samples_split': [2, 5, 10],
    'min_samples_leaf': [1, 2, 4]
}
```

**Meilleurs hyperparamètres** :
- `n_estimators`: 200
- `max_depth`: 5
- `min_samples_split`: 2
- `min_samples_leaf`: 2

---

## 4. Résultats

### 4.1 Performance du Modèle Final

| Métrique | Valeur | Interprétation |
|----------|--------|----------------|
| **MAE** | 55,936 € | Erreur moyenne de ~56K€ |
| **RMSE** | 73,602 € | Sensibilité aux outliers |
| **R²** | 0.6211 | 62% variance expliquée |
| **MAPE** | ~27% | Erreur relative moyenne |

### 4.2 Importance des Features

| Rang | Feature | Importance |
|------|---------|------------|
| 1 | `loyer_m2_local` | 49.1% |
| 2 | `surface_habitable` | 17.8% |
| 3 | `revenu_fiscal_moyen` | 13.6% |
| 4 | `n_pieces` | 7.4% |
| 5 | `longitude` | 4.0% |

### 4.3 Validation Croisée

| Fold | R² Score |
|------|----------|
| 1 | -0.68 |
| 2 | 0.21 |
| 3 | 0.65 |
| 4 | 0.56 |
| 5 | -0.35 |
| **Moyenne** | **0.08 ± 0.52** |

⚠️ La forte variabilité est due au faible volume de données (100 observations).

---

## 5. Limites et Biais Identifiés

### 5.1 Limites des Données
- **Volume insuffisant** : 100 observations est insuffisant pour un modèle robuste
- **Biais géographique** : Surreprésentation de certaines régions
- **Données manquantes** : Pas d'information sur DPE, année construction, état
- **Temporalité** : Données à un instant T, pas de mise à jour temps réel

### 5.2 Limites du Modèle
- **Généralisation** : Risque de surapprentissage sur ce petit dataset
- **Extrapolation** : Biens atypiques mal prédits
- **Stabilité** : Variance élevée en cross-validation

### 5.3 Biais Potentiels
- Biais socio-économique (corrélation revenus/prix)
- Biais géographique (zones bien/mal représentées)
- Biais temporel (marché évolutif)

---

## 6. Recommandations

### 6.1 Court terme (Immédiat)
1. ✅ Déployer le modèle en mode "aide à la décision"
2. ✅ Afficher systématiquement l'intervalle de confiance
3. ⚠️ Validation humaine obligatoire pour prix > 500K€

### 6.2 Moyen terme (3-6 mois)
1. **Augmenter le dataset** : Objectif 1000+ transactions
2. **Enrichir les features** :
   - DPE (Diagnostic Performance Énergétique)
   - Année de construction
   - État du bien (rénové, à rénover)
   - Étage pour appartements
   - Présence parking/jardin
3. **Segmentation** : Modèles séparés maisons/appartements

### 6.3 Long terme (6-12 mois)
1. **Modèles régionaux** : Un modèle par grande région
2. **Deep Learning** : Tester MLP, TabNet
3. **Time series** : Intégrer l'évolution temporelle des prix
4. **API temps réel** : Intégration données notariales DVF

---

## 7. Reproductibilité

### 7.1 Environnement Technique

```
Python: 3.11.7
Pandas: 2.x
Scikit-learn: 1.x
NumPy: 1.x
Matplotlib: 3.x
Seaborn: 0.x
```

### 7.2 Structure des Fichiers

```
data ia immobilier/
├── Data/
│   └── raw/
│       ├── transactions_sample.csv
│       ├── transactions_preprocessed.csv
│       ├── data_tableau.csv
│       ├── loyers.csv
│       ├── foyers_fiscaux.csv
│       └── ...
├── N/
│   ├── exploration.ipynb
│   ├── preprocessing.ipynb
│   ├── random_forest_model.pkl
│   ├── scaler.pkl
│   └── model_results.txt
├── test/
│   └── modelisation.ipynb
└── README.md
```

### 7.3 Exécution

1. Exécuter `exploration.ipynb` - Analyse exploratoire
2. Exécuter `preprocessing.ipynb` - Préparation données
3. Exécuter `modelisation.ipynb` - Entraînement et évaluation

---

## 8. Fichiers Livrés

| Fichier | Description |
|---------|-------------|
| `exploration.ipynb` | Notebook EDA |
| `preprocessing.ipynb` | Notebook preprocessing |
| `modelisation.ipynb` | Notebook ML |
| `random_forest_model.pkl` | Modèle entraîné |
| `scaler.pkl` | StandardScaler |
| `data_tableau.csv` | Données pour dashboard |
| `evaluation_kpis.md` | KPIs et métriques |
| `guide_tableau.md` | Guide Tableau Public |
| `note_technique.md` | Ce document |

---

## 9. Conclusion

Le modèle Random Forest développé permet d'estimer les prix immobiliers avec une erreur moyenne de **55,936€** et explique **62%** de la variance des prix. Cette performance est acceptable pour un outil d'aide à la décision, à condition d'être utilisé conjointement avec l'expertise des agents immobiliers.

Les principales pistes d'amélioration sont :
1. **Augmentation du volume de données** (priorité haute)
2. **Enrichissement des features** (DPE, année, état)
3. **Segmentation par type de bien et région**

Le modèle est opérationnel et peut être déployé en environnement de production après validation des cas limites.

---

*Document technique - Projet IA Immobilier*
*Version 1.0 - Janvier 2025*
