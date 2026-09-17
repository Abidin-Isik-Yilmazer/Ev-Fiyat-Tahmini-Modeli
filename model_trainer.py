from sklearn.ensemble import RandomForestRegressor

class ModelTrainer:
    def __init__(self):
        # n_estimators=100: Modelin 100 farklı karar ağacı üreterek ortak bir tahmin yapmasını sağlar
        self.model = RandomForestRegressor(n_estimators=100, random_state=42)

    def train(self, X_train, y_train):
        self.model.fit(X_train, y_train)
        return self.model