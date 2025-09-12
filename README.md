Proyecto 1 – Visualización de Variables Macroeconómicas

URL del repositorio:

URL de la app:



Esta aplicación en Streamlit  permite visualizar tres indicadores clave de la economía colombiana: PIB, desempleo e inflación, a lo largo de los últimos 15 años.

Fuentes:
Entidad: Banco de la República de Colombia

Series utilizadas:
-Producto Interno Bruto (PIB) (crecimiento PIB real, trimestral,base:2015,Ajuste estacional)
frecuencia trimestral

-Tasa de desempleo (total nacional) – frecuencia mensual
-inflación total – frecuencia mensual

-Periodo: 30/06/2010 al 30/06/2025 (últimos 15 años)

Transformaciones:
-Limpieza básica de columnas y tipos de datos
-Conversión de todas las series a frecuencia anual para facilitar la comparación
-Control de datos nulos y revisión de estacionalidad


Las series fueron descargadas directamente del Banco de la República. Dado que cada variable tenía una frecuencia distinta (PIB trimestral, desempleo e inflación mensual), se transformaron a frecuencia anual para facilitar la visualización conjunta. Se asumió que estas transformaciones no afectan significativamente la interpretación general de las tendencias.