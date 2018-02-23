import React, { Component } from 'react';
import { BrowserRouter as Router, Switch, Route } from 'react-router-dom';

import Navbar from './components/Navbar';
import Home from './components/Home';
import About from './components/About';

class App extends Component {

render() {

  return (
    <Router>
      <div>
        <Navbar />
        <Switch>
          <Route exact path='/' component={Home} />
          <Route path='/about' component={About} />
        </Switch>
      </div>
    </Router>
    );
  }
}

export default App;
