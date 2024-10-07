from app import db
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score

class ModeleML(db.Model):
    __tablename__ = 'modele_ml'
    
    idModele = db.Column(db.Integer, primary_key=True)
    nomModele = db.Column(db.String(100), nullable=False)
    typeModele = db.Column(db.String(50), nullable=False)  # Classification ou Régression
    parametres = db.Column(db.PickleType, nullable=False)  # Stocke les paramètres du modèle sous forme de dict
    precision = db.Column(db.Float, nullable=True)

    def entrainerModele(self, data, labels):
        """
        Entraîner le modèle avec les données des candidats.
        data: DataFrame contenant les données de formation.
        labels: Labels correspondant aux données (classification binaire ou autre).
        """
        X_train, X_test, y_train, y_test = train_test_split(data, labels, test_size=0.2, random_state=42)
        
        # Exemple d'entraînement d'un modèle de classification (SVM, par exemple)
        if self.typeModele == 'Classification':
            from sklearn.svm import SVC
            model = SVC(**self.parametres)
        elif self.typeModele == 'Régression':
            from sklearn.linear_model import LinearRegression
            model = LinearRegression(**self.parametres)
        else:
            raise ValueError("Type de modèle non supporté.")

        model.fit(X_train, y_train)
        predictions = model.predict(X_test)
        
        # Calcul de la précision
        if self.typeModele == 'Classification':
            self.precision = accuracy_score(y_test, predictions)
        elif self.typeModele == 'Régression':
            from sklearn.metrics import mean_squared_error
            self.precision = mean_squared_error(y_test, predictions, squared=False)

        db.session.commit()

    def predireCandidat(self, candidat):
        """
        Prédire si un candidat est un bon fit pour le poste.
        """
        # Extraire les données du candidat
        candidat_data = self._extraire_features_candidat(candidat)
        
        # Charger et appliquer le modèle
        if self.typeModele == 'Classification':
            # Exemple avec un modèle SVM
            from sklearn.svm import SVC
            model = SVC(**self.parametres)
        else:
            # Exemple avec un modèle de régression
            from sklearn.linear_model import LinearRegression
            model = LinearRegression(**self.parametres)
        
        prediction = model.predict([candidat_data])
        return prediction

    def evaluerModele(self):
        """
        Retourne la précision ou les performances actuelles du modèle.
        """
        return self.precision

    def _extraire_features_candidat(self, candidat):
        # Simulate feature extraction from a candidate
        return [candidat.experience, len(candidat.competences)]  # Simplified example
