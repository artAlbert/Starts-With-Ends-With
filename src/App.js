import logo from './logo.svg';
import './App.css';
import React, {useEffect, useState} from 'react';
import PostForm from './components/PostForm';
import FetchWords from './components/FetchWords';
import RadioSelection from './components/RadioSelection';

function App() {

  return (
    <div className="App">
      <header className="App-header">
        <RadioSelection/>
      </header>
    </div>
  );
}

export default App;