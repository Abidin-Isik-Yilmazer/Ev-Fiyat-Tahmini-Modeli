from data_loader import DataLoader
from model_trainer import ModelTrainer
from model_evaluator import ModelEvaluator

if __name__ == "__main__":
    # 1. Veriyi getir
    loader = DataLoader()
    X_train, X_test, y_train, y_test = loader.get_train_test_data()
    print("Veri hazırlığı tamamlandı.")

    # 2. Modeli eğit
    trainer = ModelTrainer()
    trained_model = trainer.train(X_train, y_train)
    print("Model başarıyla eğitildi.")

    # 3. Modeli değerlendir
    evaluator = ModelEvaluator(trained_model)
    evaluator.evaluate(X_test, y_test)