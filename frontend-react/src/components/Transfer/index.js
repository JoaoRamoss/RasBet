import React from 'react'
import NavBarAssembled from '../NavBarAssm'
import { TransferHistoryHolder, Title, WalletAmount, Divider,
          Horizontal, TableTitle, TransferList, TableContent,
          TransferPopUp, AmountInput, Button, PageHolder, TransferSideBar, HorizontalLine } from './TransferElements';
import { useState, useEffect } from 'react';

const TransferRecord = ({date, description, amount}) => {
  date = date.substr(0, date.indexOf(" "));
  return (
    <HorizontalLine>
      <TableContent>{date}</TableContent>
      <TableContent>{description}</TableContent>
      <TableContent>{amount} €</TableContent>
    </HorizontalLine>
  )
}


function Transfer({updateState, state, api}) {

  const [history, setHistory] = useState([]);
  const [profile, setProfile] = useState([0,0,0,0]);
  const [depositAmount, setDepositAmount] = useState(0);
  const [withdrawAmount, setWithdrawAmount] = useState(0);

  const getData = async () => {
    const prof = await api.get("/api/get_user_data");
    setProfile(prof.data.data);
    const hist = await api.get("/api/transaction_history");
    setHistory(hist.data.data.reverse());
  }

  useEffect(() => {
    getData();
  }, []);


  const changeWithdrawAmount = (event) => {
    let value = parseFloat(event.target.value);
    setWithdrawAmount(value);
  }

  const changeDepositAmount = (event) => {
    let value = parseFloat(event.target.value);
    setDepositAmount(value);
  }

  const deposit = async (e) => {
    e.preventDefault();
    const res = await api.post("/api/deposit_money", {amount : depositAmount});
    console.log(res.data.response);
    e.target.reset();
    getData();
  }

  const withdraw = async (e) => {
    e.preventDefault();
    const res = await api.post("/api/withdraw_money", {amount : withdrawAmount});
    console.log(res.data.response);
    e.target.reset();
    getData();
  }

  return (
    <div>
        <NavBarAssembled state={state} api={api} current="transfer" updateState={updateState}/>
        <PageHolder>
          <TransferHistoryHolder>
            <Title>Transaction History</Title>
            <WalletAmount>Balance: {profile[4]}€</WalletAmount>
            <Divider/>
            <Horizontal>
              <TableTitle>Date</TableTitle>
              <TableTitle>Operation</TableTitle>
              <TableTitle>Amount</TableTitle>
            </Horizontal>
            <Divider/>
            <TransferList>
              {
                history.map(hist => {
                  return <TransferRecord key={hist[2]} date={hist[2]} description={hist[1]} amount={hist[0]}/>
                })
              }
            </TransferList>
          </TransferHistoryHolder>
          <TransferSideBar>
            <TransferPopUp id="1" onSubmit={withdraw}>
              
              <Title>Withdraw</Title>
              <AmountInput placeholder='0' onChange={changeWithdrawAmount}/>
              <Button form="1" type="submit">Withdraw</Button>
              
            </TransferPopUp>
            <TransferPopUp id="2" onSubmit={deposit}>
              
              <Title>Deposit</Title>
              <AmountInput placeholder='0' onChange={changeDepositAmount}/>
              <Button form="2" type="submit">Deposit</Button>
              
            </TransferPopUp>
          </TransferSideBar>
        </PageHolder>
    </div>
  )
}

export default Transfer