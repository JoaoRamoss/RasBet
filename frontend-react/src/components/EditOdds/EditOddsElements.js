import styled from "styled-components";



export const Odd = styled.div`
    background-color: #fafafa;
    box-shadow: 0px 0px 20px 0px rgba(0, 0, 0, 0.15);
    display: flex;
    flex-direction: column;
    width: 18%;
    height: 80%;
    margin: 15px;
    border-radius: 20px;
`

export const OddTitle = styled.span`
    height: 40%;
    width: 100%;
    display: flex;
    justify-content: center;
    padding: 5px;
    text-align: center;
    align-items: center;
    font-size: 0.9vw;
    font-weight: bold;
`

export const OddInput = styled.input`
    box-shadow: 0px 0px 20px 0px rgba(0, 0, 0, 0.15);
    height: 30%;
    width: 80%;
    border-radius: 10px;
    outline: none;
    font-size: 1vw;
    text-align: center;
    font-weight: bold;
    margin-left: auto;
    margin-right: auto;
    border: 0px;
`

export const Button = styled.button`
    background-color: #ea7336;
    box-shadow: 0px 0px 20px 0px rgba(0, 0, 0, 0.15);
    font-size: 1.5vw;
    font-weight: bold;
    width: 15%;
    height: 65%;
    margin: 10px;
    margin-right: 20px;
    border-radius: 19px;
    border: 0px;
    cursor: pointer;

    transition: 0.1s ease-in-out;
    &:hover{
        scale: 1.07;
        background-color: #d76026;
        transition: 0.2s ease-in-out;
    }
`

export const Sugestion = styled.span`
    height: 20%;
    display: flex;
    justify-content: center;
    align-items: center;
    font-size: 1vw;
    margin-top: 3px;
`

export const SideWrapper = styled.div`
    width: 25%;
    padding-top: 11%;
`

export const PageWrapper = styled.div`
    display: flex;
    height: 100vh;
    width: 100vw;
`

export const GameList = styled.ul`
    background-color: #fafafa;
    box-shadow: 0px 0px 20px 0px rgba(0, 0, 0, 0.15);
    width: 70%;
    height: 100%;
    padding-top: 100px;
    padding-bottom: 100px;
    margin-left: auto;
    margin-right: auto;
    overflow: auto;

    ::-webkit-scrollbar {
        width: 10px;
        background: lightgray;
        border-radius: 10px;
    }
    ::-webkit-scrollbar-thumb {
        border-radius: 10px;
        background-color:  darkgray; 
    }
`

export const BkmTable = styled.ul`
    background-color: #fafafa;
    box-shadow: 0px 0px 20px 0px rgba(0, 0, 0, 0.1);
    width: 80%;
    height: 80%;
    border-radius: 30px;
    margin-left: auto;
    margin-right: auto;
    overflow-y: auto;
    overflow-x: hidden;

    ::-webkit-scrollbar {
        width: 0px;
    }
`


export const BKMWrapper = styled.button`
    background-color: #fafafa;
    height: 75px;
    width: 100%;
    font-size: 1.8vw;
    border-top: 0px;
    border-left: 0px;
    border-right: 0px;
    border-bottom: 2px solid darkgray;
    cursor: pointer;

    transition: 0.1s ease-in-out;
    &:hover{
        scale: 1.07;
        background-color: lightgray;
        transition: 0.2s ease-in-out;
    }

    &.active {
        background-color: #ea7336;
    }
`