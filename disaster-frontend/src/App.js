import logo from './logo.svg';
import './App.css';
import React from 'react';
import { BrowserRouter as Router, Route, Switch } from 'react-router-dom';
import DisasterList from './components/DisasterList';
import DisasterDetail from './components/DisasterDetail';
import AlertList from './components/AlertList';

const App = () => {
  return (
      <Router>
          <Switch>
              <Route path="/" exact component={DisasterList} />
              <Route path="/disaster/:id" component={DisasterDetail} />
              <Route path="/alerts" component={AlertList} />
          </Switch>
      </Router>
  );
};

function App() {
  return (
    <div className="App">
      <header className="App-header">
        <img src={logo} className="App-logo" alt="logo" />
        <p>
          Edit <code>src/App.js</code> and save to reload.
        </p>
        <a
          className="App-link"
          href="https://reactjs.org"
          target="_blank"
          rel="noopener noreferrer"
        >
          Learn React
        </a>
      </header>
    </div>
  );
}

export default App;
