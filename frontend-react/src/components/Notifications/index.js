import React from 'react'
import { Wrapper, MenuTrigger, BellIcon, DropDownMenu, Header, UnordList, Item } from './NotificationsElements';
import { useEffect, useState } from 'react';

const DropDownItem = ({message}) => {
  return(
    <Item>{message}</Item>
  );
}

const Notifications = ({api}) => {

  const [open, setOpen] = useState(false);

  const [notifications, setNotifications] = useState([]);

  useEffect(() => {
    const getData = async () => {
      const res = await api.get("/api/get_notifications");
      setNotifications(res.data.data.reverse());
    }
    getData();
  }, []);

  return (
    <Wrapper>
      <MenuTrigger onClick={() => {setOpen(!open)}}>
        <BellIcon/>
      </MenuTrigger>
      <DropDownMenu className={`${open ? 'active' : 'inactive'}`}>
        <Header>Notifications</Header>
        <UnordList>
          {notifications.map(n => {return <DropDownItem key={n[0]} message={n[1]}/>})}
        </UnordList>
      </DropDownMenu>
    </Wrapper>
  )
}


export default Notifications;
