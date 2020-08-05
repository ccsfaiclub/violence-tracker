import React, { Component } from 'react';
import { Map, TileLayer, Marker, Popup } from 'react-leaflet';
import {point} from "leaflet";

export function ViolenceMap(props) {
    // Initially, position will be centered on map
    const position = {
        lat: 41.15,
        lng: -96.50,
        zoom: 5,
    }

    // An array to hold location of all incidents
    let markers = [];
    // If there are incidents, loop through the array, returning
    // each incident's position (for its marker), and address (for its popup text)
    if (props.incidents) {
        markers = props.incidents.map(
            incident => {
                const position = {
                    lat: incident['point']['coordinates'][1],
                    lng: incident['point']['coordinates'][0],
                    zoom: 5
                }

                const popupText = incident['address'] + ', ' + incident['city'];

                return (<Marker position={position}>
                    <Popup>{popupText}</Popup>
                </Marker>);
            });
        // Assign markers for the first 100 incidents (limit can be changed)
        markers = markers.slice(0, 100);
        // Zoom into the first marker's position
        position['lat'] = props.incidents[0]['point']['coordinates'][1];
        position['lng'] = props.incidents[0]['point']['coordinates'][0];
        position['zoom'] = 12;
    }


    return (
        <Map
            center={[position.lat, position.lng]}
            zoom={position.zoom}
            style={{width: '100%', height: '900px'}}
        >
            <TileLayer
                url="https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png"
                attribution='&copy <a href="http://osm.org/copyright">OpenStreetMap</a> contributors'
            />
            {markers}
        </Map>

    );
}