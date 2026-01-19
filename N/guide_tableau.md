# 📊 Guide Tableau Public - Dashboard Immobilier

## 1. Données Préparées

Le fichier `data_tableau.csv` a été exporté avec les colonnes suivantes :

### Variables disponibles :

| Colonne | Description | Utilisation Tableau |
|---------|-------------|---------------------|
| `ville` | Nom de la ville | Dimension (labels) |
| `departement` | Code département | Dimension (filtre) |
| `region` | Région géographique | Dimension (filtre/couleur) |
| `type_batiment` | Maison/Appartement | Dimension (filtre/couleur) |
| `categorie_prix` | Tranche de prix | Dimension (filtre) |
| `prix` | Prix réel de vente | Mesure |
| `prix_predit` | Prix estimé par le modèle | Mesure |
| `erreur_pct` | Erreur en % | Mesure |
| `prix_m2` | Prix au m² réel | Mesure |
| `surface_habitable` | Surface en m² | Mesure |
| `n_pieces` | Nombre de pièces | Mesure/Dimension |
| `latitude` / `longitude` | Coordonnées GPS | Géographique |

---

## 2. Instructions pour Créer le Dashboard

### Étape 1 : Importer les données
1. Aller sur [Tableau Public](https://public.tableau.com/)
2. Se connecter ou créer un compte gratuit
3. Cliquer sur "Create a Viz"
4. Importer le fichier `data_tableau.csv`

### Étape 2 : Créer les visualisations recommandées

#### 📈 Viz 1 : Carte des prix par département
- Type : Carte (Map)
- Utiliser `latitude` et `longitude`
- Couleur : `prix_m2` (dégradé)
- Taille : `surface_habitable`
- Tooltip : ville, prix, type_batiment

#### 📊 Viz 2 : Prix réel vs Prix prédit
- Type : Scatter plot
- Axe X : `prix`
- Axe Y : `prix_predit`
- Ajouter ligne de référence y=x
- Couleur : `erreur_pct` (divergent)

#### 📊 Viz 3 : Distribution des prix par type
- Type : Box plot ou Histogramme
- Dimension : `type_batiment`
- Mesure : `prix`

#### 📊 Viz 4 : Prix moyen par région
- Type : Bar chart
- Dimension : `region`
- Mesure : AVG(`prix_m2`)
- Tri : Décroissant

#### 📊 Viz 5 : KPI Cards
- Créer des indicateurs :
  - Prix moyen
  - MAE du modèle : ~56K€
  - R² Score : 0.62
  - Nombre de transactions

### Étape 3 : Assembler le Dashboard
1. Créer un nouveau Dashboard
2. Taille recommandée : 1200 x 800 px
3. Disposition :
   ```
   +------------------------+
   |      KPI CARDS        |
   +------------------------+
   |  CARTE  |   SCATTER   |
   |         |    PLOT     |
   +------------------------+
   |  BAR    |  HISTOGRAM  |
   | CHART   |             |
   +------------------------+
   ```
4. Ajouter des filtres interactifs :
   - Région
   - Type de bien
   - Tranche de prix

### Étape 4 : Publier
1. Cliquer sur "Save to Tableau Public"
2. Nommer le workbook : "Dashboard Immobilier - Estimation Prix"
3. Copier le lien de partage

---

## 3. KPIs à Afficher

### KPIs Principaux
| KPI | Valeur | Description |
|-----|--------|-------------|
| 📊 Prix moyen | 208,840 € | Moyenne des transactions |
| 📏 Surface moyenne | 92 m² | Surface habitable moyenne |
| 🎯 MAE | 55,936 € | Erreur moyenne du modèle |
| 📈 R² Score | 62.1% | Précision du modèle |
| 🏠 Nb transactions | 100 | Volume de données |

### KPIs par Segment
- Prix moyen Maisons vs Appartements
- Prix/m² par région
- % d'erreur moyen par tranche de prix

---

## 4. Exemple de Story (Narrative)

### Page 1 : Vue d'ensemble du marché
- Carte avec tous les biens
- KPIs globaux

### Page 2 : Analyse par région
- Focus sur Île-de-France vs Province
- Comparaison des prix/m²

### Page 3 : Performance du modèle
- Scatter plot prédictions
- Distribution des erreurs

### Page 4 : Insights clés
- Top 3 features importantes
- Recommandations

---

## 5. Palette de Couleurs Recommandée

- **Bleu foncé** : #1f77b4 (KPIs, titres)
- **Bleu clair** : #aec7e8 (barres, fond)
- **Rouge** : #d62728 (erreurs négatives)
- **Vert** : #2ca02c (erreurs positives)
- **Gris** : #7f7f7f (neutres)

---

## 6. Checklist Finale

- [ ] Données importées correctement
- [ ] 5 visualisations créées
- [ ] Filtres interactifs fonctionnels
- [ ] Tooltips informatifs
- [ ] Titres et légendes clairs
- [ ] Dashboard responsive
- [ ] Publié sur Tableau Public
- [ ] Lien de partage copié

---

*Fichier : data_tableau.csv*
*Localisation : Data/raw/data_tableau.csv*
