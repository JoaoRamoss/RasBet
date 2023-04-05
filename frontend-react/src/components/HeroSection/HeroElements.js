import styled from 'styled-components'

export const HeroContainer = styled.div`
  background: #0c0c0c;
  display: flex;
  justify-content: center;
  align-items: center;
  padding: 0 30px;
  height: 100%;
  width: 100%;
  position: relative;
  z-index: 1;
`;

export const HeroBg = styled.div`
  position: fixed;
  top:0;
  width: 100%;
  height: 100vh;
  overflow: hidden;
`

export const VideoBg = styled.video`
  min-width: 100%;
  min-height: 100%;

  width: auto;
  height: auto;
  object-fit: cover;

  @media screen and (max-width: 1500px) {
    width: 30%;
  }
`;

export const RasBetLogo = styled.div`
  z-index: 3;
  background: linear-gradient(171deg, rgba(0,40,0,1) 0%, rgba(28,65,0,1) 53%, rgba(0,40,0,1) 100%);
  padding: 50px 100px;
  border-radius: 10px;
`
export const RasBetText = styled.div`
  color:black;
  font-size: 4rem;
  font-weight: bold;
  background: linear-gradient(90deg, rgba(152,131,0,1) 0%, rgba(226,194,0,1) 51%, rgba(152,131,0,1) 100%);
    -webkit-background-clip: text;
    background-clip: text;
    -webkit-text-fill-color: transparent;

  @media screen and (max-width: 500px){
    font-size: 2.5rem;
  }
`;

export const RasBetLogoOut = styled.div`
  z-index: 3;
  background: linear-gradient(90deg, rgba(152,131,0,1) 0%, rgba(226,194,0,1) 51%, rgba(152,131,0,1) 100%);
  padding: 10px 10px;
  border-radius: 10px;
`

export const MiddleWrapper = styled.div`
  z-index: 5;
  position: absolute;
  width: 60%;
  height: 50%;
  position: absolute;
  top: 50%;
  left: 50%;
  transform: translate(-50%, -50%);
  background-color: transparent;
  font-size: 4.5vw;
  font-weight: bold;
  color: white;
  display: flex;
  justify-content: center;
  align-items: center;
`