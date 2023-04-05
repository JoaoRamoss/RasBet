import React from 'react'
import Game from '../Game';
import NavBarAssembled from '../NavBarAssm'
import Boletim from '../Boletim'
import { useEffect, useState, useReducer } from 'react'; 
import { ContentWrapper, UnordList } from './FootballElements'
import { GameList } from '../EditGames/editGamesElements';



const Football = ({updateState, state, api}) => {

  const [games, setGames] = useState([]);
  const [selectedGames, setSelectedGames] = useState([]);
  const [btns, setBtns] = useState(true);
  const [, forceUpdate] = useReducer(x => x + 1, 0);

  useEffect(() => {
    const getData = async () => {
      const gg = await api.get("/api/get_active_games/football");
      setGames(gg.data.data);
    }
    getData();
  }, []);


  const addBet = (game, b) => {
    let ss = selectedGames;
    if (ss.length < 20){
      ss.push({game: game, bet: b});
    }
    setSelectedGames(ss);
    forceUpdate();
  }

  const removeBet = (id) => {
    let ss = selectedGames;
    for (var i = 0; i < ss.length; i++){
      if(ss[i].game[0] === id){
        ss.splice(i, 1);
      }
    }
    setSelectedGames(ss);
    forceUpdate();
  }

  const placeBet = async (amount) => {
    let game_ids = [];
    let betted_results = [];
    let ss = selectedGames;
    for (let i = 0; i < ss.length; i++){
      game_ids.push(ss[i].game[0]);
      betted_results.push(ss[i].bet);
    }
    const res = await api.post("api/bet", {game_ids : game_ids, betted_results : betted_results, amount : amount});
    setSelectedGames([]);
    setBtns(false);
    console.log(res.data);
  }

  return (
      <div>
        <NavBarAssembled state = {state} api={api} current="football" updateState={updateState}/>
        <ContentWrapper>
          <GameList>
          {
            games.map(g => {
              return <Game btns={btns} setBtns={setBtns} removeBet={removeBet} addBet={addBet} key={g[0]} game={g} api={api}/>
            })
          }
          </GameList>
          <Boletim selectedGames={selectedGames} placeBet={placeBet} state={state} api={api}/>
        </ContentWrapper>
      </div>
  )
}

export default Football;
