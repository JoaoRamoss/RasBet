import React, { useState } from 'react'
import { FormWrapper, GlobalStyle, StyledError, StyledForm,
     StyledInput, StyledButton, RasBetLogo, RasBetLogoOut,
      RasBetText, RasBetWrapper, NoAccount, NoAccountWrapper,
    CheckWrapper, CheckMark, CheckText} from './LoginElements';
import { useNavigate } from 'react-router-dom';

const LoginForm = ({updateState, api}) => {
  const delay = ms => new Promise(res => setTimeout(res, ms));
    const navigate = useNavigate();
    const [state, setState] = useState({
        username: '',
        password: ''
    });

    const[error, setError] = useState('');

    const[loggedIn, setLoggedIn] = useState(false);

    const handleSubmit = async e => {
        e.preventDefault();
        validate(state);
        let post = await api.post('/api/login', {username: state.username, password: state.password});
        if (post.data.response === 'username_error') {
          setError("Invalid username");
        }
        else if (post.data.response === "password_error") {
          setError("Incorrect password")
        }
        else {
          setLoggedIn(true);
          updateState(true, post.data.response, state.username);
          await delay(1000);
          navigate("/");
        }
    }

    const validate = state => {
        if (state.username === '') setError("You need to provide a username");
        else if (state.password === '') setError("You need to provide a password");
        else setError('');
    }

    const handleInput = e => {
        const inputName = e.target.name;
        const value = e.target.value;

        setState(prev => ({...prev, [inputName]: value}))
        setError('');
    }

  return (
    <div>
        <GlobalStyle/>
        <FormWrapper>
          <StyledForm onSubmit={handleSubmit}>
            <RasBetWrapper to="/">
                <RasBetLogoOut>
                <RasBetLogo>
                    <RasBetText>RasBet</RasBetText>
                </RasBetLogo>
                </RasBetLogoOut>
            </RasBetWrapper>
            <h2>WELCOME</h2>
            <label htmlFor="username"></label>
            <StyledInput type="text" name="username" placeholder='Username' value={state.username} onChange={handleInput}></StyledInput>
            <label htmlFor="email"></label>
            <StyledInput type="password" name="password" placeholder='Password' value={state.password} onChange={handleInput}></StyledInput>
            {error && (
                <StyledError>
                  <p>{error}</p>
                </StyledError>
            )}
            {!loggedIn ? (
            <div>
            <StyledButton type="submit">Log in </StyledButton>
            <NoAccountWrapper>
              <div>Don't have an account?</div>
              <NoAccount to="/register">Register now!</NoAccount>
            </NoAccountWrapper>
            </div>
            ) : 
              (
                <CheckWrapper>
                <CheckMark/>
                <CheckText>Logged in!</CheckText>
              </CheckWrapper>
              )
            }


          </StyledForm>
        </FormWrapper> 
    </div>
  );
}

export default LoginForm;
