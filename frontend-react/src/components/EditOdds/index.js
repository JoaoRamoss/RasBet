import React, { useEffect, useState } from 'react'
import { GameInfo, GameTitle, GameWrapper, Info } from '../EditGames/editGamesElements'
import NavBarAssembled from '../NavBarAssm'
import { Odd, OddTitle, OddInput, Button, Horizontal, Sugestion, SideWrapper, PageWrapper,
        BkmTable, BKMWrapper, GameList } from './EditOddsElements'


const Game = ({sendOdd, game, sugs, bkm}) => {

    const type = "h2h";
    const [home, setHome] = useState(game[7]);
    const [tie,  setTie]  = useState(game[8]);
    const [away, setAway] = useState(game[9]);

    const getSugestion = (s) => {
        for (let i = 0; i < sugs.length; i++){
            if (sugs[i][0] === s && sugs[i][2] === type && sugs[i][3] === bkm){
                return sugs[i][1];
            }
        }
        return "unknown";
    }

    const changeHome = (event) => {
        setHome(parseFloat(event.target.value));
    }

    const changeTie = (event) => {
        setTie(parseFloat(event.target.value));
    }

    const changeAway = (event) => {
        setAway(parseFloat(event.target.value));
    }

    console.log(game);
    let date = game[3].replace("T", "          ");
    date = date.replace(":00.000Z", "");

    const sendOddAux = async (e) => {
        e.preventDefault();
        await sendOdd(game[0], home, tie, away);
        e.target.reset();
    }

    return (
        <GameWrapper id={game[0]} onSubmit={sendOddAux}>
            <GameInfo>
                <GameTitle>{game[1]} - {game[2]}</GameTitle>
                <Info><pre>{date}           {game[10]}</pre></Info>
            </GameInfo>
            <Odd>
                <OddTitle>{game[1]}</OddTitle>
                <OddInput onChange={changeHome} placeholder={game[7]}/>
                <Sugestion>{getSugestion(game[1])}</Sugestion>
            </Odd>
            <Odd>
                <OddTitle>Draw</OddTitle>
                <OddInput onChange={changeTie} placeholder={game[8]}/>
                <Sugestion>{getSugestion("Draw")}</Sugestion>
            </Odd>
            <Odd>
                <OddTitle>{game[2]}</OddTitle>
                <OddInput onChange={changeAway} placeholder={game[9]}/>
                <Sugestion>{getSugestion(game[2])}</Sugestion>
            </Odd>
            <Button form={game[0]} type="submit">OK</Button>
        </GameWrapper>
    )
}


const BKM = ({name, setBkm, bkm}) => {
    return (
        <BKMWrapper className={`${bkm === name ? "active" : "inactive"}`} onClick={() => {setBkm(name)}}>{name}</BKMWrapper>
    )
}


function EditOdds({updateState, state, api}) {

  const [games, setGames] = useState([]);
  const [bkm,   setBkm]   = useState("betclic");
  const [bkms,  setBkms]  = useState([]);

  const getData = async () => {
    const gg = await api.get("/api/get_wait_games/football");
    setGames(gg.data.data);
    let aux_bkms = [];
    if (gg.data.data.length > 0){
        for (let i = 0; i < gg.data.data[0][1].length; i++){
            if (!aux_bkms.includes(gg.data.data[0][1][i][3]))
            aux_bkms.push(gg.data.data[0][1][i][3]);
        }
    }
    setBkms(aux_bkms);
  }

  useEffect(() => {
    getData();
  }, []);

  const sendOdd = async (id, home, tie, away) => {
    const res = await api.post("/api/set_games_odds", {ids: [id], odds:[[home, away, tie]]})
    console.log(res.data.response); 
    getData();
  }

  return (
    <div style={{backgroundColor: "lightgray"}}>
        <NavBarAssembled state={state} api={api} current="editodds" updateState={updateState}/>
        <PageWrapper>
            <GameList>
                {
                    games.map(g => {
                        return <Game key={g[0][0]} sendOdd={sendOdd} game={g[0]} sugs={g[1]} bkm={bkm}/>
                    })
                }
            </GameList>
            <SideWrapper>
                <BkmTable>
                    {
                        bkms.map(b => {
                            return <BKM key={b} name={b} setBkm={setBkm} bkm={bkm}/>
                        })
                    }
                </BkmTable>
            </SideWrapper>
        </PageWrapper>
    </div>
  )
}

export default EditOdds