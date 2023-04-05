import React from 'react'
import EditOdds from '../components/EditOdds'

function EditOddsPage({updateState, state, api}) {
  return (
    <EditOdds state={state} api={api} updateState={updateState}/>
  )
}

export default EditOddsPage