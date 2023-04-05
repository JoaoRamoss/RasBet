import React from 'react';
import LoginForm from './LoginForm';

const Login = ({updateState, api}) => {
  
  return (
        <div>
           <LoginForm updateState={updateState} api={api}/>
        </div>
    );
};

export default Login
