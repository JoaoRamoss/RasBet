import styled from "styled-components";




export const PageHolder = styled.div`
    display: flex;
    height: 100vh;
    width: 100vw;
    background-color: lightgray;
`

export const TransferHistoryHolder = styled.div`
    margin-top: 10vh;
    background-color: #fafafa;
    box-shadow: 0px 0px 20px 0px rgba(0, 0, 0, 0.15);
    height: 80%;
    width: 60%;
    margin-top: 15vh;
    border-radius: 30px;
    display: flex;
    flex-direction: column;
    align-items: center;
    margin-left: auto;
    margin-right: auto;
    padding: 20px;
`

export const Title = styled.span`
    font-size: 2.2vw;
    font-weight: bold;
    color: #153b00;
`

export const WalletAmount = styled.span`
    font-size: 1.7vw;
    margin-top: 5%;
    font-weight: bold;
    color: #153b00;
    margin-bottom: 1%;
`

export const Divider = styled.div`
    background-color: #153b00;
    width: 90%;
    height: 3px;
    margin-bottom: 1%;
    margin-top: 1%;
`

export const Horizontal = styled.div`
    width: 90%;
    height: 5%;
    display: flex;
    justify-content: space-around;
    align-items: center;
    margin-left: auto;
    margin-right: auto;
`

export const HorizontalLine = styled.div`
    width: 100%;
    height: 10%;
    display: flex;
    justify-content: space-around;
    align-items: center;
    margin-left: auto;
    margin-right: auto;
    margin-bottom: 20px;
    border-bottom: 2px solid darkgray;
`

export const TableTitle = styled.span`
    font-size: 1.5vw;
    width: 30%;
    height: 100%
    margin-left: 190px;
    color: #153b00;
    font-weight: bold;
`

export const TransferList = styled.ul`
    width: 90%;
    height: 60%;
    justify-content: center;
    overflow-y: auto;
    overflow-x: hidden;

    ::-webkit-scrollbar {
        width: 10px;
        background: lightgray;
    }
    ::-webkit-scrollbar-thumb {
        border-radius: 10px;
        background-color:  darkgray; 
    }
`

export const TableContent = styled.span`
    width: 30%;
    font-size: 1.2vw;
`


export const TransferSideBar = styled.div`
    margin-top: 15vh;
    margin-left: 0px;
    margin-right: auto;
    height: 70vh;
    width: 25%;
    display: flex;
    flex-direction: column;
    justify-content: space-between;
`

export const TransferPopUp = styled.form`
    display: flex;
    background-color: #fafafa;
    box-shadow: 0px 0px 20px 0px rgba(0, 0, 0, 0.15);
    height: 45%;
    width: 100%;
    border-radius: 30px;
    flex-direction: column;
    align-items: center;
    justify-content: space-between;
    gap: 10%;
    padding: 5%;
`

export const AmountInput = styled.input`
    background-color: #fafafa;
    box-shadow: 0px 0px 20px 0px rgba(0, 0, 0, 0.15);
    outline: none;
    height: 25%;
    width: 70%;
    font-size: 20px;
    text-align: center;
    border-radius: 10px;
    border: 0px;
`

export const Button = styled.button`
    background-color: #ea7336;
    box-shadow: 0px 0px 20px 0px rgba(0, 0, 0, 0.15);
    width: 45%;
    height: 30%;
    font-size: 1.3vw;
    font-weight: bold;
    border-radius: 30px;
    border: 0px;
    margin-bottom: auto;
    cursor: pointer;

    transition: 0.1s ease-in-out;
    &:hover{
        scale: 1.07;
        background-color: #d76026;
        transition: 0.2s ease-in-out;
    }
`