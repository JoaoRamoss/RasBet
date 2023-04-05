import { VscBell } from 'react-icons/vsc'
import styled, {keyframes} from 'styled-components'
import { fadeInRight } from 'react-animations'

export const Wrapper = styled.div`
    display: flex;
`

export const BellIcon = styled(VscBell)`
    position: relative;
    color: #fff;
    scale: 1.5;
    margin-top: 0.7rem;
`

export const MenuTrigger = styled.div`
    cursor: pointer;
`

export const Header = styled.h3`
    width: 100%;
    text-align: center;
    font-size: 18px;
    padding: 10px 0;

`

const dropDown = keyframes`${fadeInRight}`;
export const DropDownMenu = styled.div`
    position: absolute;
    top: 90px;
    right: 30px;
    background-color: #fafafa;
    box-shadow: 0px 0px 25px 0px rgba(0, 0, 0, 0.3);
    border-radius: 15px;
    padding: 10px 20px;
    padding-bottom: 20px;
    width: 20vw;
    margin-right: 10px;
    animation: 0.5s ${dropDown};

    &.active{
        opacity: 1;
        visibility: visible;
        transform: translateY(0);
        transition: 0.5s ease;
    }

    &.inactive{
        opacity: 0;
        visibility: hidden;
        transform: translateY(-10px);
        transition: 0.5s ease;
    }

`

export const UnordList = styled.ul`
    padding: 10px 0;
    border-top: 1px solid rgba(0, 0, 0, 0.15);
    list-style-type: none;
    max-height: 40vh;
    overflow: auto;

    ::-webkit-scrollbar {
        width: 10px;
        background: lightgray;
        border-radius: 10px;
    }
    ::-webkit-scrollbar-thumb {
        border-radius: 10px;
        background-color:  darkgray; 
    }
`

export const Item = styled.div`
    width: 90%;
    margin-left: auto;
    margin-right: auto;
    border-bottom: 1px solid rgba(0, 0, 0, 0.15);
    display: flex;
    align-items: center;
    font-size: 1rem;
    padding-bottom: 10px;
    padding-top: 7px;
`