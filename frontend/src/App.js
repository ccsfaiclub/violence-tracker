import React from 'react';
import './App.css';
import { Header } from "./components/Header";
import { Search } from "./components/Search";
import { Stats } from "./components/Stats";
import { ViolenceApp } from "./components/ViolenceApp";


function App() {

  return (
    <div className="App">
        <Header/>

        <ViolenceApp/>
        {/*ViolenceApp calls ViolenceMap*/}

        <Search/>
        <Stats/>
    </div>
  );
}

export default App;
