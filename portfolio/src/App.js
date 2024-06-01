import './App.css';
import { useState, useEffect } from 'react';

import Cmd from './components/cmd';
import Dragable from './components/dragable';


function App() {

  return (
    <div className="App vbox">
        <Dragable>
          <Cmd />
        </Dragable>

        <Dragable>
          <Cmd />
        </Dragable>
    </div>
  );
}

export default App;
