import React from 'react'
import EditGames from '../components/EditGames'

function EditGamesPage({updateState, state, api}) {
  return (
    <div>
        <EditGames state={state} api={api} updateState={updateState}/>
    </div>
  )
}

export default EditGamesPage