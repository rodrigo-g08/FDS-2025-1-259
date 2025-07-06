# YouTube Trending Analysis – United Kingdom UK

## 🎯 Objetivo del Proyecto

El objetivo de este proyecto es analizar las tendencias de los videos más populares en YouTube en el país de **Gran Bretaña**, usando un enfoque estructurado basado en la metodología **CRISP-DM**. A través del análisis de datos, se busca identificar qué categorías de video son más populares, cómo evolucionan las tendencias a lo largo del tiempo, y si es posible predecir interacciones como vistas, likes y comentarios.

Este análisis permitirá a una consultora internacional comprender el impacto del contenido según su tipo, canal, localización geográfica y evolución temporal.

---

## 👥 Alumnos Participantes

| Código      | Nombre Completo                     | Rol                      |
|-------------|-------------------------------------|---------------------------|
| U20221c424  | Angel Gabriel Diaz Chavez           | Data Engineer             |
| U20231B834  | Rodrigo Alonso Gamero Vera          | Business Project Sponsor  |
| U202314397  | Marcelo Matias Hernandez Rengifo    | Data Scientist            |
| U202319900  | Jairo Luis Orihuela Paredes         | Data Analyst              |

---

## 📊 Descripción del Conjunto de Datos

El dataset usado proviene del repositorio público de estadísticas de videos en tendencia de YouTube. Se trabajó específicamente con los archivos:

- `GBvideos.csv`: contiene registros de videos en tendencia en Reino Unido, incluyendo vistas, likes, dislikes y comentarios.  
- `GB_category_id.json`: archivo que asigna nombres a los IDs de categoría de video.

**Principales columnas del dataset:**

- `video_id`, `title`, `channel_title`, `category_id`, `views`, `likes`, `dislikes`, `comment_count`, `publish_time`, `trending_date`, entre otras.  
- Información adicional como latitud/longitud del estado, estado geográfico, etiquetas, si los comentarios o calificaciones están desactivados.

📄 **Documento PDF con la descripción detallada del dataset adjunto en el repositorio.**

---

## ✅ Conclusiones

- Las categorías de video más populares en Gran Bretaña fueron aquellas relacionadas con entretenimiento y música.
- Existen categorías con altos ratios de likes/dislikes, lo cual es un buen indicador de aceptación.
- La winsorización de valores extremos mejoró significativamente la calidad del dataset sin pérdida de información relevante.
- Mediante técnicas como **K-Means**, se identificaron agrupaciones útiles para comprender el comportamiento del público.
- El modelo predictivo permitió evaluar la posibilidad de estimar vistas o likes a partir de otras variables, aunque se requieren más datos para mejorar la precisión.

---

## 📄 Licencia de Uso

Este proyecto se distribuye bajo la Licencia MIT. Ver más en el archivo `LICENSE`.

---

## 📎 Enlaces Útiles

- 📁 Repositorio del Proyecto: [FDS-2025-1-259](https://github.com/rodrigo-g08/FDS-2025-1-259)
- 📄 Documento PDF con la descripción de los datos: `Descripcion_Dataset_YouTube_GB.pdf`
