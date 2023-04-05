import React from 'react'
import NavBarAssembled from '../NavBarAssm';
import { BetHistoryHolder, LeftArrow, MainContent, Username, HistoryTitle,
          SeparatorLine, RightArrow, BetWrapper, BetList, BetRight, AmountWrapper,
          AmountText, AmountValue, TotalWrapper, TotalText, TotalValue,
          MiniBetWrapper, MiniBetTitle, MiniBetResult, CashOutButtonWrapper, CashOutButton } from './BetHistoryElements'
import { useState, useEffect } from 'react';


const MiniBet = ({b}) => {

  const getVencedor = () => {
    if (b[4] === "WAIT") return "Running";
    else if (b[3] === 1) return "Draw";
    else if (b[3] === 0) return "Winner: " + b[0];
    else if (b[3] === 2) return "Winner: " + b[1];
  }

  return (
    <MiniBetWrapper>
      <MiniBetTitle>{b[0]} - {b[1]}</MiniBetTitle>
      <MiniBetResult>{getVencedor()}</MiniBetResult>
    </MiniBetWrapper>
  )
}

const Bet = ({bet, api}) => {
  
  const [onGoing, setOnGoing] = useState(false);

  if (bet[4] === "WAIT" && !onGoing) setOnGoing(true);
  else if (bet[4] != "WAIT" && onGoing) setOnGoing(false);

  const cashout = async () => {
    const res = await api.post("/api/cash_out", {bet_id : bet[0]});
    if (res.data.response === "valid"){
      setOnGoing(false);
      bet[4] = "CASHED_OUT";
    }
  }

  const getTotalGains = (n) => {
    if (n === 1 && bet[4] === "CASHED_OUT"){
      return bet[1] / 2;
    }
    else if (n === 1 && bet[4] === "WIN"){
      return bet[1] * bet[2];
    }
    else if (n === 1){
      return 0;
    }
    else if (n === 0 && bet[4] != "CASHED_OUT"){
      return "Total Gains";
    }
    else if (n === 0){
      return "Cashout";
    }
  }

  return (
    <BetWrapper>
      <BetList>
        {
          bet[5].map(b => {
            return <MiniBet key={b[0]} b={b}/>
          })
        }
      </BetList>
      <BetRight>
          <AmountWrapper>
            <AmountText>Betted Amount</AmountText>
            <AmountValue>{bet[1]}€</AmountValue>
          </AmountWrapper>
          {!onGoing &&
          <TotalWrapper>
            <TotalText>{getTotalGains(0)}</TotalText>
            <TotalValue>{getTotalGains(1)}€</TotalValue>
          </TotalWrapper>
          }
          {onGoing &&
            <CashOutButtonWrapper>
              <CashOutButton onClick={cashout}>Cashout</CashOutButton>
            </CashOutButtonWrapper>
          }
      </BetRight>
    </BetWrapper>
  )
}

const BetHistory = ({updateState, state, api}) => {

  const [history, setHistory] = useState([]);
  const [current, setCurrent] = useState(0);

  const getData = async () => {
    const hist = await api.get("/api/bet_history");
    setHistory(hist.data.data.reverse());
  }

  useEffect(() => {
    getData();
  }, []);

  const goRight = () => {
    if (current !== history.length - 1){
      setCurrent(current + 1);
    }
  }

  const goLeft = () => {
    if(current !== 0){
      setCurrent(current - 1);
    }
  }

  const date = history[current] !== undefined ? history[current][3].split(" ")[0] : "";

  return (
    <div style={{backgroundColor: "lightgray", height: "100vh", paddingTop: "15vh"}}>
      <NavBarAssembled state={state} api={api} current="bethistory" updateState={updateState}/>
      <BetHistoryHolder>
        <LeftArrow onClick={goLeft}/>
        <MainContent>
          <Username>Bet History</Username>
          <HistoryTitle>{date}</HistoryTitle>
          <SeparatorLine/>
          {history.length > 0 &&
           <Bet api={api} bet={history[current]}/>
          }
        </MainContent>
        <RightArrow onClick={goRight}/>
      </BetHistoryHolder>
    </div>
  )
}

export default BetHistory;
