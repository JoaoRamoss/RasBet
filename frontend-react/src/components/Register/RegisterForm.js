import React, { useRef, useState } from 'react'
import { FormWrapper, GlobalStyle, StyledError, StyledForm,
     StyledInput, StyledButton, RasBetLogo, RasBetLogoOut,
      RasBetText, RasBetWrapper, NoAccount, NoAccountWrapper, 
      CheckMark, CheckWrapper, SumbitWrapper, CheckText} from './RegisterElements';
import { useNavigate } from 'react-router-dom';

const RegisterForm = ({api, updateState, type}) => {
    const delay = ms => new Promise(res => setTimeout(res, ms));

    const navigate = useNavigate();

    const ref = useRef();

    const [state, setState] = useState({
        username: '',
        password: '',
        email: '',
        birthdate: '',
        nif: '',
        token: ''
    });

    const [registred, setRegistred] = useState(false);

    const[error, setError] = useState('');

    const handleSubmit = async e => {
        e.preventDefault();
        if (validate(state) === true) {
          let post = await api.post('/api/register_' + type, {nif: state.nif, username: state.username, email: state.email, password: state.password, token: state.token});
          if (post.data.response === 'nif_taken') setError("The provided NIF is already in use")
          else if (post.data.response === 'username_taken') setError("Username already in use");
          else if (post.data.response === 'email_taken') setError("Email already in use");
          else if (post.data.response === 'token_error') setError("Invalid Token");
          else{
            setRegistred(true);
            await delay(1000);
            updateState(true, post.data.response, state.username);
            navigate("/");
          }
        }
    }

    const validate = state => {
        const passRegex = new RegExp(/^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)[a-zA-Z\d]{6,}$/)
        const emailRegex = new RegExp(/^\w+([\.-]?\w+)*@\w+([\.-]?\w+)*(\.\w{2,3})+$/)

        if (state.username === ''){ 
          setError("You need to provide an username")
          return false;
        }
        else if (emailRegex.test(state.email) === false) {
          setError("The provided email isn't valid")
          return false;
        }
        else if (state.password === ''){
           setError("You need to provide a password")
           return false;
        }
        else if (state.password.length < 6) {
          setError("The password must be at least 6 characters long")
          return false;
        }
        else if (passRegex.test(state.password) === false) {
          setError("The password must have an upper case letter and a number")
          return false;
        }
        else if (state.nif.length < 9) {
          setError("invalid NIF")
          return false;
        }
        else setError('');
        return true;
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
            <h2>REGISTER</h2>
            <label htmlFor="username"></label>
            <StyledInput type="text" name="username" placeholder='Username' value={state.username} onChange={handleInput}></StyledInput>
            <label htmlFor="email"></label>
            <StyledInput type="text" name="email" placeholder='E-Mail' value={state.email} onChange={handleInput}></StyledInput>
            <label htmlFor="password"></label>
            <StyledInput type="password" name="password" placeholder='Password' value={state.password} onChange={handleInput}></StyledInput>
            <label htmlFor="birthdate"></label>
            <StyledInput type="text" ref={ref} onFocus={() => {ref.current.type = "date"}} onBlur = {() => {ref.current.type = "text"}} placeholder="Birthdate" name="birthdate" value={state.birthdate} onChange={handleInput}></StyledInput>
            <label htmlFor="nif"></label>
            <StyledInput type="text" name="nif" placeholder="NIF" maxLength="9" value={state.nif} onChange={handleInput}></StyledInput>
            
            {type != "user" &&
              <StyledInput type="password" name="token" placeholder="TOKEN" maxLength="100" value={state.token} onChange={handleInput}></StyledInput>  
            }

            {error && (
                <StyledError>
                  <p>{error}</p>
                </StyledError>
            )}
            {!registred ? (
            <SumbitWrapper>
              <StyledButton type="submit">Register </StyledButton>
              <NoAccountWrapper>
                <div>Already have an account?</div>
                <NoAccount to="/login">Log in!</NoAccount>
              </NoAccountWrapper>
            </SumbitWrapper>) : 
            (
              <CheckWrapper>
                <CheckMark/>
                <CheckText>Success!</CheckText>
              </CheckWrapper>
            )
            }


          </StyledForm>
        </FormWrapper> 
    </div>
  );
}

export default RegisterForm;
