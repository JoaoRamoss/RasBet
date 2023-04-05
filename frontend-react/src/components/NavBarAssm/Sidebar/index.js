import React from 'react'
import { SidebarContainer, Icon, CloseIcon, SideBtnWrap, SidebarLink, SidebarRoute, SidebarWrapper, SidebarMenu, UserName, UsernameWrapper} from './SidebarElements';





const SpecSideBar = () => {
  return (
    <SidebarMenu>
      <SidebarLink to='/editodds'>Edit Odds</SidebarLink>
    </SidebarMenu>
  )
}

const AdminSideBar = () => {
  return (
    <SidebarMenu>
      <SidebarLink to='/editgames'>Edit Games</SidebarLink>
      <SidebarLink to='/options'>  Options</SidebarLink>
    </SidebarMenu>
  )
}

const UserSideBar = ({state}) => {
  return (
    <SidebarMenu>
      <SidebarLink to='/football'>Football</SidebarLink>
      <SidebarLink to='/bethistory'>History</SidebarLink>
      <SidebarLink to='/transfer'>Transfers</SidebarLink>
      <SidebarLink to='/editprofile'>Profile</SidebarLink>
      {!state.loggedIn &&
      <SidebarLink to='/register'>Register</SidebarLink>
      }
    </SidebarMenu>
  )
}

const Sidebar = ({isOpen, toggle, state}) => {
  return (
    <SidebarContainer isOpen={isOpen} onClick={toggle}>
      <Icon onClick={toggle}>
        <CloseIcon />
      </Icon>
      <SidebarWrapper>
        
        {state.userType === "valid_user" &&
          <UserSideBar state={state}/>
        }
        {state.userType === "valid_admin" &&
          <AdminSideBar/>
        }
        {state.userType === "valid_specialist" &&
          <SpecSideBar/>
        }

        <SideBtnWrap>
          {!state.loggedIn ? 
          (<SidebarRoute to="/login">Login</SidebarRoute>) : 
          (<UsernameWrapper>
            <UserName to='/'>
              {state.username}
            </UserName>
          </UsernameWrapper>)
          }
        </SideBtnWrap>
      </SidebarWrapper>
    </SidebarContainer>
  )
}

export default Sidebar;


