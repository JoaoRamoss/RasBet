import React from 'react'
import { useEffect, useState } from 'react'
import { BoletimWrapper, BoletimText, BetButton, BetList, ListItem, Game, BetDesc, Cotas, BetWrapper,
          BottomMenu, AmountWrapper, Amount, StyledInput, TotalGains, TotalGainsValue, TotalGainsWrapper, SecondWrapper, 
          TopWrapper, Euro} from './BoletimElements'



const BetItem = ({home, away, type, odd}) => {
  return (
    <ListItem>
      <Game>{home} - {away}</Game>
      <BetWrapper>
        <BetDesc>{type}</BetDesc>
        <Cotas>Odd: {odd}</Cotas>
      </BetWrapper>
    </ListItem>
  )
}


const Boletim = ({selectedGames, placeBet, state, api}) => {
  
  const [currentAmount, setCurrentAmount] = useState(0);

  const finalCota = (ss) => {
    let s = 1;
    for(let i = 0; i < ss.length; i++){
      s = s * ss[i].game[7 + ss[i].bet];
    }
    return s;
  }

  const changeAmount = event => {
    setCurrentAmount(event.target.value);
  }

  const bet = () => {
    placeBet(currentAmount);
    setCurrentAmount(0);
  }
  
  return (
    <div>
        <BoletimWrapper>
          <BoletimText>Bet Slip</BoletimText>
          <BetList>
            {
              selectedGames.map(g => {
                return <BetItem key={g.game[0]} home={g.game[1]} away={g.game[2]} type={g.bet === 1 ? "Draw" : (g.bet === 0 ? "Winner: " + g.game[1] : "Winner: " + g.game[2])} odd={g.game[7 + g.bet]}/>
              })
            }
          </BetList>
          <BottomMenu id="1" onSubmit={(e) => {e.preventDefault(); bet(); e.target.reset()}}>
            <TopWrapper>
              <Cotas>Odd: {finalCota(selectedGames)}</Cotas>
              <AmountWrapper>
                <Amount>Amount</Amount>
                <StyledInput type="text" name="amount" placeholder='0' onChange={changeAmount}/>
                <Euro> €</Euro>
              </AmountWrapper>
            </TopWrapper>
            <SecondWrapper>
              <TotalGainsWrapper>
                <TotalGains>Total gains:</TotalGains>  
                <TotalGainsValue placeholder="0">{currentAmount * finalCota(selectedGames)}</TotalGainsValue>
              </TotalGainsWrapper>  
              <BetButton form="1" type="submit">Bet</BetButton>
            </SecondWrapper>
          </BottomMenu>
        </BoletimWrapper>
    </div>
  )
}

export default Boletim