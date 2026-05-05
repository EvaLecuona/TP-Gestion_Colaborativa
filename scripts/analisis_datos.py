import pandas as pd
import matplotlib.pyplot as plt

# Carga del dataset utilizando rutas relativas para asegurar la portabilidad del proyecto
df = pd.read_csv('datos/sales_sample_2024.csv')

# Procesamiento de datos: Se define la columna de ventas totales para el análisis
# En este escenario, se utiliza 'sales_amount' como métrica principal
df['total_venta'] = df['sales_amount']

# Configuración del aspecto visual del gráfico
plt.figure(figsize=(10,6))
plt.plot(df['sales_date'], df['sales_amount'], marker='o', color='b', linestyle='-')

# Personalización de etiquetas y títulos del reporte visual
plt.title('Evolución de Ventas 2024 - Escenario Comercial')
plt.xlabel('Fecha de Venta')
plt.ylabel('Monto (ARS)')
plt.xticks(rotation=45)
plt.tight_layout()

# Exportación automatizada del resultado a la carpeta de destino técnica
plt.savefig('resultados/grafico_ventas.png')
print("Análisis completado exitosamente. El gráfico ha sido exportado a la carpeta /resultados.")
