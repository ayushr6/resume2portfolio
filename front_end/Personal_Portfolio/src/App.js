import './App.css';
import Header from './components/header/Header';
import Home from './components/home/Home';
import About from './components/about/About';
import Skills from './components/skills/Skills';
import Qualifications from './components/qualifications/Qualifications';
import Footer from './components/footer/Footer';

import Work from './components/work/Work';
import React, { useEffect, useState } from 'react';
import axios from "axios";
// http://127.0.0.1:8000/api/user-details/2/
const App = () => {
  const [data, setData] = useState([]);

  useEffect(() => {
    const fetchData = async () => {
      try {
        const response = await axios.get('http://127.0.0.1:8000/api/user-details/2/');
        setData(response.data);
        console.log('API Response:', response.data);
      } catch (error) {
        console.error('Error fetching data:', error);
      }
    };

    fetchData();
  }, []);

  return (
    <>
      <Header />
      <main className='main'>
        <Home data={data} />
        <About />
        <Skills />
        <Qualifications />
        <Work />
        <Footer />
      </main>
    </>
  );
};

export default App;
