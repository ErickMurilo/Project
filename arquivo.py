df['Data da Compra']

df['Data da Compra'] = pd.to_datetime(df['Data da Compra'], format='%d/%m/%Y')
print(df)

display(df)

df['Preço'].sum()

def format_number(value, prefix = ''):
  for unit in ['', 'mil']:
           if value < 1000:
                    return f'{prefix} {value:.2f} {unit}'
           value /= 1000
  return f'{prefix} {value:.2f} milhões'

format_number(df['Preço'].sum(), 'R$')

format_number(df.shape[0])

df_rec_estado = df.groupby('Local da compra')[['Preço']].sum()
print(df_rec_estado)

df_rec_estado = df.drop_duplicates(subset='Local da compra')[['Local da compra', 'lat', 'lon']]
print(df_rec_estado)

df_rec_estado = df.groupby('Local da compra')[['Preço']].sum()
df_rec_estado = df.drop_duplicates(subset='Local da compra')[['Local da compra', 'lat',
'lon']].merge(df_rec_estado, left_on='Local da compra', right_index=True).sort_values('Preço', ascending=False)
print(df_rec_estado)
