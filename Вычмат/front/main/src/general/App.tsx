import React from 'react';
import ErrorPage from '../errorPage/ErrorPage';
import './App.css'
import { BrowserRouter as Router, Route, Routes} from 'react-router-dom';
import Lab2 from '../lab2/Lab2';
import Home from './Home';
import Linear from '../lab2/Linear';
import LSystem from '../lab2/LSystem';
import Lab3 from '../lab3/Lab3';
import Lab4 from '../lab4/Lab4';
import Lab5 from '../lab5/Lab5';

const App = () => {
  return (
    <Router>
      <Routes>
        <Route path="/lab2" element={<Lab2/>} />
        <Route path="/lab2/linear" element={<Linear/>} />
        <Route path="/lab2/system" element={<LSystem/>} />
        <Route path="/" element={<Home/>} />
        <Route path="/lab3" element={<Lab3/>} />
        <Route path="/lab4" element={<Lab4/>} />
        <Route path="/lab5" element={<Lab5/>} />
        <Route path="*" element={<ErrorPage />} />
      </Routes>
    </Router>
  );
};

export default App;
