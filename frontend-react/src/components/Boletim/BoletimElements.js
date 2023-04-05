import styled from 'styled-components'


export const BoletimWrapper = styled.div`
    height: 80vh;
    width: 25vw;
    margin-left: 0px;
    margin-right: 1vw;
    margin-top: 15vh;
    border-radius: 30px;
    background-color: #fafafa;
    display: flex;
    flex-direction: column;
    align-items: center;
    justify-content: space-between;
    padding-top: 10px;
    padding-bottom: 20px;
`

export const BoletimText = styled.p`
    font-size: 2vw;
    display: flex;
    align-items: center;
    justify-content: center;
    width: 100%;
    margin-bottom: 10px;
`

export const BetList = styled.ul`
    height: 75%;
    width: 90%;
    margin-left: auto;
    margin-right: auto;
    border-radius: 20px;
    box-shadow: 0px 0px 20px 0px rgba(0, 0, 0, 0.15);
    padding-top: 10px;
    overflow: auto;
    background-color: #fafafa;
    margin-bottom: 20px;

    ::-webkit-scrollbar {
        width: 0px;
    }
`

export const BottomMenu = styled.form`
    background-color: #fafafa;
    box-shadow: 0px 0px 20px 0px rgba(0, 0, 0, 0.15);
    width: 85%;
    height: 25%;
    margin-right: auto;
    margin-left: auto;
    border-radius: 20px;
    display: flex;
    flex-direction: column;
    padding-top: 10px;
    padding-bottom: 10px;
`

export const TopWrapper = styled.div`
    display: flex;
    height: 50%;
    align-items: center;
    justify-content: space-between;
    margin-bottom: 10px;
`

export const Cotas = styled.span`
    border: 1px solid black;
    border-radius: 7px;
    padding: 10px;
    font-size: 0.7vw;
    margin-left: 5%;
`

export const AmountWrapper = styled.span`
    display: flex;
    border: 1px solid darkgrey;
    align-items: center;
    border-radius: 5px;
    width: 55%;
    height: 75%;
    margin-right: 5%;
`

export const Amount = styled.div`
    margin-right: 10px;
    margin-left: 10px;
    color: darkgray;
    font-size: 0.8vw;
`

export const StyledInput = styled.input`
    text-align: center;
    border: none;
    outline: none;
    box-shadow: 0px 0px 20px 0px rgba(0, 0, 0, 0.15);
    border-radius: 5px;
    height: 80%;
    width: 45%;
    font-size: 1vw;
    margin-right: 10px;
`

export const Euro = styled.div`
    font-size: 1vw;
    color: darkgray;
    margin-right: 10px;
`

export const SecondWrapper = styled.div`
    display: flex;
    height: 50%;
    align-items: center;
    justify-content: space-between;
    padding-left: 5%;
    padding-right: 5%;
`

export const TotalGainsWrapper = styled.div`
    display: flex;
    flex-direction: column;
`

export const TotalGains = styled.div`
    text-align: center;
    font-size: 0.9vw;
    margin-bottom: 5px;
`

export const TotalGainsValue = styled.div`
    text-align: center;
    font-size: 1vw;
    color: #ea7336;
`

export const BetButton = styled.button`
    width: 50%;
    height: 100%;
    background-color: #ea7336;
    border: 0px;
    border-radius: 15px;
    font-weight: bold;
    font-size: 1.1vw;
    cursor: pointer;
    margin-bottom: 3px;

    transition: 0.1s ease-in-out;
    &:hover{
        scale: 1.07;
        background-color: #d76026;
        transition: 0.2s ease-in-out;
    }
`

export const ListItem = styled.div`
    background-color: #fafafa;
    display: flex;
    flex-direction: column;
    justify-content: center;
    box-shadow: 0px 0px 20px 0px rgba(0, 0, 0, 0.15);
    width: 85%;
    height: 80px;
    margin-left: auto;
    margin-right: auto;
    margin-bottom: 15px;
    border-radius: 10px;
`

export const Game = styled.div`
    border-bottom: 1px solid black;
    width: 100%;
    padding-left: 20px;
    padding-right: 20px;
    font-weight: bold;
    font-size: 0.9vw;
    height: 40%;
    display: flex;
    align-items: center;
`

export const BetWrapper = styled.div`
    height: 60%;
    display: flex;
    align-items: center;
    justify-content: space-between;
    padding-left: 20px;
    padding-right: 20px;
`

export const BetDesc = styled.span`
    font-size: 0.8vw;
`









