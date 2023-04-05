import './App.css';
import {BrowserRouter as Router, Routes, Route} from 'react-router-dom'
import Homepage from './pages';
import LoginPage from './pages/login';
import RegisterPage from './pages/register';
import FootballPage from './pages/football';
import BetHistoryPage from './pages/betHistory';
import axios from 'axios'
import { useState, useEffect } from 'react'
import TransferPage from './pages/transfer';
import EditGamesPage from './pages/editGames';
import EditOddsPage from './pages/editOdds';
import EditProfilePage from './pages/editProfile';
import OptionsPage from './pages/Options';


function App() {

  useEffect(() => {
    isLoggedIn();
  }, []);

  const [state, setState] = useState({
    loggedIn: false,
    userType: '',
    username: '',
  });

  const updateState = (loggedIn, userType, username) => {
    setState({
      loggedIn: loggedIn, 
      userType: userType, 
      username: username
    });
  }
  
  const api = axios.create({
    baseURL: "http://localhost:8080",
    withCredentials: true
  })

  const isLoggedIn = async () => {
    const post = await api.get("/api/login")
    if (post.data.response !== 'logged_out') {
      updateState(true, post.data.response, post.data.username); 
    }
    else {
      updateState(false, '', '');
    }
  }

  return (
    <Router>
      <Routes>
        <Route path="/" element={<Homepage state={state} api={api} type={state.userType} updateState={updateState}/>} exact></Route>
        <Route path="/login" element={<LoginPage updateState={updateState} api={api}/>} exact></Route>
        <Route path="/register" element={<RegisterPage api = {api} updateState={updateState} type={"user"}/>} exact></Route>
        <Route path="/register_admin" element={<RegisterPage api = {api} updateState={updateState} type={"admin"}/>} exact></Route>
        <Route path="/register_specialist" element={<RegisterPage api = {api} updateState={updateState} type={"specialist"}/>} exact></Route>
        <Route path="/football" element={<FootballPage state={state} api={api} updateState={updateState}/>} exact></Route>
        <Route path="/bethistory" element={<BetHistoryPage state={state} api={api} updateState={updateState}/>} exact></Route>
        <Route path="/transfer" element={<TransferPage state={state} api={api} updateState={updateState}/>} exact></Route>
        <Route path="/editprofile" element={<EditProfilePage setState={setState} state={state} api={api} updateState={updateState}/>} exact></Route>
        <Route path="/editodds" element={<EditOddsPage state={state} api={api} updateState={updateState}/>} exact></Route>
        <Route path="/editgames" element={<EditGamesPage state={state} api={api} updateState={updateState}/>} exact></Route>
        <Route path="/options" element={<OptionsPage state={state} api={api} updateState={updateState}/>} exact></Route>
        <Route path="*" element={<h1 style={{textAlign: 'center', marginTop: 50 + 'px'}}>404: NOT FOUND</h1>}/>
      </Routes>
    </Router>
  );
}

export default App;
