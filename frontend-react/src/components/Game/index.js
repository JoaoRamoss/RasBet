import React from 'react'
import { useState, useEffect } from 'react';
import { GameInfo, GameTitle, Info, GameWrapper } from '../EditGames/editGamesElements';

import { Outcomes, VicWrapper, VicName, VicOdd, FollowBtn } from './GameElements'



const Game = ({btns, setBtns, removeBet, addBet, game, api}) => {

  const [pressedHome, setPressedHome] = useState(false);
  const [pressedTie,  setPressedTie]  = useState(false);
  const [pressedAway, setPressedAway] = useState(false);
  const [follows,     setFollows]     = useState(false);

  useEffect(() => {
    const getData = async () => {
      const gg = await api.post("/api/check_follows_game", {"game_id" : game[0]});
      setFollows(gg.data.data === "true");
    }
    getData();
  }, []);

  const getBtnClass = (n) => {
    if (n === 0){
      if (pressedHome && btns){
        return "active"
      }
      else if (!btns && pressedHome){
        setPressedHome(false);
      }
      return "inactive"
    }
    else if (n === 1){
      if (pressedTie && btns){
        return "active"
      }
      else if (!btns && pressedTie){
        setPressedTie(false);
      }
      return "inactive"
    }
    else if (n === 2){
      if (pressedAway && btns){
        return "active"
      }
      else if (!btns && pressedAway){
        setPressedAway(false);
      }
      return "inactive"
    }
  }

  const followClass = () => {
    if (follows) return "active";
    else return "inactive"
  }

  const followName = () => {
    if (follows) return "Unfollow"
    else return "Follow"
  }

  const toggleFollow = async () => {
    if (follows){
      const res = await api.post("/api/unfollow_game", {"game_id" : game[0]});
      if (res.data.response === "valid") setFollows(false);
    }
    else {
      const res = await api.post("/api/follow_game", {"game_id" : game[0]});
      if (res.data.response === "valid") setFollows(true);
    }
  }

  let date = game[3].replace("T", "            ");
  date = date.replace(":00.000Z", "");

  return (
    <GameWrapper>
      <GameInfo>
        <GameTitle>{game[1]} - {game[2]}</GameTitle>
        <Info>
          <pre>{date}</pre>
          <FollowBtn type="button" className={followClass()} onClick={() => {toggleFollow()}}>{followName()}</FollowBtn>
        </Info>
      </GameInfo>
      <Outcomes>
          <VicWrapper type="button" className={getBtnClass(0)} onClick={() => {
              setBtns(true);
              setPressedAway(false);
              setPressedTie(false);
              setPressedHome(!pressedHome);
              removeBet(game[0]);
              if (!pressedHome) addBet(game, 0);
          }}>
              <VicName>{game[1]}</VicName>
              <VicOdd>{game[7]}</VicOdd>
          </VicWrapper>
          <VicWrapper type="button" className={getBtnClass(1)} onClick={() => {
              setBtns(true);
              setPressedTie(!pressedTie);
              setPressedAway(false);
              setPressedHome(false);
              removeBet(game[0]);
              if (!pressedTie) addBet(game, 1);
          }}>
              <VicName>Draw</VicName>
              <VicOdd>{game[8]}</VicOdd>
          </VicWrapper>
          <VicWrapper type="button" className={getBtnClass(2)} onClick={() => {
              setBtns(true);
              setPressedAway(!pressedAway);
              setPressedTie(false);
              setPressedHome(false);
              removeBet(game[0]);
              if (!pressedAway) addBet(game, 2);
          }}>
              <VicName>{game[2]}</VicName>
              <VicOdd>{game[9]}</VicOdd>
          </VicWrapper>
      </Outcomes>
    </GameWrapper>
  )
}

export default Game;
