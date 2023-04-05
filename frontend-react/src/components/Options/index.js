import React, { useState, useEffect } from 'react'
import NavBarAssembled from '../NavBarAssm'
import { Button, Horizontal, Input, NotifyWrapper, OptionsWrapper, OptionTitle, PageWrapper, SendButton, TextBox } from './OptionsElements'



const Option = ({changeOption, opt}) => {

    const [value, setValue] = useState(opt[1]);
    let name = opt[0]//.toLowerCase();
    name = name.replace("_", " ");

    const setNewValue = (event) => {
        setValue(event.target.value);
    }

    const submitForm = async (e) => {
      e.preventDefault();
      if (value.length > 0){
        await changeOption(opt[0], value);
      }
      e.target.reset();
    }

    return (
        <Horizontal id={opt[0]} onSubmit={submitForm}>
            <OptionTitle>{name}</OptionTitle>
            <Input onChange={setNewValue} placeholder={opt[1]}/>
            <Button form={opt[0]} type="submit">OK</Button>
        </Horizontal>
    )
}


function Options({updateState, state, api}) {

  const [message, setMessage] = useState("");
  const [options, setOptions] = useState([]);

  const changeMessage = (event) => {
    setMessage(event.target.value);
  }

  const sendMessage = async () => {
    if (message.length > 0){
        const res = await api.post("/api/notify_all", {message: message});
        console.log(res.data.response);
    }
  }

  const submitMessageForm = async (e) => {
    e.preventDefault();
    if (message.length > 0){
      await sendMessage();
    }
    e.target.reset();
  }

  const getData = async () => {
    const res = await api.get("/api/options");
    setOptions(res.data.data);
    console.log(res.data.data);
  }

  useEffect(() => {
    getData();
  }, []);

  const changeOption = async (name, value) => {
    const res = await api.post("/api/options", {option: name, value: value});
    getData();
  }

  return (
    <div>
        <NavBarAssembled state={state} api={api} current="options" updateState={updateState}/>
        <PageWrapper>
            <OptionsWrapper>
                {
                    options.map(o => {
                        return <Option key={o[0]} changeOption={changeOption} opt={o}/>
                    })
                }
            </OptionsWrapper>
            <NotifyWrapper id="1" onSubmit={submitMessageForm}>
                <TextBox placeholder='Write a Message' onChange={changeMessage}/>
                <SendButton form="1" type="submit">Send</SendButton>
            </NotifyWrapper>
        </PageWrapper>
    </div>
  )
}

export default Options