import pandas as pd

df_caja1 = pd.DataFrame({
    'fetcha': ['2021-01-01', '2021-02-01', '2021-03-01', '2021-04-01', '2021-05-01'],
    'venta_caja1': [1004, 2500, 1300, 4005, 5002]
})

df_caja2 = pd.DataFrame({
    'fetcha': ['2021-01-01', '2021-02-01', '2021-03-01', '2021-04-01', '2021-05-01', '2021-06-01'],
    'venta_caja2': [1500, 3000, 1400, 5000, 6000, 1239]
})


df_ventas_totals = pd.merge(df_caja1, df_caja2, on='fetcha', how='outer')
df_ventas_totals['Total'] = df_ventas_totals[['venta_caja1', 'venta_caja2']].sum(axis=1)

print(df_ventas_totals)
