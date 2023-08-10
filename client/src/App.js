import React, { useState, useEffect } from 'react';
import { BrowserRouter as Route, Router } from 'react-router-dom';
import Home from './Home';
import PotionChallenge from './PotionChallenge';
import HousePoints from './HousePoints';
import Ingredients from './Ingredients';
import Potions from './Potions';
import './App.css';


function App(){
  const [potions, setPotions] = useState([]);

  useEffect(() => {
    const fetchPotions = async () => {
      try {
        const response = await fetch('http://localhost:4000/potions');
        if (!response.ok) {
          throw new Error('Error fetching potions');
        }
        const data = await response.json();
        setPotions(data);
      } catch (error) {
        console.error('Error fetching potions:', error);
        setPotions([]);
      }
    };

    fetchPotions();
  }, []);


  return (
    <Router>
      <div>
        <Route exact path="/" component={Home} />
        <Route path="/potionchallenge" component={PotionChallenge} />
        <Route path="/ingredients" component={Ingredients} />
        <Route path="/potions" components={Potions} />
        <Route path="housepoints" components={HousePoints} /> 
      </div>
    </Router>
  );
}

export default App;
