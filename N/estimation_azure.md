# 💰 ESTIMATION DES COÛTS AZURE

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
- ✅ Coût très faible
- ✅ Auto-scaling
- ✅ Pas de gestion serveur
- ✅ Paiement à l'usage

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
- ✅ Performance stable
- ✅ Haute disponibilité (99.95%)
- ✅ Pipeline ML intégré
- ✅ Sécurité renforcée

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

🔗 Accéder à l'Azure Pricing Calculator :  
**https://azure.microsoft.com/fr-fr/pricing/calculator/**

Configuration suggérée :
1. Ajouter "Azure Functions" → Consumption Plan
2. Ajouter "Storage Account" → Blob Storage Standard
3. Ajouter "Azure Machine Learning" → Basic
4. Sélectionner région "France Centre"

---

## 6. Comparaison des Coûts

### 6.1 Tableau Récapitulatif

| Option | Coût/mois | Coût/an | Cas d'usage |
|--------|-----------|---------|-------------|
| **A. Minimale** | 25€ | 300€ | POC, tests |
| **B. Standard** | 130€ | 1,560€ | Production PME |
| **C. Enterprise** | 500€ | 6,000€ | Grande entreprise |

### 6.2 Évolution des Coûts avec la Charge

| Requêtes/jour | Option A | Option B | Option C |
|---------------|----------|----------|----------|
| 100 | 15€ | 110€ | 450€ |
| 1,000 | 25€ | 130€ | 450€ |
| 10,000 | 80€ | 200€ | 500€ |
| 100,000 | 300€ | 500€ | 550€ |

> 💡 **L'Option A devient plus chère que B au-delà de ~50,000 req/jour**

---

## 7. Coûts Cachés à Prévoir

### 7.1 Coûts Additionnels

| Poste | Estimation |
|-------|------------|
| Support Azure | 0€ (Basic) à 100€/mois (Standard) |
| Formation équipe | 500€ (one-time) |
| Développement initial | 2,000-5,000€ |
| Maintenance annuelle | 10-20% du coût initial |

### 7.2 Optimisations Possibles

| Action | Économie potentielle |
|--------|----------------------|
| Reserved Instances (1 an) | -30% |
| Reserved Instances (3 ans) | -50% |
| Azure Spot VMs (non-critique) | -60 à -90% |
| Compression données | -20% stockage |
| Mise en cache | -50% requêtes |

---

## 8. Recommandation

### 8.1 Phase de Lancement (0-6 mois)

**🎯 Recommandation : Option A (Minimale)**

- Budget : **~30€/mois**
- Suffisant pour 1,000 estimations/jour
- Permet de valider l'adoption

### 8.2 Phase de Croissance (6-12 mois)

**🎯 Recommandation : Option B (Standard)**

- Budget : **~150€/mois**
- Plus de fiabilité et monitoring
- Pipeline ML pour retraining automatique

### 8.3 Phase Scale (12+ mois)

**🎯 Recommandation : Option C (Enterprise)**

- Budget : **~500€/mois**
- Multi-région possible
- SLA 99.99%

---

## 9. Estimation Annuelle

### 9.1 Budget Prévisionnel

| Année | Option | Coût mensuel | Coût annuel | Notes |
|-------|--------|--------------|-------------|-------|
| 1 | A puis B | 30€ → 130€ | ~1,000€ | Montée progressive |
| 2 | B | 150€ | ~1,800€ | Production stable |
| 3 | B/C | 200€ | ~2,400€ | Évolution si besoin |

### 9.2 ROI Estimé

| Indicateur | Avant ML | Après ML | Gain |
|------------|----------|----------|------|
| Temps estimation | 30 min | 5 min | 83% |
| Coût/estimation | 25€ (agent) | 0.01€ (Azure) | 99.96% |
| Estimations/jour | 10 | 50+ | 400%+ |

**ROI = (Gain temps × Coût agent) - Coût Azure**

Exemple avec 30 estimations/jour :
- Économie temps : 30 × 25 min × 0.5€/min = 375€/jour
- Coût Azure : ~1€/jour
- **ROI quotidien : ~374€**

---

## 10. Ressources

### 10.1 Liens Utiles

- 📊 [Azure Pricing Calculator](https://azure.microsoft.com/fr-fr/pricing/calculator/)
- 📖 [Azure ML Pricing](https://azure.microsoft.com/fr-fr/pricing/details/machine-learning/)
- 📖 [Azure Functions Pricing](https://azure.microsoft.com/fr-fr/pricing/details/functions/)
- 📖 [Optimisation des coûts Azure](https://docs.microsoft.com/fr-fr/azure/cost-management-billing/)

### 10.2 Azure TCO Calculator

Pour une comparaison avec infrastructure on-premise :  
🔗 https://azure.microsoft.com/fr-fr/pricing/tco/calculator/

---

*Estimation réalisée avec les tarifs Azure France Centre - Janvier 2025*  
*Les prix peuvent varier selon les promotions et mises à jour Microsoft*
