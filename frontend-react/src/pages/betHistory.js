import React from 'react'
import BetHistory from '../components/BetHistory';

const BetHistoryPage = ({updateState, state, api}) => {
  return (
    <div>
        <BetHistory state={state} api={api} updateState={updateState}/>
    </div>
  )
}

export default BetHistoryPage;
