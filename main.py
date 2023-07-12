import pandas as pd
from statsmodels.tsa.arima.model import ARIMA

# Döviz kuru verilerini yükleyin (Örnek olarak CSV dosyasından okuyoruz)
data = pd.read_csv('doviz_kuru_ver.csv')

# Tarih sütununu indeks olarak ayarlayın
data['Tarih'] = pd.to_datetime(data['Tarih'], format='%Y-%m-%d')
data.set_index('Tarih', inplace=True)

# Veri çerçevesinin indeksini sınırlayın
start_date = data.index.min()
end_date = data.index.max()
new_index = pd.date_range(start=start_date, end=end_date, freq='D')
data = data.reindex(new_index)

# ARIMA modelini oluşturun
model = ARIMA(data, order=(1, 1, 1))  # Örnek olarak (p, d, q) = (1, 1, 1)

# Modeli eğitin
model_fit = model.fit()

# Gelecekteki döviz kuru tahminini yapın
future_date = pd.to_datetime('2023-07-15')  # Tahmin yapmak istediğiniz tarih

# Veri çerçevesini genişletin
data_extended = data.reindex(data.index.union(pd.Index([future_date])))

# Modeli yeniden eğitin
model_extended = ARIMA(data_extended, order=(1, 1, 1))
model_fit_extended = model_extended.fit()

# Gelecekteki döviz kuru tahminini yapın
forecast = model_fit_extended.get_forecast(steps=1)

# Tahmin sonucunu alın
predicted_value = forecast.predicted_mean.iloc[-1]

print(f"On {future_date.date()}, the predicted exchange rate is {predicted_value:.2f}.")
