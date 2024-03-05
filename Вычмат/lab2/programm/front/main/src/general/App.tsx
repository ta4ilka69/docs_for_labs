import React from 'react';
import ErrorPage from '../errorPage/ErrorPage';
import './App.css'
import { BrowserRouter as Router, Route, Routes} from 'react-router-dom';
import Lab2 from '../lab2/Lab2';
import Home from './Home';
import Linear from '../lab2/Linear';
import LSystem from '../lab2/LSystem';

const App = () => {
  return (
    <Router>
      <Routes>
        <Route path="/lab2" element={<Lab2/>} />
        <Route path="/lab2/linear" element={<Linear/>} />
        <Route path="/lab2/system" element={<LSystem/>} />
        <Route path="/" element={<Home/>} />
        <Route path="*" element={<ErrorPage />} />
      </Routes>
    </Router>
  );
};

export default App;
