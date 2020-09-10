import React from 'react';
import styled from "styled-components";
import Grid from "@material-ui/core/Grid";
import List from "@material-ui/core/List";
import ListItem from "@material-ui/core/ListItem";


const Number = styled.div`
  font-size: 2.5em;
  color: orangered;
`;

const Title = styled.div`
  background-color: #485461;
  background-image: linear-gradient(315deg, #485461 0%, #28313b 74%);
  text-align: center;
  justify-content: center;
  padding: 50px;
  margin: 40px;
  font-size: 2.5em;
  color: white;
`;

const Row = styled.div`
  width: 100%;
  display: flex;
  flex-direction: row;
  justify-content: center;
  justify-content: space-between;
`;

export function Header(props) {
    const total_incidents = props.stats['getTotalIncidents'];
    const total_cities = props.stats['getTotalDistinctCities'];
    const total_states = props.stats['getTotalDistinctStates'];


    return (
        <Title>
            <Row>
                <Number>{total_incidents}</Number> reported police brutality incidents across
                <Number>{total_cities}</Number> cities and
                <Number>{total_states}</Number> states in the United States
            </Row>
        </Title>
    );
}