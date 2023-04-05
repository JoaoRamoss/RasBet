import React, {useState} from 'react'
import Navbar from './Navbar'
import Sidebar from './Sidebar'

const NavBarAssembled = ({updateState, state, api, current}) => {
  const [isOpen, setIsOpen] = useState(false);

  const toggle = () => {
    setIsOpen(!isOpen)
  }

  return (
    <div> 
      <Navbar toggle={toggle} state={state} api={api} current={current} updateState={updateState}/>
    </div>
  )
}

// <Sidebar isOpen = {isOpen} toggle={toggle} state={state}/>

export default NavBarAssembled;
