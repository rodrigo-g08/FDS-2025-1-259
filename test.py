import pandas as pd
import numpy as np
from sklearn.ensemble import RandomForestRegressor
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
from sklearn.metrics import mean_squared_error, r2_score

# --- 1. Cargar y preparar datos ---
df = pd.read_csv('dataset_completo_con_ratios.csv')  # Reemplaza con tu ruta

# Convertir publish_time a datetime
df['publish_time'] = pd.to_datetime(df['publish_time'])

# Extraer features temporales
df['publish_hour'] = df['publish_time'].dt.hour
df['publish_day'] = df['publish_time'].dt.dayofweek

# Codificar channel_title
le_channel = LabelEncoder()
df['channel_title'] = le_channel.fit_transform(df['channel_title'])

# Convertir booleanos a enteros
bool_cols = ['comments_disabled', 'ratings_disabled', 'video_error_or_removed']
df[bool_cols] = df[bool_cols].astype(int)

# --- 2. Seleccionar variables para el modelo ---
features = [
    'category_id', 'comment_count', 'comments_disabled',
    'ratings_disabled', 'video_error_or_removed',
    'publish_hour', 'publish_day', 'channel_title'
]

X = df[features]
y = df['views']  # Cambia a 'likes' o 'dislikes' si lo deseas

# --- 3. Dividir en entrenamiento y prueba ---
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# --- 4. Entrenar modelo ---
model = RandomForestRegressor(n_estimators=100, random_state=42)
model.fit(X_train, y_train)

# --- 5. Evaluar modelo ---
y_pred = model.predict(X_test)
rmse = np.sqrt(mean_squared_error(y_test, y_pred))
r2 = r2_score(y_test, y_pred)

print(f"🔍 RMSE: {rmse:.2f}")
print(f"📈 R² score: {r2:.2f}")
