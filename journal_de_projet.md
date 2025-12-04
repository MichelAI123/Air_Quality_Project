## Journal de Projet - Déploiement IA

**Date :** 25 Novembre 2025
**Auteur :** Michel DONGMO

## Contexte

Aider les villes a predire la qualité de l'air en se basant sur les anciennes données 

## Objectif

Préparer et containeriser l'API de prédiction pour un déploiement public et vérifier le fonctionnement local.

## Choix Techniques

- **Modèle :** Random Forest (choisi pour son F1-score de 0.8284165091158822).
- **API :** FastAPI choisi pour sa rapidité et sa documentation automatique.
- **Conteneurisation :** Docker utilisé pour garantir la portabilité.

## Étapes réalisées

1. Export du modèle depuis le notebook.
2. Création de l'API FastAPI (`app.py`) exposant `/health` et `/predict`.
3. Ajout des dépendances dans `requirements.txt`.
4. Ajout du modèle `model/best_model.pkl`.
5. Rédaction du Dockerfile et .dockerignore.
6. Tests locaux via `uvicorn` et `curl`.
7. Construction et exécution de l'image Docker, tests via `docker ps` et `curl`.
8. Réalisation des captures d'écran et génération du PDF.

## Choix techniques

- FastAPI / Uvicorn pour performance et docs automatiques
- Pickle / joblib pour sérialisation; ONNX possible pour portabilité
- Image basée sur `python:3.11-slim`

## Problèmes rencontrés

- Erreur lors du décodage des variables encodées par fréquence
- Erreur de désérialisation XGBoost -> solution: re-sérialiser avec joblib ou exporter en ONNX.
- Durée d'optimisation très longue à cause des variétés des hyperparamètres

## Tests effectués

- GET /health -> ok
- POST /predict -> pas ok

## Conclusion & recommandations

Convertir en ONNX pour portabilité 

Ajouter tests unitaires, CI/CD)
