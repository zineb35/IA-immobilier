# ESTIMATION DES COÛTS AZURE

## Déploiement du Modèle ML Immobilier

**Date d'estimation** : Janvier 2025  
**Région** : France Centre (francecentral)  
**Devise** : EUR (€)

---

## 1. Architecture Proposée

### 1.1 Schéma de Déploiement

```
                    ┌─────────────────────────────────────────────┐
                    │                  AZURE                       │
┌──────────┐        │  ┌───────────────┐    ┌──────────────────┐  │
│  Client  │───────►│  │   API Gateway │───►│  Azure Functions │  │
│ (Agent)  │        │  │  (App Service)│    │   (Inference)    │  │
└──────────┘        │  └───────────────┘    └────────┬─────────┘  │
                    │                                 │            │
                    │         ┌───────────────────────┴──────┐     │
                    │         │                              │     │
                    │         ▼                              ▼     │
                    │  ┌──────────────┐         ┌────────────────┐│
                    │  │ Blob Storage │         │ Azure ML Studio││
                    │  │   (Model)    │         │  (Retraining)  ││
                    │  └──────────────┘         └────────────────┘│
                    └─────────────────────────────────────────────┘
```

### 1.2 Options de Déploiement

| Option | Description | Complexité | Coût |
|--------|-------------|------------|------|
| **A. Minimale** | Azure Functions + Storage | Faible | ~30€/mois |
| **B. Standard** | App Service + Azure ML | Moyenne | ~150€/mois |
| **C. Enterprise** | AKS + Azure ML + Monitoring | Élevée | ~500€/mois |

---

## 2. Option A : Déploiement Minimal (Recommandé pour démarrer)

### 2.1 Composants

| Service | Tier | Spécifications | Coût/mois |
|---------|------|----------------|-----------|
| **Azure Functions** | Consumption | 1M requêtes gratuites | ~5€ |
| **Azure Blob Storage** | Standard | 10 GB (modèle + données) | ~2€ |
| **Azure API Management** | Consumption | 1M calls | ~3€ |
| **Application Insights** | Basic | Monitoring | ~5€ |

### 2.2 Estimation Mensuelle

| Poste | Calcul | Coût |
|-------|--------|------|
| Functions (1000 req/jour) | 30K req/mois × 0.000016€ | ~0.50€ |
| Exécution Functions | 30K × 500ms × 128MB | ~5€ |
| Stockage | 5 GB × 0.0184€/GB | ~0.10€ |
| Bande passante | 10 GB sortant | ~0.90€ |
| Monitoring | Basic tier | ~10€ |

**Total Option A : ~20-30 €/mois**

### 2.3 Avantages
- Coût très faible
- Auto-scaling
- Pas de gestion serveur
- Paiement à l'usage

---

## 3. Option B : Déploiement Standard (Production)

### 3.1 Composants

| Service | Tier | Spécifications | Coût/mois |
|---------|------|----------------|-----------|
| **Azure App Service** | B1 | 1 core, 1.75 GB RAM | ~50€ |
| **Azure Machine Learning** | Basic | Workspace | ~0€ (pay-per-use) |
| **Azure Blob Storage** | Standard | 50 GB | ~10€ |
| **Azure SQL Database** | Basic | 2 GB | ~5€ |
| **Application Insights** | Standard | Monitoring avancé | ~20€ |
| **Azure Key Vault** | Standard | Secrets | ~3€ |

### 3.2 Estimation Mensuelle

| Poste | Calcul | Coût |
|-------|--------|------|
| App Service B1 | 24/7 | ~50€ |
| ML Compute (retrain) | 10h × DS1_v2 | ~15€ |
| Stockage | 50 GB | ~10€ |
| Base de données | Basic 2 GB | ~5€ |
| Monitoring | 10 GB logs | ~20€ |
| Key Vault | 10K opérations | ~3€ |
| Réseau | 50 GB sortant | ~5€ |

**Total Option B : ~110-150 €/mois**

### 3.3 Avantages
- Performance stable
- Haute disponibilité (99.95%)
- Pipeline ML intégré
- Sécurité renforcée

---

## 4. Option C : Déploiement Enterprise (Scalabilité)

### 4.1 Composants

| Service | Tier | Spécifications | Coût/mois |
|---------|------|----------------|-----------|
| **Azure Kubernetes (AKS)** | Standard | 2 nodes DS2_v2 | ~200€ |
| **Azure ML** | Enterprise | Workspace complet | ~100€ |
| **Azure Cosmos DB** | Provisioned | 10K RU/s | ~80€ |
| **Azure Front Door** | Standard | CDN + WAF | ~50€ |
| **Azure Monitor** | Full | Logs + Metrics | ~50€ |
| **Azure DevOps** | Basic | CI/CD | ~20€ |

### 4.2 Estimation Mensuelle

**Total Option C : ~450-600 €/mois**

---

## 5. Calcul Détaillé - Azure Pricing Calculator

### 5.1 Hypothèses de Calcul

| Paramètre | Valeur |
|-----------|--------|
| Région | France Centre |
| Requêtes/jour | 1,000 |
| Requêtes/mois | 30,000 |
| Taille modèle | 50 MB |
| Temps inférence | 500 ms |
| Retraining | 1x/semaine |

### 5.2 Liens Azure Calculator

Accéder à l'Azure Pricing Calculator :  
**https://azure.microsoft.com/fr-fr/pricing/calculator/**

Configuration suggérée :
1. Ajouter "Azure Functions" - Consumption Plan
2. Ajouter "Storage Account" - Blob Storage Standard
3. Ajouter "Azure Machine Learning" - Basic
4. Sélectionner région "France Centre"

---

## 6. Comparaison des Options

| Critère | Option A | Option B | Option C |
|---------|----------|----------|----------|
| **Coût mensuel** | ~30€ | ~150€ | ~500€ |
| **Scalabilité** | Auto | Manuelle | Auto |
| **Disponibilité** | 99.9% | 99.95% | 99.99% |
| **Complexité** | Faible | Moyenne | Élevée |
| **MLOps** | Non | Basique | Complet |
| **Cas d'usage** | POC/Test | Production PME | Enterprise |

---

## 7. Recommandation

### Pour ce projet (POC/Démarrage)

**Option A recommandée** : ~30€/mois

Raisons :
- Dataset petit (100 observations)
- Volume de requêtes faible attendu
- Phase de validation du modèle
- Budget limité

### Évolution future

```
POC (Option A) → Validation → Production (Option B) → Scale (Option C)
     30€/mois                      150€/mois              500€/mois
```

---

## 8. Coûts Cachés à Prévoir

| Poste | Estimation |
|-------|------------|
| Transfert de données | ~5€/mois |
| Support Azure | 0€ (Basic) à 100€ (Standard) |
| Certificats SSL | Inclus App Service |
| Backup | ~5€/mois |
| Tests/Dev | +20% du coût prod |

---

## 9. Optimisations Possibles

1. **Reserved Instances** : -30% sur App Service (1 an)
2. **Spot VMs** : -80% pour retraining (interruptible)
3. **Auto-shutdown** : Environnements de dev
4. **Tier gratuit** : Exploiter les quotas gratuits

---

## 10. Récapitulatif

| Budget | Option | Services |
|--------|--------|----------|
| < 50€/mois | A - Minimal | Functions + Storage |
| 100-200€/mois | B - Standard | App Service + ML |
| > 400€/mois | C - Enterprise | AKS + ML complet |

---

*Estimation Azure - Projet IA Immobilier*  
*Version 1.0 - Janvier 2025*
