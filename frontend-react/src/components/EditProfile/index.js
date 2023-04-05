import React, { useState, useEffect } from 'react'
import NavBarAssembled from '../NavBarAssm'
import { Button, Horizontal, Input, Label, PageWrapper, ProfileElement, ProfileLine, ProfileWrapper, Value } from './EditProfileElements'





function EditProfile({updateState, setState, state, api}) {

  const [username, setUsername] = useState("");
  const [email,    setEmail]    = useState("");
  const [password, setPassword] = useState("");
  const [auxUsername, setAuxUsername] = useState("");
  const [auxEmail, setAuxEmail] = useState("");

  const getData = async () => {
    const hist = await api.get("/api/get_user_data");
    setUsername(hist.data.data[1]);
    setEmail(hist.data.data[2]);
    //setPassword(hist.data.data[3]);
    setAuxUsername(hist.data.data[1]);
    setAuxEmail(hist.data.data[2]);
  }

  useEffect(() => {
    getData();
  }, []);

  const changeUsername = (event) => {
    setUsername(event.target.value);
  }

  const changeEmail = (event) => {
    setEmail(event.target.value);
  }

  const changePassword = (event) => {
    setPassword(event.target.value);
  }

  const handleFormSubmit = async e => {
    e.preventDefault();
    await sendProfile();
    e.target.reset();
  }

  const sendProfile = async () => {
    const res = await api.post("/api/edit_profile", {username: username, email: email, password: password})
    console.log(res.data);
    if (res.data.response === "valid"){
        setAuxUsername(username);
        setAuxEmail(email);
        setState({loggedIn: true, userType: "valid_user", username: username});
    }
  }

  return (
    <div>
        <NavBarAssembled state={state} api={api} current="editprofile" updateState={updateState}/>
        <PageWrapper>
            <ProfileWrapper>
                <form id="1" onSubmit={handleFormSubmit}>
                <Horizontal>
                    <ProfileElement>
                        <ProfileLine>
                            <Label>Username</Label>
                            <Value>{auxUsername}</Value>
                        </ProfileLine>
                        <ProfileLine>
                            <Label>New Username</Label>
                            <Input placeholder='Username' onChange={changeUsername}/>
                        </ProfileLine>
                    </ProfileElement>
                    <Button form="1" type="submit">OK</Button>
                </Horizontal>
                </form>
                <form id="2" onSubmit={handleFormSubmit}>
                <Horizontal>
                    <ProfileElement>
                        <ProfileLine>
                            <Label>Email</Label>
                            <Value>{auxEmail}</Value>
                        </ProfileLine>
                        <ProfileLine>
                            <Label>New Email</Label>
                            <Input placeholder='Email' onChange={changeEmail}/>
                        </ProfileLine>
                    </ProfileElement>
                    <Button form="2" type="submit">OK</Button>
                </Horizontal>
                </form>
                <form id="3" onSubmit={handleFormSubmit}>
                <Horizontal>
                    <ProfileElement>
                        <ProfileLine>
                            <Label>Password</Label>
                            <Value>***********</Value>
                        </ProfileLine>
                        <ProfileLine>
                            <Label>New Password</Label>
                            <Input placeholder='Password' type="password" onChange={changePassword}/>
                        </ProfileLine>
                    </ProfileElement>
                    <Button form="3" type="submit">OK</Button>
                </Horizontal>
                </form>
            </ProfileWrapper>
        </PageWrapper>
    </div>
  )
}

export default EditProfile