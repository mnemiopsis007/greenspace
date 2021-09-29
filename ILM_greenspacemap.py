import plotly.graph_objects as go
import plotly.express as px
import pandas as pd

px.set_mapbox_access_token("pk.eyJ1IjoibW5lbWlvcHNpcyIsImEiOiJjazE3N2ZicTEwNG5oM2Nsanp4bmZsZG5jIn0.-Mjv0izGOYAqZAgIr9JCkg")

df = pd.read_csv("Azy_data.csv")


fig = px.scatter_mapbox(df, lat="Lat", lon="Long", color="Greenspace", size="Size",
                  color_continuous_scale="greens", size_max=30, zoom=12)
fig.show()

# df2 = pd.read_csv("jayla_data.csv")

# fig2 = px.scatter_mapbox(df2, lat="Lat", lon="Long", color="WBGT", size="Size",
#                  color_continuous_scale="reds", size_max=30, zoom=12)

# fig2.show()


