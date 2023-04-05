import React from 'react'
import HeroSection from '../components/HeroSection';
import NavBarAssembled from '../components/NavBarAssm';
import { useEffect } from 'react';

const Homepage = ({updateState, state, api, type}) => {

  useEffect(() => {
    document.title = "RasBet"
  })

  return (
    <div>
      <NavBarAssembled state={state} api={api} type={type} updateState={updateState}/>
      <HeroSection/>
    </div>
  )
}

export default Homepage
