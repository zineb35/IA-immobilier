# NOTE MÉTHODOLOGIQUE
## Projet IA Immobilier

---

**Projet** : Estimation des prix immobiliers par Machine Learning  
**Date** : Janvier 2025

---

## 1. OBJECTIF

Développer un modèle prédictif pour estimer automatiquement le prix des biens immobiliers en France.

## 2. DONNÉES

- **Source** : Kaggle (données DVF publiques)
- **Volume** : 100 transactions immobilières
- **Variables** : surface, nombre de pièces, type de bien, localisation, loyer local, revenu fiscal

## 3. MÉTHODOLOGIE

1. **Exploration** : Analyse statistique des données
2. **Prétraitement** : Nettoyage et enrichissement avec données externes
3. **Modélisation** : Test de 2 algorithmes (Régression Linéaire, Random Forest)
4. **Évaluation** : Métriques MAE, RMSE, R²

## 4. RÉSULTATS

| Modèle | MAE | R² |
|--------|-----|-----|
| Régression Linéaire | 65,754 € | 0.51 |
| **Random Forest** | **55,936 €** | **0.62** |

Le modèle Random Forest a été retenu car il offre les meilleures performances.

## 5. LIMITES

- Dataset de taille limitée (100 observations)
- Absence de certaines features (DPE, année construction)

## 6. CONCLUSION

Le modèle atteint un R² de 0.62, ce qui est satisfaisant pour un projet exploratoire.

---
