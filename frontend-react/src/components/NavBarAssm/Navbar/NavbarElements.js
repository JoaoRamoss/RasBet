import {Link as LinkR} from 'react-router-dom';
import styled from 'styled-components'
import {VscBell, VscBellDot} from 'react-icons/vsc';

export const Nav = styled.nav`
    background: linear-gradient(171deg, rgba(0,40,0,1) 0%, rgba(28,65,0,1) 53%, rgba(0,40,0,1) 100%);
    height: 10vh;
    min-height: 60px;
    display: flex;
    justify-content: center;
    align-items: center;
    font-size: 1.1rem;
    position: fixed;
    top: 0;
    width: 100%;
    z-index: 10;

    @media screen and (max-width: 960px) {
        transition: 0.8s all ease;
    }
    
`;

export const NavbarContainer = styled.div`
    box-shadow: 0px 0px 20px 0px rgba(0, 0, 0, 1);
    display: flex;
    justify-content: space-between;
    height: 100%;
    z-index: 1;
    width: 100%;
    padding: 0 24px;
`;

export const NavLogo = styled(LinkR)`
    background: linear-gradient(90deg, rgba(152,131,0,1) 0%, rgba(226,194,0,1) 51%, rgba(152,131,0,1) 100%);
    -webkit-background-clip: text;
    background-clip: text;
    -webkit-text-fill-color: transparent;
    justify-self: flex-start;
    cursor: pointer;
    font-size: 1.5rem;
    display:flex;
    align-items: center;
    margin-left: 24px;
    font-weight: bold;
    text-decoration: none;
`;

export const MobileIcon = styled.div`
    display:none;
`;

export const NavMenu = styled.ul`
    display: flex;
    align-items: center;
    list-style: none;
    width: 70%;
    height: 100%;
    margin-right: 20px;
    margin-left: 20px;
    justify-content: center;
    overflow: auto;

    ::-webkit-scrollbar {
        width: 0px;
    }
`;

export const NavItem = styled.li`
    height: 50%;
    border-radius: 50px;
    font-size: large;
    margin-right: 10px;
    margin-left: 10px;
    background-color: transparent;

    &.active{
        color: green;
        background-color: white;
    }
`;

export const NavLinks = styled(LinkR)`
    color: white;
    display: flex;
    align-items: center;
    text-decoration: none;
    padding: 0 1rem;
    height: 100%;
    cursor: pointer;
    transition: 0.2s ease-in-out;

    &.active{
        color: #153b00;
    }

    &:hover {
        color: rgba(152,131,0,1);
    }      
`;

export const NavBtn = styled.nav`
    display: flex;
    align-items: center;
    transition: 0.1s ease-in-out;

    &:hover{
        transition: 0.1s ease-in-out;
        scale: 1.1;
    }
`;

export const NavBtnLink = styled(LinkR)`
    border-radius: 50px;
    background: linear-gradient(90deg, rgba(152,131,0,1) 0%, rgba(226,194,0,1) 51%, rgba(152,131,0,1) 100%);
    white-space: nowrap;
    padding: 10px 22px;
    color: #010606;
    font-size: 16px; 
    outline: none;
    border: none;
    cursor: pointer;
    transition: all  0.5s ease-in-out;
    text-decoration: none;

`

export const UserName = styled(LinkR)`

    text-decoration: none;
    color: #fff;
    font-size: 1.3vw;
`;

export const UsernameWrapper = styled.button`
    border-radius: 50px;
    background-color: transparent;
    overflow: hidden;
    border: 2px solid #fff;
    padding: 7px 14px;
    cursor: pointer;
`

export const RightWrapper = styled.div`
    display: flex;
    align-items: center;
    justify-content: center;
    align-self: center;
    margin: 0;
    padding: 0;
    gap: 30px;
`

export const LoginRightSide = styled.div`
    display: flex;
    gap: 30px;
`