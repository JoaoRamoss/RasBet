import React from 'react'
import TransferHistory from '../components/Transfer'


function TransferPage({updateState, state, api}) {
  return (
    <TransferHistory state={state} api={api} updateState={updateState}/>
  )
}

export default TransferPage