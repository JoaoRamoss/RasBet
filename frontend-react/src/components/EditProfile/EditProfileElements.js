import styled from "styled-components";

export const PageWrapper = styled.div`
    background-color: lightgray;
    width: 100vw;
    height: 100vh;
`

export const ProfileWrapper = styled.ul`
    background-color: #fafafa;
    box-shadow: 0px 0px 20px 0px rgba(0, 0, 0, 0.15);
    width: 70%;
    height: 100vh;
    margin-left: auto;
    margin-right: auto;
    padding-top: 15vh;
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

export const Horizontal = styled.div`
    background-color: lightgray;
    box-shadow: 0px 0px 20px 0px rgba(0, 0, 0, 0.15);
    width: 80%;
    height: 100px;
    margin-left: auto;
    margin-right: auto;
    border-radius: 30px;
    display: flex;
    margin-top: 40px;
    padding-right: 15px;
`

export const ProfileElement = styled.div`
    width: 90%;
    height: 100%;
    display: flex;
    flex-direction: column;
    padding-top: 10px;
    padding-bottom: 10px;
`

export const ProfileLine = styled.div`
    width: 100%;
    height: 50%;
    display: flex;
    padding-top: 10px;
    padding-bottom: 10px;
    padding-left: 20px;
    padding-right: 20px;
`

export const Label = styled.span`
    width: 25%;
    height: 100%;
    display: flex;
    align-items: center;
    font-size: 1.1vw;
    margin-right: 20px;
    border-right: 2px solid darkgray;
    color: #153b00;
`

export const Value = styled.span`
    width: 75%;
    height: 100%;
    display: flex;
    align-items: center;
    font-size: 1.1vw;
`

export const Input = styled.input`
    width: 75%;
    height: 100%;
    display: flex;
    align-items: center;
    box-shadow: 0px 0px 20px 0px rgba(0, 0, 0, 0.15);
    font-size: 1.1vw;
    outline: none;
    border: 0px;
    border-radius: 15px;
    padding-left: 10px;
`

export const Button = styled.button`
    background-color: #ea7336;
    box-shadow: 0px 0px 20px 0px rgba(0, 0, 0, 0.15);
    width: 10%;
    height: 70%;
    margin-left: auto;
    margin-top: auto;
    margin-bottom: auto;
    margin-right: auto;
    border-radius: 20px;
    border: 0px;
    font-size: 1.3vw;
    font-weight: bold;
    cursor: pointer;

    transition: 0.1s ease-in-out;
    &:hover{
        scale: 1.07;
        background-color: #d76026;
        transition: 0.2s ease-in-out;
    }
`