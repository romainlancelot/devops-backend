# Les éléments évalués lors de la soutenance

## Minimum attendu (Pour avoir genre 11 quoi)

- [x] Avoir un projet en ligne sur Github/Gitlab/Autre chose
- [x] Utiliser des conteneurs
- [x] Avoir une pipeline automatique qui se lance à chaque commit de la branche main
- [x] La pipeline doit avoir au minimum les étapes suivantes :
  - [x] Des test unitaires
  - [x] Un build du projet
  - [x] Une mise en ligne du livrable (Sur dockerhub par exemple)
- [x] La pipeline doit s’arrêter si une des étapes échoue.
- [x] Déployer sur Kubernetes (Même si c’est fait à la main, c’est ok)
- [x] Pouvoir faire une démonstration de bout en bout allant d’un commit sur le projet au déploiement de ce commit.
- [x] Pouvoir faire une démonstration d’une pipeline qui échoue si jamais une des étapes ne passe pas.

## Exemples d’éléments supplémentaires qui seront pris en compte (Sans ordre de priorité)

### Les trucs pas trop durs

- [x] Mise en place d’un linter dans une pipeline automatique
- [x] Mise en place d’une pipeline pour des merge request/pull request
- [ ] Mise en place d’une pipeline pour déployer des release github/gitlab (Pipeline sur des tags)
- [x] Calculer et afficher le coverage des tests unitaires dans les merge/pull requests
- [x] Avoir une pipeline pour déployer le projet sur Kubernetes, la pipeline peut être lancée manuellement
- [x] Déploiement sur Kubernetes avec Helm

### Les trucs un peu plus longs

- [ ] Mise en place d’un outil de qualité de code (SonarCloud, Code Climate) dans une pipeline automatique
- [ ] Afficher le rapport de qualité de code dans une merge/pull request et bloquer la validation si la qualité descend en dessous d’un seuil
- [ ] Mise en place de tests automatiques supplémentaires (Tests e2e, tests de montée en charge) dans une pipeline automatique
- [ ] Mettre en place un repository GitOps https://github.com/weaveworks/awesome-gitops
- [x] Créer un outil qui va communiquer avec l’api gitlab/github pour déployer votre projet (backend et frontend). Il peut s’agir d’un chatbot discord/slack, d’un outil en ligne de commande, d’une petite api avec une interface web simple.
- [x] Ajouter une route de healthcheck sur votre backend pour vérifier l’état après un déploiement
- [x] Ajouter une pipeline qui va utiliser la route de healthcheck pour confirmer que le déploiement est correct
- [ ] Mise en place d’outils de monitoring (Prometheus)
- [ ] Mise en place d’outils de gestion des logs (Elasticsearch)
- [ ] Création d’environnements à la volée (Pouvoir mettre en ligne un nouvel environnement avec une pipeline)
