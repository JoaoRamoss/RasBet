import React from 'react'
import NavBarAssembled from '../NavBarAssm'
import { GameList, GameWrapper, GameInfo, GameTitle, Info, Button } from './editGamesElements'
import { useState, useEffect } from 'react'



const Game = ({click, game}) => {

    const btn = game[10];
    let date = game[3].replace("T", "            ");
    date = date.replace(":00.000Z", "");

    return (
        <GameWrapper>
            <GameInfo>
                <GameTitle>{game[1]} - {game[2]}</GameTitle>
                <Info><pre>{date}            {game[10]}</pre></Info>
            </GameInfo>
            <Button type="button" className={`${btn === "ACTIVE" ? "active" : "inactive"}`} onClick={() => {click("ACTIVE", btn, game[0])}}>Active</Button>
            <Button type="button" className={`${btn === "WAIT" ? "active" : "inactive"}`} onClick={() => {click("WAIT", btn, game[0])}}>Wait</Button>
            <Button type="button" className={`${btn === "SLEEP" ? "active" : "inactive"}`} onClick={() => {click("SLEEP", btn, game[0])}}>Sleep</Button>
        </GameWrapper>
    )
}

function EditGames({updateState, state, api}) {

  const [games, setGames] = useState([]);

  const getData = async () => {
    const gg = await api.get("/api/get_all_games/football");
    setGames(gg.data.data);
  }

  useEffect(() => {
    getData();
  }, []);

  const click = async (n, btn, id) => {
    const res = await api.post("/api/set_games_states", {ids: [id], states: [n]});
    await getData();
  }

  return (
    <div style={{backgroundColor: "lightgray"}}>
        <NavBarAssembled state={state} api={api} current="editgames" updateState={updateState}/>
        <GameList>
            {
                games.map(g => {
                    if (g[4] === "FALSE") return <Game key={g[0]} click={click} game={g}/>
                })
            }
        </GameList>
    </div>
  )
}

export default EditGames