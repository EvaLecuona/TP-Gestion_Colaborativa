
import pandas as pd
import matplotlib.pyplot as plt


df = pd.read_csv('datos/sales_sample_2024.csv')


df['total_venta'] = df['sales_amount'] 


plt.figure(figsize=(10,6))
plt.plot(df['sales_date'], df['sales_amount'], marker='o')
plt.title('Evolución de Ventas 2024')
plt.xticks(rotation=45)
plt.tight_layout()

plt.savefig('resultados/grafico_ventas.png')
print("Análisis completado. Gráfico guardado en /resultados.")
