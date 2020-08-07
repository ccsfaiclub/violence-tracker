import React from 'react';
import {useEffect, useState} from "react";
import {ViolenceMap} from "./ViolenceMap";
import {getData} from "../client";


export function ViolenceApp() {
    const [incidentData, setIncidentData] = useState(null);

    useEffect(() => {
        if (incidentData === null) {
            getData().then(json => {
                setIncidentData(json);
            })
        }
    });


    return (
        <ViolenceMap incidents={incidentData}/>
    );
}

