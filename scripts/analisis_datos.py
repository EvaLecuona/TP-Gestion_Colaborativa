
import pandas as pd
import matplotlib.pyplot as plt

# Cargar los datos (usando rutas relativas como pide el TP)
df = pd.read_csv('datos/sales_sample_2024.csv')

# Lógica: Calcular ventas totales
df['total_venta'] = df['sales_amount'] # Aquí podrías multiplicar si tuvieras 'cantidad'

# Generar un gráfico simple
plt.figure(figsize=(10,6))
plt.plot(df['sales_date'], df['sales_amount'], marker='o')
plt.title('Evolución de Ventas 2024')
plt.xticks(rotation=45)
plt.tight_layout()

# Guardar el gráfico en /resultados
plt.savefig('resultados/grafico_ventas.png')
print("Análisis completado. Gráfico guardado en /resultados.")
