
import folium
import pandas

'''data0 = pandas.read_csv("litrate.csv")
lit11 = list (data0["2011"])
lit1 = list (data0["2001"])

incn = []
for liter11, liter1 in zip(lit11,lit1):
    incn.append(liter11-liter1)

def color_fill(literacy):
    if literacy < 60:
        return 'red'
    elif 60<= literacy <80:
        return 'orange'
    else:
        return 'green' '''



data = pandas.read_csv("population.csv")
data.head()
center_lat = data.Latitude.mean()
center_long = data.Longitude.mean()

lat = list(data["Latitude"])
lon = list(data["Longitude"])
sta = list(data["State"])
dis = list(data["District"])
pop11 = list(data["Population in 2011"])
pop1 = list(data["Population in 2001"])

inc = []
for po1, po11 in zip(pop1,pop11):
    inc.append(round((((po11 - po1)/po1)*100) , 2))

def color_producer(population):
    if population < 1:
        return 'blue'
    elif 1 <= population < 10:
        return 'green' 
    elif 5 <= population < 15:
        return 'pink'
    elif 15 <= population < 25:
        return 'orange'
    elif 25<= population < 35:
        return 'red'
    else:
        return 'darkred' 



m= folium.Map(location=[center_lat,center_long],tiles="Stamen Terrain")
folium.FitBounds([(center_lat-5,center_long-5),(center_lat+5,center_long+5)]).add_to(m)

fpop = folium.FeatureGroup(name="India_population_circle_markers")
for lt,ln,st,di,incr in zip(lat,lon,sta,dis,inc):
    fpop.add_child(folium.CircleMarker(location=[lt,ln],radius=10, popup= st+", "+di+", "+str(incr)+"%", fill_color= color_producer(incr), color='grey',fill_opacity=0.7))


fpoy = folium.FeatureGroup(name="India_state_literacy")
fpoy.add_child(folium.GeoJson(data=open('INDIA_STATES.json','r',encoding='utf-8-sig').read()))
    

#lambda x:{'fillcolor':'red' if x['properties']['STATE'] < '60' else 'orange' if '60'<=x['properties']['STATE']> '80' else 'green' 

m.add_child(fpoy)
m.add_child(fpop)


m.add_child(folium.LayerControl())


m.save("INDIA_map.html")

 