import styled, { createGlobalStyle, css, keyframes } from 'styled-components';
import {Link as LinkR} from 'react-router-dom'
import { IoIosCheckmarkCircle } from 'react-icons/io'
import { rollIn, fadeInLeft } from 'react-animations'

export const GlobalStyle = createGlobalStyle`
    html {
        height: 100vh;
    }

    body {
        height: 100vh;
        width: 100vw;
        background: linear-gradient(171deg, rgba(0,40,0,1) 0%, rgba(28,65,0,1) 53%, rgba(0,40,0,1) 100%);
        margin: 0;

    }

    h2{
        text-align: center;
        color: rgba(28,65,0,1);
        font-size: 1.7vw;
    }

    input:focus {
        outline-color: #ea7336;
    }

    p{
        text-align: center;
    }
`;


export const FormWrapper = styled.div`
    display: flex;
    justify-content: center;
    align-items: center;
    height: 100vh;
    padding: 0 20px;
`;

export const StyledForm = styled.form`
    display: flex;
    flex-direction: column;
    justify-content: space-around;
    width: 35vw;
    height: 80vh;
    min-height: 400px;
    min-width: 300px;
    padding: 40px;
    padding-bottom: 0px;
    background-color: #fff;
    border-radius: 25px;
    box-sizing: border-box;
    box-shadow:  0px 0px 20px 0px rgba(0, 0, 0, 1);
`;

export const StyledInput = styled.input`
    display: block;
    text-align: center;
    width: 100%;
    background-color: #fff;
    height: 8%;
    max-height: 30px;
    border-radius: 15px;
    border: 1.5px solid green;
    margin-left: auto;
    margin-right: auto;
    margin-top: 5px;
    margin-bottom: 5px;
    font-size: 0.7vw;
`;

export const StyledButton = styled.button`
    display: block;
    background-color: #ea7336;
    color: #333;
    font-size: 1.2vw;
    font-weight: bold;
    border: 0;
    border-radius: 15px;
    height: 25%;
    width: 100%;
    cursor: pointer;
    box-sizing: border-box;
    transition: 0.2s ease-in-out;
    align-self: center;
    margin-top: 2vh;

    &:hover{
        background-color:#d76026;
        transition: 0.2s ease-in-out;
    }
`;

export const StyledError = styled.div`
    color: red;
    font-weight: 400;
    align-self: center;
`;


export const RasBetLogo = styled.div`
  display: flex;
  max-width: 180px;
  z-index: 3;
  background: linear-gradient(171deg, rgba(0,40,0,1) 0%, rgba(28,65,0,1) 53%, rgba(0,40,0,1) 100%);
  width: 6vw;
  height: 3vw;
  border-radius: 0.5vw;
  justify-content: center;
  align-items: center;
`
export const RasBetText = styled.div`
  color:black;
  font-size: 1.3vw;
  font-weight: bold;
  background: linear-gradient(90deg, rgba(152,131,0,1) 0%, rgba(226,194,0,1) 51%, rgba(152,131,0,1) 100%);
    -webkit-background-clip: text;
    background-clip: text;
    -webkit-text-fill-color: transparent;
  text-align: center;
`;

export const RasBetLogoOut = styled.div`
  z-index: 3;
  background: linear-gradient(90deg, rgba(152,131,0,1) 0%, rgba(226,194,0,1) 51%, rgba(152,131,0,1) 100%);
  padding: 5px;
  border-radius: 0.7vw;
  cursor: pointer;
  box-shadow:  0px 0px 20px 0px rgba(0, 0, 0, 0.5);
`;

export const RasBetWrapper = styled(LinkR)`
    display:flex;
    max-width: 110px;
    text-decoration: none;
    cursor:pointer;
    transition: 0.1s ease-in-out;

    &:hover {
        transition: 0.1s ease-in-out;
        scale: 1.1;
    }
`;

export const NoAccountWrapper = styled.div`
    display:flex;
    flex-direction:column;
    font-size: .8rem;
    justify-content: center;
    align-items: center;
    gap: 5px;
    margin-top: 5%;
    margin-bottom: 10%;
`;

export const NoAccount = styled(LinkR)`
    color: rgba(28,65,0,1);
`
export const CheckWrapper = styled.div`
    display: flex;
    flex-direction: column;
    align-items: center;
    justify-content: center;
    gap: 10px;
`;


const rollAnimation = keyframes`${rollIn}`
export const CheckMark = styled(IoIosCheckmarkCircle)`
    color: green;
    scale: 4;
    margin: 30px;
    transition: all 0.2s ease-in-out;
    animation: 0.5s ${rollAnimation};
`;

const slide = keyframes`${fadeInLeft}`
export const CheckText = styled.div`
    font-size: 1vw;
    margin-bottom: 5%;
    animation: 0.5s ${slide}
`

export const SumbitWrapper = styled.div`
    transition: all 0.2s ease-in-out;
`