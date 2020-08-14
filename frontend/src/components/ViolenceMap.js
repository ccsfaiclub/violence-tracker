import React, {Component, useState} from 'react';
import {Map, TileLayer, Marker, Popup, ZoomControl} from 'react-leaflet';
import ReactLeafletSearch from "react-leaflet-search";
import { Sidebar, Tab } from "react-leaflet-sidebarv2";
import { withStyles } from "@material-ui/core/styles";
import Avatar from "@material-ui/core/Avatar";
import CardMedia from "@material-ui/core/CardMedia";
import CardContent from "@material-ui/core/CardContent";
import Divider from "@material-ui/core/Divider";
import Typography from "@material-ui/core/Typography";
import Card from "@material-ui/core/Card";
import {deepOrange} from "@material-ui/core/colors";


const styles = muiBaseTheme => ({
    card: {
        maxWidth: 450,
        margin: "auto",
        transition: "0.3s",
        boxShadow: "0 8px 40px -12px rgba(0,0,0,0.3)",
        "&:hover": {
            boxShadow: "0 16px 70px -12.125px rgba(0,0,0,0.3)"
        }
    },
    avatar: {
        display: "inline-block",
        backgroundColor: deepOrange[500]
    },
    media: {
        paddingTop: "106.25%"
    },
    content: {
        textAlign: "left",
        padding: muiBaseTheme.spacing.unit * 4
    },
    heading: {
        fontWeight: "bold"
    },
    subheading: {
        lineHeight: 2
    },
    divider: {
        margin: `${muiBaseTheme.spacing.unit * 4}px 0`
    }

});

export function ViolenceMap(props) {
    // Initially, position will be centered on map
    const position = {
        lat: 41.15,
        lng: -96.50,
        zoom: 5,
    }
    // Sidebar
    const [sidebarState, setSidebarState] = useState(
        {
            collapsed: true,
            selected: 'home',
            selectedIncident: null
        })
    // Show incident info on sidebar if there's data to show
    let selectedIncidentComponent;
    if (sidebarState.selectedIncident) {
        const incident = sidebarState.selectedIncident;
        var date = incident['date'];
        var [yyyy, mm, dd] = date.split('-');
        var date = `${mm}-${dd}-${yyyy}`;

        const links = JSON.parse(incident['links']); // links is a string of JSON
        // console.log(typeof(links))

        let sources = [];
        for (const i in links) {
            const url = links[i]["url"]
            if (url) {
                sources.push((<p><a href={url}target="_blank">{url}</a></p>))
            }
        }

        // alert(sources);

        selectedIncidentComponent =
           // <div>{sidebarState.selectedIncident['name']}</div>

           <Card className={incident.card} align={"left"}>
               <CardMedia
                   className={incident.media}
               />
               <CardContent className={incident.content}>
                   <Typography
                       className={"MuiTypography--heading"}
                       variant={"h5"}
                       color={"orange"}
                       gutterBottom
                   >
                       {incident['city'] + ', ' + incident['state']}
                       <Typography
                           className={"MuiTypography--heading"}
                           variant={"subtitle1"}
                       >
                           {date}
                       </Typography>
                   </Typography>
                   <Divider className={incident.divider} light />
                   <Typography
                       className={"MuiTypography--subheading"}
                       variant={"h5"}
                       color={"darkgrey"}
                   >
                       <p><p><h2>{incident['name']}</h2></p></p>
                   </Typography>
                   <Typography
                       className={"MuiTypography--subheading"}
                       variant={"display1"}
                       color={"textSecondary"}
                   >
                       <p><h2>{incident['description']}</h2></p>
                   </Typography>
                   <Divider className={incident.divider} light />
                   <Typography
                       className={"MuiTypography--subheading"}
                       variant={"display4"}
                       color={"textSecondary"}
                   >

                       <p><h3>Sources:</h3></p>
                       {sources}

                       {/*`<a href="${links[i]['url']}"/>`*/}
                   </Typography>
                   <Divider className={incident.divider} light />
               </CardContent>
           </Card>
    }

    // Closes and opens the sidebar, respectively
    function onClose() {
        setSidebarState({
            collapsed: true
        });
    }
    function onOpen(id) {
        setSidebarState({
            collapsed: false,
            selected: id
        });
    }

    // Shows the info card in the sidebar when a marker is clicked
    function onMarkerClicked(clickedIncident) {
        setSidebarState(
            {
                collapsed:false,
                selectedIncident: clickedIncident,
                selected:'home'}
                )
    }

    // An array to hold location of all incidents
    let markers = [];
    // If there are incidents, loop through the array, returning
    // each incident's position (for its marker), and address (for its popup text)
    if (props.incidents) {

        markers = props.incidents.map(
            incident => {
                const p = {
                    lat: incident.location['lat'],
                    lng: incident.location['lon'],
                    zoom: 5
                }
                //position.lat = p.lat;
                //position.lng = p.lng;
                const id = incident['id'];
                const popupName = incident['name'];
                const popupLocation = incident['city'] + ', ' + incident['state'];

                // Call back
                return (<Marker position={p} onclick={() => onMarkerClicked(incident)}>
                    <Popup>{popupName} <p><strong>{popupLocation}</strong></p></Popup>
                    {/*<Popup>{popupLocation}</Popup>*/}
                </Marker>);
            });
        // Assign markers for the first __ incidents (limit can be changed)
        markers = markers.slice(0, 700);
    }


    return (
        <div>
            <Map
                className="sidebar-map"
                center={[position.lat, position.lng]}
                zoom={position.zoom}
                style={{height: '100vh', width: '100wh'}}
                zoomControl={'false'}
                // position={{'bottomright'}}
            >
                <TileLayer
                    url="https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png"
                    attribution='&copy <a href="http://osm.org/copyright">OpenStreetMap</a> contributors'
                />
                {markers}
                {/*This component adds a search bar to the top right of the page.*/}
                {/*Users can search by city or state.*/}
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
                    // popUp={ .customPopup}
                    closeResultsOnClick={true}
                    openSearchOnLoad={true}
                />

                <ZoomControl position="topright" />

                <Sidebar
                    id="sidebar"
                    collapsed={sidebarState.collapsed}
                    selected={sidebarState.selected}
                    onOpen={onOpen}
                    onClose={onClose}
                    position="left"

                >
                    <Tab id="home" header="VIOLENCE TRACKER" icon="fa fa-bars">
                        <p>View incidents of police brutality in the U.S.</p>
                    </Tab>

                    {selectedIncidentComponent}

                    <Tab id="info" header="Stats" icon="fa fa-area-chart">
                        <p>View dashboard</p>
                    </Tab>
                    <Tab id="settings" header="Report" icon="fa fa-exclamation-triangle">
                        <p>Report an incident</p>
                    </Tab>

                </Sidebar>
            </Map>
        </div>
    );
}