import urllib2
import json
import webbrowser
from datetime import datetime

startTime=datetime.now()

#Will be used to launch a web browser and view the output
filepath = 'file:///c:/python27/Earthquakebigg.html'
#Read complete documentation for the API here-http://www.openhazards.com/data/GetEarthquakeCatalog
url='http://api.openhazards.com/GetEarthquakeCatalog?t0=2014/06/06'
htmlCoords=""
#Reads the weather forecast
quakes = urllib2.urlopen(url).read().splitlines()
count=str(len(quakes))
print "%s have to be processed"%count
for quake in quakes:
    quakeData=quake.split(" ",6)
    lat,lon=quakeData[2],quakeData[3]
    #Format of JS: new google.maps.LatLng(X,X)
    htmlCoords+='new google.maps.LatLng('+str(lat)+","+str(lon)+"),"
print "%s earthquakes have been processed in "%count+str(datetime.now()-startTime)

#To remove the last comma which gets added by iteration of the previous statement.        
jsInput = htmlCoords[:-1]

#Create the HTML file
outputFile = open('Earthquakebigg.html','w')
message="""<!DOCTYPE html>
<html>
  <head>
    <meta charset="utf-8">
    <title>Heatmap</title>
    <style>
      html, body, #map-canvas {
        height: 100%;
        margin: 0px;
        padding: 0px
      }
      #panel {
        position: absolute;
        top: 5px;
        left: 50%;
        margin-left: -180px;
        z-index: 5;
        background-color: #fff;
        padding: 5px;
        border: 1px solid #999;
      }
    </style>
    <script src="https://maps.googleapis.com/maps/api/js?v=3.exp&libraries=visualization"></script>
    <script>

    var map, pointarray, heatmap;

    var taxiData = ["""+jsInput+"""
  
    ];

    function initialize() {
      var mapOptions = {
        zoom: 2,
        center: new google.maps.LatLng(0,0),
        mapTypeId: google.maps.MapTypeId.ROADMAP
    };

     map = new google.maps.Map(document.getElementById('map-canvas'),
      mapOptions);

      var pointArray = new google.maps.MVCArray(taxiData);

      heatmap = new google.maps.visualization.HeatmapLayer({
    data: pointArray
      });

  heatmap.setMap(map);
    }

function toggleHeatmap() {
  heatmap.setMap(heatmap.getMap() ? null : map);
}

function changeGradient() {
  var gradient = [
    'rgba(0, 255, 255, 0)',
    'rgba(0, 255, 255, 1)',
    'rgba(0, 191, 255, 1)',
    'rgba(0, 127, 255, 1)',
    'rgba(0, 63, 255, 1)',
    'rgba(0, 0, 255, 1)',
    'rgba(0, 0, 223, 1)',
    'rgba(0, 0, 191, 1)',
    'rgba(0, 0, 159, 1)',
    'rgba(0, 0, 127, 1)',
    'rgba(63, 0, 91, 1)',
    'rgba(127, 0, 63, 1)',
    'rgba(191, 0, 31, 1)',
    'rgba(255, 0, 0, 1)'
  ]
  heatmap.set('gradient', heatmap.get('gradient') ? null : gradient);
}

function changeRadius() {
  heatmap.set('radius', heatmap.get('radius') ? null : 20);
}



google.maps.event.addDomListener(window, 'load', initialize);

    </script>
  </head>

  <body>
    <div id="panel">
      <button onclick="toggleHeatmap()">Toggle Heatmap</button>
      <button onclick="changeGradient()">Change gradient</button>
      <button onclick="changeRadius()">Change radius</button>
    </div>
    <div id="map-canvas"></div>
  </body>
</html>"""
outputFile.write(message)
outputFile.close()

#Launch a browser to view the results
webbrowser.open(filepath)


        
        
        
    

