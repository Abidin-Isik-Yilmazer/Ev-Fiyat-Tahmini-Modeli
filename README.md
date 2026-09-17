# 🏡 Ev Fiyat Tahmini Modeli

Bu proje, California Housing veri setini kullanarak ev özelliklerine (oda sayısı, evin yaşı, bölge geliri vb.) göre ev fiyatlarını tahmin eden bir makine öğrenmesi modelidir. Proje, Nesne Yönelimli Programlama (OOP) mimarisiyle modüler olarak tasarlanmış olup, tahmin sonuçlarını düz bir terminal çıktısı yerine masaüstü arayüzü (GUI) ile kullanıcıya sunmaktadır.

## 🛠️ Kullanılan Teknolojiler ve Kütüphaneler

* **Dil:** Python
* **Makine Öğrenmesi:** Scikit-learn (Random Forest Regressor)
* **Veri İşleme:** Pandas
* **Masaüstü Arayüzü (GUI):** Tkinter

## 🚀 Proje Özellikleri

* **Algoritma:** Doğrusal Regresyon'a kıyasla karmaşık örüntüleri çok daha iyi yakalayan **Rastgele Orman (Random Forest Regressor)** algoritması kullanılmıştır.
* **Mimari (OOP):** Proje, "Tek Sorumluluk Prensibi"ne uygun olarak veri yükleme, model eğitimi ve model değerlendirme işlemlerini ayrı Python dosyalarına (`data_loader.py`, `model_trainer.py`, `model_evaluator.py` ve ana yönetici `main.py`) bölerek yöneten temiz bir yapıya sahiptir.
* **Kullanıcı Arayüzü:** `tkinter` kütüphanesi kullanılarak oluşturulan masaüstü penceresi; Ortalama Karesel Hata (MSE) ve R2 skorunu gösterirken, aynı zamanda gerçek fiyatları, tahmin edilen fiyatları, sapma miktarını ve yüzde bazında hata oranını listeleyen bir tablo sunar.

---

## ⚙️ Kurulum ve Çalıştırma

**1. Projeyi Klonlayın:**
```bash
git clone [https://github.com/Abidin-Isik-Yilmazer/Ev-Fiyat-Tahmini-Modeli.git](https://github.com/Abidin-Isik-Yilmazer/Ev-Fiyat-Tahmini-Modeli.git)
```

**2. Proje Klasörüne Girin:**
```bash
cd Ev-Fiyat-Tahmini-Modeli
```

**3. Gerekli Kütüphaneleri Yükleyin:**
```bash
pip install pandas scikit-learn
```

**4. Uygulamayı Başlatın (Arayüzü Açın):**
```bash
python main.py
```
