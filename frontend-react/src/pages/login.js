import React from 'react'
import Login from '../components/Login'
import { useEffect } from 'react'
 
const LoginPage = ({updateState, api}) => {

  useEffect(() => {
    document.title = "RasBet - login"
  })

  return (
    <div>
      <Login updateState={updateState} api={api}/>
    </div>
  )
}

export default LoginPage
