#ID_cliente=12d80bed82d744fa8a019db12b765825
#Client_scret=3f44b45982c549dcadfdfbf2e24eff91

import os
import pandas as pd
import seaborn as sns
from dotenv import load_dotenv
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials, SpotifyOAuth


# load the .env file variables
load_dotenv()

client_id = os.environ.get("CLIENT_ID")
client_secret = os.environ.get("CLIENT_SECRET")
print(client_id)
# Configuración de autenticación y conexion
client_credential_manager = SpotifyClientCredentials(client_id=client_id, client_secret=client_secret) 

sp = spotipy.Spotify(client_credentials_manager=client_credential_manager)
'''
sp = spotipy.Spotify(auth_manager=SpotifyOAuth(
    client_id="client_id",
    client_secret="client_secret",
    #redirect_uri="http://localhost/"
))
'''
fito='1tZ99AnqyjgrmPwLfGU5eo'
response = sp.artist_top_tracks(fito)
if response:
  # We keep the "tracks" object of the answer
  df= pd.DataFrame(columns = ['name', 'popularity', 'time'])
  tracks = response["tracks"]
  for track in tracks:
    name=track['name']
    popu=int(track['popularity'])
    time=int(track['duration_ms'])/(1000*60)
    df=pd.concat([df,pd.DataFrame({'name':name,'popularity':popu,'time':time}, index = [0])], ignore_index = True)

df_pupu=df.sort_values('popularity')
print(df[:3])

#Analisis de la duracion frente a la popularidad

scatter_plot = sns.scatterplot(data = df, x = "popularity", y = "time")
fig = scatter_plot.get_figure()
fig.savefig("scatter_plot.png")


