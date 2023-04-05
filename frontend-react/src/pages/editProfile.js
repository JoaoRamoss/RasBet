import React from 'react'
import EditProfile from '../components/EditProfile'

function EditProfilePage({updateState, setState, state, api}) {
  return (
    <EditProfile setState={setState} state={state} api={api} updateState={updateState}/>
  )
}

export default EditProfilePage