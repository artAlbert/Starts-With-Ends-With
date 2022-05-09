import logo from './logo.svg';
import './App.css';
import React, {useEffect, useState} from 'react';
import PostForm from './components/PostForm';
import FetchWords from './components/FetchWords';

function App() {

  return (
    <div className="App">
      <header className="App-header">
        
        <PostForm />
        <FetchWords />
      </header>
    </div>
  );
}

export default App;