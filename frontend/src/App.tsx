import React from 'react';
import { BrowserRouter as Router, Route, Switch } from 'react-router-dom';
import Home from './pages/Home';
import Profile from './pages/Profile';
import Community from './pages/Community';
import Login from './components/Auth/Login';
import Register from './components/Auth/Register';
import CommunityList from './components/Community/CommunityList';
import CommunityDetail from './components/Community/CommunityDetail';
import EthicalNotice from './components/Safeguards/EthicalNotice';

const App: React.FC = () => {
  return (
    <Router>
      <Switch>
        <Route path="/" exact component={Home} />
        <Route path="/profile" component={Profile} />
        <Route path="/community" exact component={CommunityList} />
        <Route path="/community/:id" component={CommunityDetail} />
        <Route path="/login" component={Login} />
        <Route path="/register" component={Register} />
        <Route path="/ethical-notice" component={EthicalNotice} />
      </Switch>
    </Router>
  );
};

export default App;