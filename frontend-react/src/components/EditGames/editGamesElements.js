import styled from "styled-components";


export const GameList = styled.ul`
    background-color: #fafafa;
    box-shadow: 0px 0px 20px 0px rgba(0, 0, 0, 0.15);
    width: 70vw;
    height: 100vh;
    margin-left: auto;
    margin-right: auto;
    padding-top: 10vh;
    padding-bottom: 100px;
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

export const GameWrapper = styled.form`
    background-color: lightgray;
    box-shadow: 0px 0px 20px 0px rgba(0, 0, 0, 0.15);
    width: 90%;
    height: 100px;
    margin-left: auto;
    margin-right: auto;
    margin-top: 40px;
    display: flex;
    justify-content: space-between;
    border-radius: 30px;
    align-items: center;
`

export const GameInfo = styled.div`
    width: 60%;
    height: 100%;
    display: flex;
    flex-direction: column;
`

export const GameTitle = styled.span`
    height: 50%;
    display: flex;
    align-items: center;
    font-size: 1.6vw;
    padding-left: 15px;
    margin-left: 15px;
    border-bottom: 2px solid darkgray;
    overflow: hidden;
`

export const Info = styled.span`
    height: 50%;
    padding-left: 30px;
    font-size: 1.2vw;
    display: flex;
    align-items: center;
`

export const Button = styled.button`
    background-color: #fafafa;
    box-shadow: 0px 0px 20px 0px rgba(0, 0, 0, 0.15);
    width: 16.7%;
    height: 60%;
    margin: 20px;
    border-radius: 20px;
    font-size: 1.2vw;
    font-weight: bold;
    border: 0px;
    cursor: pointer;

    transition: 0.1s ease-in-out;
    &:hover{
        scale: 1.07;
        background-color: white;
        transition: 0.2s ease-in-out;
    }
    &.active {
        background-color: #ea7336;
    }
`

