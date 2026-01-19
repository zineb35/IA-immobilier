# 📋 CONFORMITÉ LÉGALE - RGPD & IA

## Document de Conformité - Projet IA Immobilier

**Date** : Janvier 2025  
**Version** : 1.0  
**Responsable** : [Nom du responsable de traitement]

---

## 1. Analyse des Données Personnelles

### 1.1 Inventaire des Données Traitées

| Donnée | Type | Sensibilité | Finalité |
|--------|------|-------------|----------|
| Adresse du bien | Localisation | Modérée | Géolocalisation |
| Ville | Localisation | Faible | Agrégation |
| Département | Localisation | Faible | Statistiques |
| Latitude/Longitude | GPS | Modérée | Mapping |
| Prix de vente | Financier | Modérée | Prédiction |
| Revenus fiscaux moyens | Statistique | Faible | Enrichissement (agrégé) |

### 1.2 Catégorisation RGPD

**Données à caractère personnel identifiées** :
- ✅ Adresses précises des biens
- ✅ Coordonnées GPS (peuvent identifier un lieu précis)

**Données NON personnelles** :
- Prix agrégés par zone
- Statistiques départementales
- Type de bien (maison/appartement)

### 1.3 Source des Données

| Source | Base légale | Vérification |
|--------|-------------|--------------|
| DVF (Demandes de Valeurs Foncières) | Données publiques (Open Data) | ✅ Légal |
| INSEE (revenus fiscaux) | Données statistiques agrégées | ✅ Légal |
| Loyers (CLAMEUR/INSEE) | Données statistiques agrégées | ✅ Légal |

---

## 2. Base Légale du Traitement

### 2.1 Fondement Juridique

Le traitement repose sur **l'intérêt légitime** (Article 6.1.f RGPD) :
- Amélioration des services d'estimation immobilière
- Aide à la décision pour les agents
- Pas de collecte de données sensibles

### 2.2 Données Publiques

Les données DVF sont **ouvertes** et rendues publiques par l'État français depuis 2019.  
Source : [data.gouv.fr](https://www.data.gouv.fr/fr/datasets/demandes-de-valeurs-foncieres/)

> **Article L112-3 du Code des relations entre le public et l'administration** :  
> Les données publiques sont librement réutilisables.

---

## 3. Mesures de Protection

### 3.1 Pseudonymisation Appliquée

| Donnée d'origine | Traitement | Donnée conservée |
|------------------|------------|------------------|
| Adresse complète | Supprimée | Non conservée |
| Nom vendeur/acheteur | Non collecté | N/A |
| Référence cadastrale | Supprimée | Non conservée |
| Coordonnées GPS | Conservées (précision réduite) | 5 décimales max |

### 3.2 Minimisation des Données

Seules les données **strictement nécessaires** sont conservées :
- Surface, nombre de pièces, type de bien
- Localisation agrégée (ville, département)
- Prix de transaction

### 3.3 Sécurité des Données

| Mesure | Implémentation |
|--------|----------------|
| Chiffrement stockage | AES-256 (recommandé) |
| Accès restreint | Authentification requise |
| Logs d'accès | Traçabilité des consultations |
| Sauvegarde | Backup chiffrés |

---

## 4. Droits des Personnes

### 4.1 Applicabilité

⚠️ **Important** : Les données DVF étant des données publiques anonymisées, les droits RGPD individuels sont **limités**.

Cependant, en cas de demande :

| Droit | Applicable | Procédure |
|-------|------------|-----------|
| Accès | ⚠️ Limité | Redirection vers data.gouv.fr |
| Rectification | ❌ Non | Données publiques officielles |
| Effacement | ❌ Non | Données publiques |
| Opposition | ⚠️ Limité | Analyse au cas par cas |
| Portabilité | ❌ Non | Données non collectées directement |

### 4.2 Contact DPO

Pour toute question relative à la protection des données :  
📧 Email : [dpo@entreprise.fr]  
📍 Adresse : [Adresse postale]

---

## 5. Transparence Algorithmique

### 5.1 Obligation d'Explication (IA Act)

Conformément au futur **AI Act européen**, le modèle doit être :

| Exigence | Conformité | Preuve |
|----------|------------|--------|
| Explicable | ✅ | Feature importance fournie |
| Auditable | ✅ | Code source documenté |
| Non discriminant | ✅ | Pas de données sensibles |
| Réversible | ✅ | Décision humaine finale |

### 5.2 Catégorie de Risque (AI Act)

Selon la classification AI Act :
- **Risque** : LIMITÉ (outil d'aide à la décision)
- **Usage** : Estimation immobilière (non critique)
- **Décision finale** : Humaine (agent immobilier)

### 5.3 Information des Utilisateurs

Les agents utilisant l'outil doivent être informés que :
1. Le prix affiché est une **estimation** algorithmique
2. L'estimation peut contenir une **marge d'erreur** (~56K€)
3. La **décision finale** reste humaine

---

## 6. Registre des Traitements

### 6.1 Fiche de Traitement

| Champ | Information |
|-------|-------------|
| **Nom du traitement** | Estimation prix immobiliers ML |
| **Responsable** | [Nom entreprise] |
| **Finalité** | Aide à l'estimation des biens |
| **Base légale** | Intérêt légitime |
| **Catégories de données** | Données immobilières publiques |
| **Destinataires** | Agents immobiliers internes |
| **Transferts hors UE** | Non |
| **Durée de conservation** | 3 ans (données anonymisées) |
| **Mesures de sécurité** | Chiffrement, accès restreint |

### 6.2 AIPD (Analyse d'Impact)

Une **Analyse d'Impact relative à la Protection des Données** est **NON REQUISE** car :
- Les données sont publiques et anonymisées
- Le traitement n'est pas à grande échelle
- Pas de profilage individuel
- Pas de décision automatisée impactante

---

## 7. Checklist de Conformité

### 7.1 Avant Déploiement

- [x] Vérification de la source des données (publiques/légales)
- [x] Pseudonymisation des données sensibles
- [x] Documentation du modèle (explicabilité)
- [x] Définition de la base légale
- [x] Rédaction de la fiche registre
- [ ] Nomination d'un DPO (si > 250 employés)
- [ ] Formation des utilisateurs

### 7.2 En Production

- [ ] Logs d'accès activés
- [ ] Politique de rétention définie
- [ ] Procédure de réponse aux demandes
- [ ] Audit annuel planifié
- [ ] Mise à jour documentation si évolution

---

## 8. Recommandations

### 8.1 Actions Prioritaires

1. **Nommer un référent RGPD** si non existant
2. **Informer les utilisateurs** (agents) de la nature algorithmique
3. **Documenter les versions** du modèle pour traçabilité
4. **Supprimer** les adresses précises du dataset final

### 8.2 Améliorations Futures

1. Intégrer un **mécanisme d'opt-out** pour les propriétaires
2. Mettre en place un **audit de biais** régulier
3. Créer une **page de transparence** publique sur le modèle

---

## 9. Références Réglementaires

- **RGPD** : Règlement (UE) 2016/679
- **Loi Informatique et Libertés** : Loi n°78-17 modifiée
- **AI Act** : Proposition de règlement COM/2021/206 (en cours)
- **Open Data** : Directive (UE) 2019/1024

---

## 10. Signatures

| Rôle | Nom | Date | Signature |
|------|-----|------|-----------|
| Data Scientist | | | |
| DPO | | | |
| Responsable métier | | | |

---

*Document de conformité RGPD - Projet IA Immobilier*  
*Version 1.0 - Janvier 2025*
