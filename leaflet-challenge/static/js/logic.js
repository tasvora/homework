// // Creating map object
// var myMap = L.map("map", {
//     center: [34.0522, -118.2437],
//     zoom: 8
//   });

//   // Adding tile layer
//   L.tileLayer("https://api.tiles.mapbox.com/v4/{id}/{z}/{x}/{y}.png?access_token={accessToken}", {
//     attribution: "Map data &copy; <a href=\"https://www.openstreetmap.org/\">OpenStreetMap</a> contributors, <a href=\"https://creativecommons.org/licenses/by-sa/2.0/\">CC-BY-SA</a>, Imagery © <a href=\"https://www.mapbox.com/\">Mapbox</a>",
//     maxZoom: 18,
//     id: "mapbox.streets",
//     accessToken: API_KEY
//   }).addTo(myMap);

function markerSize(mag) {
    return mag * 10000;

}

function markerColor(mag) {
    colorCode = "white";
    if (mag <= 1) {
        colorCode = "#ADFF2F";
    } else if (mag <= 2) {
        colorCode = "#FFD700";
    } else if (mag <= 3) {
        colorCode = "#FFA500";
    } else if (mag <= 4) {
        colorCode = "#FF8C00";
    } else if (mag <= 5) {
        colorCode = "#FF4500";
    } else if (mag > 5) {
        colorCode = "#F61313";
    }
    return colorCode;
}

// Load in GeoJson data
var eq_Past7_days_url = "https://earthquake.usgs.gov/earthquakes/feed/v1.0/summary/all_week.geojson";

d3.json(eq_Past7_days_url, function (response) {
    console.log(response);
    createFeatures(response.features);
});

function createFeatures(earthquakeData) {
    // Define a function we want to run once for each feature in the features array
    // Give each feature a popup describing the place and time of the earthquake
    function onEachFeature(feature, layer) {
        console.log(feature);
        layer.bindPopup("<h3>" + feature.properties.place +
            "</h3><hr><p>" + new Date(feature.properties.time) + "</p>");
    }
    function pointToLayer(feature, latlng) {
        return new L.circle(latlng,
            {
                radius: markerSize(feature.properties.mag),
                fillColor: markerColor(feature.properties.mag),
                fillOpacity: 0.50,
                stroke: false,
            })
    }


    // Create a GeoJSON layer containing the features array on the earthquakeData object
    // Run the onEachFeature function once for each piece of data in the array
    var earthquakes = L.geoJSON(earthquakeData, {
        onEachFeature: onEachFeature,
        pointToLayer: pointToLayer
    });

    // Sending our earthquakes layer to the createMap function
    createMap(earthquakes);
}



function createMap(earthquakes) {

    // Define streetmap and darkmap layers
    var satellite = L.tileLayer("https://api.tiles.mapbox.com/v4/{id}/{z}/{x}/{y}.png?access_token={accessToken}", {
        attribution: "Map data &copy; <a href=\"https://www.openstreetmap.org/\">OpenStreetMap</a> contributors, <a href=\"https://creativecommons.org/licenses/by-sa/2.0/\">CC-BY-SA</a>, Imagery © <a href=\"https://www.mapbox.com/\">Mapbox</a>",
        maxZoom: 18,
        id: "mapbox.satellite",
        accessToken: API_KEY
    });

    var lightmap = L.tileLayer("https://api.tiles.mapbox.com/v4/{id}/{z}/{x}/{y}.png?access_token={accessToken}", {
        attribution: "Map data &copy; <a href=\"https://www.openstreetmap.org/\">OpenStreetMap</a> contributors, <a href=\"https://creativecommons.org/licenses/by-sa/2.0/\">CC-BY-SA</a>, Imagery © <a href=\"https://www.mapbox.com/\">Mapbox</a>",
        maxZoom: 18,
        id: "mapbox.light",
        accessToken: API_KEY
    });

    var outdoors = L.tileLayer("https://api.tiles.mapbox.com/v4/{id}/{z}/{x}/{y}.png?access_token={accessToken}", {
        attribution: "Map data &copy; <a href=\"https://www.openstreetmap.org/\">OpenStreetMap</a> contributors, <a href=\"https://creativecommons.org/licenses/by-sa/2.0/\">CC-BY-SA</a>, Imagery © <a href=\"https://www.mapbox.com/\">Mapbox</a>",
        maxZoom: 18,
        id: "mapbox.outdoors",
        accessToken: API_KEY
    });


    // Define a baseMaps object to hold our base layers
    var baseMaps = {
        "Satellite": satellite,
        "Grayscale": lightmap,
        "Outdoors" : outdoors
    };

    // Create overlay object to hold our overlay layer
    var overlayMaps = {
        Earthquakes: earthquakes
    };

    // Create our map, giving it the streetmap and earthquakes layers to display on load
    var myMap = L.map("map", {
        center: [
            37.09, -95.71
        ],
        zoom: 5,
        layers: [lightmap, earthquakes]
    });

    // Create a layer control
    // Pass in our baseMaps and overlayMaps
    // Add the layer control to the map
    L.control.layers(baseMaps, overlayMaps, {
        collapsed: false
    }).addTo(myMap);

    var legend = L.control({ position: 'bottomright' });

    legend.onAdd = function (map) {

        var div = L.DomUtil.create('div', 'info legend'),
            magnitudes = [0, 1, 2, 3, 4, 5],
            colors = ["#ADFF2F","#FFD700","#FFA500","#FF8C00","#FF4500","#F61313"],
            labels = [];

        //setting html for div we just  created above.
        div.innerHTML = '<div class="labels">'
        //<div class="min">' + magnitudes[0] + '</div><div class="max">' + magnitudes[magnitudes.length - 1] + '</div></div>'

        magnitudes.forEach(function (magnitudes, index) {
            if(index<5){
                range = index+1;
                div.innerHTML += '<div class="place">' + index +'-'+ range +'</div>'
            }else {
                div.innerHTML += '<div class="place">' + index +'+</div>'
            }
            
            
            
            console.log(colors[index]);
            labels.push('<li style="background-color: ' + colors[index] + '"></li>')
        })

        div.innerHTML += '</div><ul>' + labels.join('') + '</ul>'
        return div;//this is very important 
        
    };
    legend.addTo(myMap);

}
