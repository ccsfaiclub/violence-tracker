import React from 'react';
import {ViolenceMap} from "./ViolenceMap";
import {getData} from "../client";
import {Header} from "./Header";
import { useQuery } from "@apollo/react-hooks"
import gql from "graphql-tag"

// this query will be passed to useQuery to tell Apollo to
// fetch incidents data, including location
const GET_INCIDENTS = gql`
{
  getTotalIncidents,
  getTotalDistinctCities,
  getTotalDistinctStates,
  incidents {
        id
        externalId
        links
        state
        city
        description
        tags
        name
        date
        dateText
        location {
            id
            city
            state
            lat
            lon
        }
    }
}
`;


export function ViolenceApp() {
    const { loading, error, data } = useQuery(GET_INCIDENTS);
    console.log(loading);

    if (error) return <h1>Something went wrong!</h1>;
    if (loading) return <h1>Loading...</h1>;

    if (data) {
        return (
            <div className="App">
                <Header stats={data}/>
                <ViolenceMap incidents={data['incidents']}/>
            </div>
        );
    }
    return (<h1>No data</h1>)
}

