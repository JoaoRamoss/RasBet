import styled from 'styled-components';


export const Outcomes = styled.div`
    display: flex;
    justify-content: space-around;
    align-items: center;
    width: 70%;
    height: 100%;
`

export const VicWrapper = styled.button`
    width: 25%;
    height: 75%;
    display: flex;
    flex-direction: column;
    background-color: #fafafa;
    border: none;
    border-radius: 20px;
    box-shadow: 0px 0px 20px 0px rgba(0, 0, 0, 0.15);
    justify-content: center;
    align-items: center;
    cursor: pointer;

    transition: 0.1s ease-in-out;
    &:hover{
        scale: 1.07;
        background-color: #d76026;
        transition: 0.2s ease-in-out;
    }
    &.active {
        background-color: #ea7336;
    }
    
`

export const VicName = styled.div`
    font-size: 1vw;
    text-align: center;
    font-weight: bold;
    width: 90%;
    height: 45%;
    display: flex;
    justify-content: center;
    align-items: center;
    overflow: hidden;
    border-bottom: 2px solid darkgray;
`

export const VicOdd = styled.div`
    font-size: 1.2vw;
    font-weight: bold;
    width: 50%;
    height: 35%;
    display: flex;
    align-items: center;
    justify-content: center;
    margin: auto;
    box-shadow: 0px 0px 20px 0px rgba(0, 0, 0, 0.15);
    border-radius: 15px;
    background-color: #fafafa;
`

export const FollowBtn = styled.button`
    width: 30%;
    height: 70%;
    font-size: 1vw;
    font-weight: bold;
    box-shadow: 0px 0px 20px 0px rgba(0, 0, 0, 0.1);
    border-radius: 15px;
    border: 0px;
    margin-left: auto;
    margin-right: auto;
    cursor: pointer;
    
    transition: 0.1s ease-in-out;
    &:hover{
        color: white;
        scale: 1.07;
        background-color: #1c4000;
        transition: 0.2s ease-in-out;
    }
    &.active {
        &:hover{
            color: black;
            scale: 1.07;
            background-color: white;
            transition: 0.2s ease-in-out;
        }
        color: white;
        background-color: #1c4000;
    }
`