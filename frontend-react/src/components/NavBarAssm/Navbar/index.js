import React, { useEffect, useState } from 'react';
import {FaBars} from 'react-icons/fa'
import {Nav, NavbarContainer, NavLogo, MobileIcon, NavMenu, NavItem, NavLinks, NavBtn, NavBtnLink, UserName,
   UsernameWrapper, RightWrapper, LoginRightSide} from './NavbarElements'
import Notifications from '../../Notifications';
import { Navigate, useNavigate } from 'react-router-dom';



const SpecNavBar = ({current}) => {
  return (
    <NavMenu>
      <NavItem className={`${current === "editodds" ? "active" : "inactive"}`}>
          <NavLinks className={`${current === "editodds" ? "active" : "inactive"}`} to='/editodds'>Edit Odds</NavLinks>
      </NavItem>
    </NavMenu>
  )
}

const AdminNavBar = ({current}) => {
  return (
    <NavMenu>
      <NavItem className={`${current === "editgames" ? "active" : "inactive"}`}>
          <NavLinks className={`${current === "editgames" ? "active" : "inactive"}`} to='/editgames'>Edit Games</NavLinks>
      </NavItem>
      <NavItem className={`${current === "options" ? "active" : "inactive"}`}>
          <NavLinks className={`${current === "options" ? "active" : "inactive"}`} to='/options'>  Options</NavLinks>
      </NavItem>
    </NavMenu>
  )
}

const UserNavBar = ({state, current}) => {
  return (
    <NavMenu>
      <NavItem className={`${current === "football" ? "active" : "inactive"}`}>
          <NavLinks className={`${current === "football" ? "active" : "inactive"}`} to='/football'>Football</NavLinks>
      </NavItem>
      {!state.loggedIn && 
      (<NavItem className={`${current === "register" ? "active" : "inactive"}`}>
          <NavLinks className={`${current === "register" ? "active" : "inactive"}`} to ='/register'>Register</NavLinks>
      </NavItem>)
      }
      <NavItem className={`${current === "bethistory" ? "active" : "inactive"}`}>
          <NavLinks className={`${current === "bethistory" ? "active" : "inactive"}`} to='/bethistory'>History</NavLinks>
      </NavItem>
      <NavItem className={`${current === "transfer" ? "active" : "inactive"}`}>
          <NavLinks className={`${current === "transfer" ? "active" : "inactive"}`} to='/transfer'>Wallet</NavLinks>
      </NavItem>
      <NavItem className={`${current === "editprofile" ? "active" : "inactive"}`}>
          <NavLinks className={`${current === "editprofile" ? "active" : "inactive"}`} to='/editprofile'>Profile</NavLinks>
      </NavItem>
    </NavMenu>
  )
}

const Navbar = ({toggle, updateState, state, api, current}) => {

  const [currentPage, setCurrentPage] = useState("");
  
  useEffect(() => {
    if (currentPage !== current) setCurrentPage(current);
  }, []);

  const navigate = useNavigate();
  
  const handleClick = async () => {
    const res = await api.post("/api/logout");
    console.log("logout");
    updateState(false, "", "");
    navigate("/login");
  }

  return(
      <div>
        <Nav>
          <NavbarContainer>
            <NavLogo to="/">
              RasBet
            </NavLogo>

            {(state.userType === "valid_user" || state.userType === "user") &&
              <UserNavBar current={currentPage} state={state}/>
            }
            {(state.userType === "valid_admin" || state.userType === "admin") &&
              <AdminNavBar current={currentPage}/>
            }
            {(state.userType === "valid_specialist" || state.userType === "specialist") &&
              <SpecNavBar current={currentPage}/>
            }
            
            <RightWrapper>
                {!state.loggedIn ? (<NavBtn><NavBtnLink to='/login'>Login</NavBtnLink></NavBtn>) :
                  (
                    <LoginRightSide>
                    <NavBtn>
                      <UsernameWrapper onClick={handleClick}>
                        <UserName>
                          {state.username}
                        </UserName>
                      </UsernameWrapper>
                    </NavBtn>
                    {(state.userType === "valid_user" || state.userType === "user") &&
                      <Notifications api={api}/>
                    }
                    </LoginRightSide>
                    )
                }
            </RightWrapper>
          </NavbarContainer>
        </Nav>
      </div>
  );
};

export default Navbar;