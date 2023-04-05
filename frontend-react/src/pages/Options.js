import React from 'react'
import Options from '../components/Options'

function OptionsPage({updateState, state, api}) {
  return (
    <Options state={state} api={api} updateState={updateState}/>
  )
}

export default OptionsPage