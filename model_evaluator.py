import pandas as pd
from sklearn.metrics import mean_squared_error, r2_score
import tkinter as tk
from tkinter import ttk


class ModelEvaluator:
    def __init__(self, model):
        self.model = model

    def evaluate(self, X_test, y_test):
        # 1. Tahminleri yap
        y_pred = self.model.predict(X_test)
        mse = mean_squared_error(y_test, y_pred)
        r2 = r2_score(y_test, y_pred)

        # 2. Ekrana sığması için ilk 30 evi örnek olarak al ve tabloyu (DataFrame) hazırla
        df = pd.DataFrame({
            'Gerçek Fiyat': y_test.values[:30] * 100000,
            'Tahmin Edilen': y_pred[:30] * 100000
        })

        df['Hata Miktarı'] = abs(df['Gerçek Fiyat'] - df['Tahmin Edilen'])
        df['Hata Oranı'] = (df['Hata Miktarı'] / df['Gerçek Fiyat']) * 100

        # Sayıları Dolar ve Yüzde formatına çevirerek şıklaştır
        df['Gerçek Fiyat'] = df['Gerçek Fiyat'].apply(lambda x: f"${x:,.0f}")
        df['Tahmin Edilen'] = df['Tahmin Edilen'].apply(lambda x: f"${x:,.0f}")
        df['Hata Miktarı'] = df['Hata Miktarı'].apply(lambda x: f"${x:,.0f}")
        df['Hata Oranı'] = df['Hata Oranı'].apply(lambda x: f"%{x:.2f}")

        # 3. Masaüstü Penceresini (Arayüzü) Oluştur
        root = tk.Tk()
        root.title("Ev Fiyat Tahmin Sonuçları")
        root.geometry("850x550")
        root.configure(bg="#f8f9fa")

        # Başlık ve Model Puanları
        baslik = tk.Label(root, text="GERÇEK VS TAHMİN KARŞILAŞTIRMASI", font=('Arial', 14, 'bold'), bg="#f8f9fa")
        baslik.pack(pady=(20, 5))

        skor = tk.Label(root, text=f"Ortalama Karesel Hata (MSE): {mse:.4f}   |   R-kare (R2) Skoru: {r2:.4f}",
                        font=('Arial', 11, 'bold'), fg="#2c3e50", bg="#f8f9fa")
        skor.pack(pady=(0, 20))

        # Tablo Stili
        style = ttk.Style()
        style.theme_use("clam")
        style.configure("Treeview.Heading", font=('Arial', 10, 'bold'), background="#2c3e50", foreground="white")
        style.configure("Treeview", font=('Arial', 10), rowheight=25)

        # 4. Tabloyu Ekrana Çizdir
        tree = ttk.Treeview(root, columns=list(df.columns), show='headings', height=15)

        for col in df.columns:
            tree.heading(col, text=col)
            tree.column(col, anchor="center")

        for index, row in df.iterrows():
            tree.insert("", "end", values=list(row))

        tree.pack(fill='both', expand=True, padx=20, pady=(0, 20))

        # Pencereyi ekranda tut
        root.mainloop()