import React from 'react'
import Register from '../components/Register'
import { useEffect } from 'react'

const RegisterPage = ({api, updateState, type}) => {

  useEffect(() => {
    document.title = "RasBet - register"
  })

  return (
    <div>
      <Register api={api} updateState={updateState} type={type}/>
    </div>
  )
}

export default RegisterPage;
