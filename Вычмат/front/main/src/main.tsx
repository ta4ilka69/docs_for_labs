import React from 'react'
import ReactDOM from 'react-dom/client'
import App from './general/App.tsx'
import './index.css'
import Header from './general/Header.tsx'
import Footer from './general/Footer.tsx'

ReactDOM.createRoot(document.getElementById('root')!).render(
  <React.StrictMode>
    <Header/>
    <App />
    <Footer/>
  </React.StrictMode>,
)
