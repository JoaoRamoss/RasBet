import styled from "styled-components";

export const PageWrapper = styled.div`
    background-color: lightgray;
    width: 100vw;
    height: 100vh;
    display: flex;
`

export const OptionsWrapper = styled.ul`
    background-color: #fafafa;
    box-shadow: 0px 0px 20px 0px rgba(0, 0, 0, 0.15);
    width: 65%;
    height: 100vh;
    margin-left: auto;
    margin-right: auto;
    padding-top: 100px;
    overflow: auto;

    ::-webkit-scrollbar {
        width: 10px;
        background: lightgray;
    }
    ::-webkit-scrollbar-thumb {
        border-radius: 10px;
        background-color:  darkgray; 
    }
`

export const Horizontal = styled.form`
    background-color: lightgray;
    box-shadow: 0px 0px 20px 0px rgba(0, 0, 0, 0.1);
    width: 80%;
    height: 100px;
    margin-left: auto;
    margin-right: auto;
    border-radius: 30px;
    display: flex;
    align-items: center;
    margin-bottom: 80px;
`

export const OptionTitle = styled.div`
    width: 43%;
    height: 100%;
    display: flex;
    align-items: center;
    font-size: 1.3vw;
    padding-left: 50px;
`

export const Input = styled.input`
    box-shadow: 0px 0px 20px 0px rgba(0, 0, 0, 0.1);
    width: 37%;
    height: 60px;
    border-radius: 15px;
    font-size: 1.3vw;
    padding-left: 20px;
    border: 0px;
    text-align: center;
    outline: none;
    background-color: white;
`

export const Button = styled.button`
    background-color: #ea7336;
    width: 15%;
    height: 70%;
    margin-left: 40px;
    margin-right: 15px;
    border-radius: 20px;
    border: 0px;
    font-size: 1.5vw;
    font-weight: bold;
    cursor: pointer;

    transition: 0.1s ease-in-out;
    &:hover{
        scale: 1.07;
        background-color:#d76026;
        transition: 0.2s ease-in-out;
    }
`

export const NotifyWrapper = styled.form`
    background-color: #fafafa;
    width: 25%;
    height: 80%;
    margin-right: auto;
    margin-top: 15vh;
    border-radius: 35px;
    display: flex;
    flex-direction: column;
    box-shadow: 0px 0px 20px 0px rgba(0, 0, 0, 0.15);
    padding: 20px;
`

export const TextBox = styled.textarea`
    background-color: white;
    box-shadow: 0px 0px 20px 0px rgba(0, 0, 0, 0.15);
    width: 100%;
    height: 100%;
    resize: none;
    border: 0px;
    border-radius: 20px;
    font-size: 1.2vw;
    padding: 20px;
    outline: none;
`

export const SendButton = styled.button`
    background-color: #ea7336;
    margin-top: 10%;
    margin-left: auto;
    margin-right: auto;
    margin-bottom: auto;
    padding: 0;
    width: 35%;
    height: 20%;
    border-radius: 20px;
    border: 0px;
    font-size: 1.4vw;
    font-weight: bold;
    cursor: pointer;

    transition: 0.1s ease-in-out;
    &:hover{
        scale: 1.07;
        background-color:#d76026;
        transition: 0.2s ease-in-out;
    }
`