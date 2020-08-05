import React, { Component } from 'react';
import { Map, TileLayer, Marker, Popup } from 'react-leaflet';

export function ViolenceMap() {
    const position = {
        lat: 37.7749,
        lng: -122.4194,
        zoom: 13,
    }

    return (
        <div>
            <h1>MAP</h1>
            <Map
                center={[position.lat, position.lng]}
                zoom={position.zoom}
                style={{ width: '100%', height: '900px'}}
            >
                <TileLayer
                    url="https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png"
                    attribution='&copy <a href="http://osm.org/copyright">OpenStreetMap</a> contributors'
                />
                <Marker position={position}>
                    <Popup>An incident popup.<br />AI Rocks!.</Popup>
                </Marker>
            </Map>

        </div>
    );
}