import styled from 'styled-components';
import { VscArrowLeft, VscArrowRight } from 'react-icons/vsc'


export const BetHistoryHolder = styled.div`
    background-color: #fafafa;
    box-shadow: 0px 0px 20px 0px rgba(0, 0, 0, 0.15);
    width: 65vw;
    height: 80vh;
    margin-left: auto;
    margin-right: auto;
    border-radius: 30px;
    display: flex;
    justify-content: center;
    align-items: center;
`

export const LeftArrow = styled(VscArrowLeft)`
    width: 4vw;
    height: 4vw;
    border-radius: 50%;
    border: 0px;
    box-shadow: 0px 0px 20px 0px rgba(0, 0, 0, 0.15);
    margin-left: 2%;
    padding: 5px;
    color: darkgray;
    cursor: pointer;
`

export const MainContent = styled.div`
    height: 100%; 
    width: 90%;
    display: flex;
    flex-direction: column;
    align-items: center;
    justify-content: space-around;
    padding-bottom: 3%;
    padding-top: 1%;
`

export const Username = styled.span`
    font-size: 3vw;
    color: #153b00;
    font-weight: bold;
`

export const HistoryTitle = styled.span`
    font-size: 2vw;
    color: #153b00;
    font-weight: bold;
`

export const SeparatorLine = styled.div`
    background-color: darkgray;
    width: 90%;
    height: 3px;
    border-radius: 4px;
`


export const RightArrow = styled(VscArrowRight)`
    width: 4vw;
    height: 4vw;
    border-radius: 50%;
    box-shadow: 0px 0px 20px 0px rgba(0, 0, 0, 0.15);
    cursor: pointer;
    border: 0px;
    margin-right: 2%;
    color: darkgray;
    padding: 5px;
`

export const BetWrapper = styled.div`
    background-color: #fafafa;
    box-shadow: 0px 0px 20px 0px rgba(0, 0, 0, 0.15);
    width: 95%;
    height: 60%;
    border-radius: 20px;
    display: flex;
    align-items: center;
`

export const BetList = styled.ul`
    width: 50%;
    height: 90%;
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

export const BetRight = styled.div`
    width: 50%;
    height: 90%;
    display: flex;
    flex-direction: column;
    border-left: 3px solid darkgray;
`

export const AmountWrapper = styled.div`
    width: 100%;
    height: 50%;
    display: flex;
    flex-direction: row;
    justify-content: space-between;
    align-items: center;
`

export const AmountText = styled.span`
    margin-left: 15%;
    font-size: 2vw;
`

export const AmountValue = styled.span`
    margin-right: 15%;
    font-size: 2vw;
    color: #153b00;
    font-weight: bold;
`

export const TotalWrapper = styled.div`
    width: 100%;
    height: 50%;
    display: flex;
    flex-direction: row;
    justify-content: space-between;
    align-items: center; 
`

export const CashOutButtonWrapper = styled.div`
    width: 100%;
    height: 50%;
    display: flex;
    flex-direction: row;
    justify-content: center;
    align-items: center; 
`

export const CashOutButton = styled.div`
    width: 40%;
    height: 50%;
    background-color: #ea7336;
    border-radius: 20px;
    display: flex;
    align-items: center;
    justify-content: center;
    font-size: 2vw;
    font-weight: bold;
    border: 3px solid 153b00;
    cursor: pointer;

    transition: 0.1s ease-in-out;
    &:hover{
        scale: 1.07;
        background-color: #d76026;
        transition: 0.2s ease-in-out;
    }
`


export const TotalText = styled.span`
    margin-left: 15%;
    font-size: 2vw;
`

export const TotalValue = styled.span`
    margin-right: 15%;
    font-size: 2vw;
    color: #ea7336;
    font-weight: bold;
`


export const MiniBetWrapper = styled.div`
    width: 100%;
    height: 30%;
    display: flex;
    flex-direction: column;
    align-items: center;
`

export const MiniBetTitle = styled.span`
    height: 50%;
    display: flex;
    align-items: center;
    padding-left: 20px;
    font-size: 1.5vw;
    font-weight: bold;
    color: #153b00;
    width: 100%;
`

export const MiniBetResult = styled.span`
    height: 40%;
    width: 90%;
    padding-left: 30px;
    font-size: 1.2vw;
    border-bottom: 3px solid darkgray;
`