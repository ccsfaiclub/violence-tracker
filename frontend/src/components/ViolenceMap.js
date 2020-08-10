import React, { Component } from 'react';
import { Map, TileLayer, Marker, Popup } from 'react-leaflet';
import {point} from "leaflet";
import CardContent from "@material-ui/core/CardContent";
import * as marker from "leaflet";
import {Search} from "./Search";
import ReactLeafletSearch from "react-leaflet-search";

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

        console.log(props.incidents)
        markers = props.incidents.map(
            incident => {
                const p = {
                    lat: incident.location['lat'],
                    lng: incident.location['lon'],
                    zoom: 5
                }
                //position.lat = p.lat;
                //position.lng = p.lng;

                const popupName = incident['name'];
                const popupLocation = incident['city'] + ', ' + incident['state'];

                return (<Marker position={p}>
                    <Popup>{popupName} <p><strong>{popupLocation}</strong></p></Popup>
                    {/*<Popup>{popupLocation}</Popup>*/}
                </Marker>);
            });
        // Assign markers for the first __ incidents (limit can be changed)
        markers = markers.slice(0, 700);
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

            {/*This component adds a search bar to the top right of the page.*/}
            {/*Users can search incidents by inputting the name of the city or state.*/}
            {/*The map zooms to the location entered.*/}
            <ReactLeafletSearch
                position="topright"
                inputPlaceholder="Search by city or state"
                search = {
                    [33.100745405144245, 46.48315429687501]
                }
                showMarker={true}
                zoom={7}
                showPopup={false}
                // popUp={this.customPopup}
                closeResultsOnClick={true}
                openSearchOnLoad={true}
            />
        </Map>

    );
}