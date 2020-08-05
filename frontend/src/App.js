import React, { Component, Fragment } from 'react';
// import axios from 'axios';

import './App.css';
import { Header } from "./components/Header";
import { ViolenceMap } from "./components/ViolenceMap";
import { Search } from "./components/Search";
import { Stats } from "./components/Stats";


function App() {

  return (
    <div className="App">
        <Header/>
        <ViolenceMap/>
        <Search/>
        <Stats/>
    </div>
  );
}

export default App;
