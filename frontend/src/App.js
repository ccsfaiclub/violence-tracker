import React from 'react';

import './App.css';
import {Header} from "./components/Header";
import {Map} from "./components/Map";
import {Search} from "./components/Search";
import {Stats} from "./components/Stats";

function App() {
  return (
    <div className="App">
        <Header/>
        <Map/>
        <Search/>
        <Stats/>
    </div>
  );
}

export default App;
