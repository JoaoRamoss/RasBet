import React from 'react'
import Football from '../components/Football'

const FootballPage = ({updateState, state, api}) => {
  return (
    <Football state={state} api={api} updateState={updateState}/>
  )
}

export default FootballPage