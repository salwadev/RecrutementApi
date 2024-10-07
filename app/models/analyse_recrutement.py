from app import db
class AnalyseRecrutement:
    def __init__(self, historiqueCandidats, historiquePostes, modele):
        self.historiqueCandidats = historiqueCandidats  # List of Candidats
        self.historiquePostes = historiquePostes  # List of Postes
        self.modele = modele  # Instance of ModeleML

    def analyserCandidatures(self):
        """
        Analyser les candidatures via le modèle ML.
        Prend les informations des candidats historiques et analyse via le modèle ML.
        """
        candidats_data = [self._extraire_features_candidat(c) for c in self.historiqueCandidats]
        labels = [self._generer_label(c, p) for c, p in zip(self.historiqueCandidats, self.historiquePostes)]
        
        self.modele.entrainerModele(candidats_data, labels)
        
        resultats = []
        for candidat in self.historiqueCandidats:
            prediction = self.modele.predireCandidat(candidat)
            resultats.append({
                "candidat": candidat.nom,
                "prediction": prediction
            })
        return resultats

    def optimiserProcessus(self):
        """
        Optimiser le processus de recrutement en fonction des prédictions.
        Exemple : on peut suggérer d'accorder plus d'importance aux candidats ayant certaines compétences ou expérience.
        """
        # Basé sur les prédictions, ajuster la pondération des critères dans le processus
        suggestions = []
        for candidat in self.historiqueCandidats:
            prediction = self.modele.predireCandidat(candidat)
            if prediction > 0.8:  # Exemple de seuil
                suggestions.append(f"Suggérer {candidat.nom} pour un entretien immédiat.")
        return suggestions

    def _extraire_features_candidat(self, candidat):
        """
        Extraire les caractéristiques du candidat à utiliser pour l'analyse ML.
        """
        return [candidat.experience, len(candidat.competences)]  # Exemple simplifié

    def _generer_label(self, candidat, poste):
        """
        Générer un label pour la classification.
        Par exemple, si le candidat a été embauché pour le poste ou non.
        """
        # Suppose we return 1 if the candidate was hired, 0 otherwise (example logic)
        return 1 if candidat.categorie == "Sérieux" else 0
