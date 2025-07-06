import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np

sns.set(style='whitegrid')
plt.rcParams['axes.titlesize'] = 14
plt.rcParams['axes.labelsize'] = 12

df = pd.read_csv('/content/df_womens_rosters_21_23.csv')

def limpar_percentual(coluna):
    return (
        df[coluna]
        .astype(str)
        .str.replace('%', '', regex=False)
        .str.replace('-', '', regex=False)
        .replace('', np.nan)      
        .astype(float)
    )

df['Block Success'] = limpar_percentual('Block Success')
df['Efficiency'] = limpar_percentual('Efficiency')
df['Serve Success'] = limpar_percentual('Serve Success')

jogadoras_br = df[df['Country_Name'] == 'Brazil'].copy()

jogadoras_br['Year'] = pd.to_numeric(jogadoras_br['Year'], errors='coerce')
colunas_numericas = ['Total Points', 'Block Points', 'Efficiency', 'Block Success']
for col in colunas_numericas:
    jogadoras_br[col] = pd.to_numeric(jogadoras_br[col], errors='coerce')

media_ano = jogadoras_br.groupby('Year')[['Total Points', 'Block Points', 'Efficiency']].mean().reset_index()

plt.figure(figsize=(10, 6))
plt.plot(media_ano['Year'], media_ano['Total Points'], marker='o', label='Total Points')
plt.plot(media_ano['Year'], media_ano['Block Points'], marker='s', label='Block Points')
plt.plot(media_ano['Year'], media_ano['Efficiency'], marker='^', label='Efficiency')

plt.title('Média das Estatísticas por Ano - Jogadoras Brasileiras (2021–2023)')
plt.xlabel('Ano')
plt.ylabel('Média')
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.show()

top10_pontos = (
    jogadoras_br.groupby('Player Name')['Total Points']
    .sum()
    .sort_values(ascending=False)
    .head(10)
    .reset_index()
)

plt.figure(figsize=(10, 6))
sns.barplot(x='Total Points', y='Player Name', data=top10_pontos, palette='viridis')
plt.title('Top 10 Jogadoras BR por Pontos Totais (2021–2023)')
plt.xlabel('Total de Pontos')
plt.ylabel('Jogadora')
plt.tight_layout()
plt.show()

jogadoras_nao_liberos = jogadoras_br[~jogadoras_br['Position'].str.lower().str.contains('L')]

top10_bloqueio = (
    jogadoras_nao_liberos.groupby('Player Name')['Block Success']
    .sum()
    .sort_values(ascending=False)
    .head(10)
    .reset_index()
)

plt.figure(figsize=(10, 6))
sns.barplot(x='Block Success', y='Player Name', data=top10_bloqueio, palette='viridis')
plt.title('Top 10 Jogadoras BR com Maior Sucesso em Bloqueios (2021–2023)')
plt.xlabel('Sucesso em Bloqueios')
plt.ylabel('Jogadora')
plt.tight_layout()
plt.show()

eficiencia_validas = jogadoras_br[jogadoras_br['Efficiency'].notna()]

top10_eficiencia = (
    eficiencia_validas.groupby('Player Name')['Efficiency']
    .mean()
    .sort_values(ascending=False)
    .head(10)
    .reset_index()
)

plt.figure(figsize=(10, 6))
sns.barplot(x='Efficiency', y='Player Name', data=top10_eficiencia, palette='viridis')
plt.title('Top 10 Jogadoras BR por Eficiência Média (2021–2023)')
plt.xlabel('Eficiência Média')
plt.ylabel('Jogadora')
plt.tight_layout()
plt.show()

eficiencia_por_pais = (
    df[df['Efficiency'].notna()]
    .groupby('Country_Name')['Efficiency']
    .mean()
    .sort_values(ascending=False)
    .reset_index()
)

plt.figure(figsize=(12, 6))
sns.barplot(x='Efficiency', y='Country_Name', data=eficiencia_por_pais.head(10), palette='coolwarm')
plt.title('Top 10 Países por Eficiência Média das Jogadoras (2021–2023)')
plt.xlabel('Eficiência Média (%)')
plt.ylabel('País')
plt.tight_layout()
plt.show()

comparar_paises = ['Brazil', 'USA', 'Italy']

df_comp = df[df['Country_Name'].isin(comparar_paises) & df['Efficiency'].notna()]

plt.figure(figsize=(8, 6))
sns.boxplot(x='Country_Name', y='Efficiency', data=df_comp, palette='pastel')
plt.title('Distribuição da Eficiência por País (2021–2023)')
plt.xlabel('País')
plt.ylabel('Eficiência (%)')
plt.tight_layout()
plt.show()

paises = ['Brazil', 'USA', 'Italy']
df_filtrado = df[df['Country_Name'].isin(paises)].copy()
media_saque_bloqueio = df_filtrado.groupby('Country_Name')[['Serve Success', 'Block Success']].mean().reset_index()
plt.figure(figsize=(10,6))

largura = 0.35
x = np.arange(len(media_saque_bloqueio['Country_Name']))

plt.bar(x - largura/2, media_saque_bloqueio['Serve Success'], width=largura, label='Sucesso no Saque')
plt.bar(x + largura/2, media_saque_bloqueio['Block Success'], width=largura, label='Sucesso no Bloqueio')

plt.xticks(x, media_saque_bloqueio['Country_Name'])
plt.ylabel('Média de Sucesso (%)')
plt.title('Comparação de Sucesso no Saque e Bloqueio - Brasil, EUA e Itália (2021-2023)')
plt.legend()
plt.grid(axis='y')
plt.tight_layout()
plt.show()

from sklearn.preprocessing import MinMaxScaler

scaler = MinMaxScaler()

medias = media_saque_bloqueio.copy()
medias['Efficiency'] = df_comp.groupby('Country_Name')['Efficiency'].mean().values

medias_scaled = medias.copy()
medias_scaled[['Serve Success', 'Block Success', 'Efficiency']] = scaler.fit_transform(medias_scaled[['Serve Success', 'Block Success', 'Efficiency']])

medias_scaled['Score'] = medias_scaled[['Serve Success', 'Block Success', 'Efficiency']].mean(axis=1)

medias_scaled.sort_values('Score', ascending=False)