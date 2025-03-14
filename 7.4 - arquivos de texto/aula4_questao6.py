import pandas as pd

# Abrindo o arquivo CSV com o caminho correto
file_path = '/home/pd/Documentos/python/Módulo7/7.4 - arquivos de texto/spotify-2023.csv'
data = pd.read_csv(file_path, encoding='latin-1')

# Visualizando as cinco primeiras linhas do DataFrame
print(data.head())

# Filtrando os dados para os anos de 2012 a 2022
data_filtered = data[(data['released_year'] >= 2012) & (data['released_year'] <= 2022)]

# Inicializando uma lista para armazenar as músicas mais tocadas por ano
top_tracks_per_year = []

# Iterando pelos anos de 2012 a 2022
for year in range(2012, 2023):
    # Filtrando as músicas do ano atual
    year_tracks = data_filtered[data_filtered['released_year'] == year]
    
    # Ignorando linhas com mais de um artista ou com nomes de músicas entre aspas
    year_tracks = year_tracks[~year_tracks['artist(s)_name'].str.contains('"')]
    year_tracks = year_tracks[~year_tracks['track_name'].str.contains('"')]
    
    # Verificando se ainda existem músicas após o filtro
    if not year_tracks.empty:
        # Encontrando a música com o maior número de streams
        top_track = year_tracks.loc[year_tracks['streams'].idxmax()]
        
        # Adicionando informações à lista
        top_tracks_per_year.append([
            top_track['track_name'],
            top_track['artist(s)_name'],
            top_track['released_year'],
            top_track['streams']
        ])

# Imprimindo a lista produzida
print(top_tracks_per_year)