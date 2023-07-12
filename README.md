# Döviz Kuru Tahmini
Bu Python kodu, ARIMA (Otomatik Regresyon Entegre Hareketli Ortalama) modelini kullanarak gelecekteki döviz kuru tahminleri yapmak için kullanılır. Kod, verileri bir CSV dosyasından okur, ARIMA modelini eğitir ve belirli bir tarih için döviz kuru tahmini yapar.

## Gereksinimler
Bu kodun çalışması için aşağıdaki Python kütüphanelerini yüklemeniz gerekmektedir:
<pre>
pandas
statsmodels
</pre>
Bu kütüphaneleri aşağıdaki komutla yükleyebilirsiniz:

<pre> 
  pip install pandas statsmodels
</pre>

## Kullanım
Döviz kuru verilerini içeren bir CSV dosyasını doviz_kuru_ver.csv olarak kaydedin.

Yukarıdaki gereksinimleri yükleyin.

Verilerinizi pd.read_csv fonksiyonu ile okuyun ve Tarih sütununu indeks olarak ayarlayın.
ARIMA modelini oluşturmak için ARIMA sınıfını kullanın. Modelin order parametresini isteğe bağlı olarak ayarlayabilirsiniz. Örneğin, (1, 1, 1) değeri kullanılmıştır.

Modeli eğitmek için fit yöntemini kullanın.

Tahmin yapmak istediğiniz gelecek tarihi belirleyin ve pd.to_datetime fonksiyonuyla uygun formata dönüştürün.

Veri çerçevesini genişletmek için reindex yöntemini kullanın.

Genişletilmiş veri çerçevesiyle yeni bir ARIMA modeli oluşturun ve bu modeli eğitin.

Gelecekteki döviz kuru tahminini yapmak için get_forecast yöntemini kullanın. steps parametresi ile tahmin yapmak istediğiniz adım sayısını belirtin.

Tahmin sonucunu almak için predicted_mean özelliğini kullanın.

Son olarak, tahmin edilen döviz kuru değerini ekrana yazdırın.
