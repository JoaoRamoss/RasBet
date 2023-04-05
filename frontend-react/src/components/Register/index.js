import React from 'react'
import RegisterForm from './RegisterForm'

const Register = ({api, updateState, type}) => {
  return (
    <div>
      <RegisterForm api={api} updateState={updateState} type={type}/>
    </div>
  )
}

export default Register;
