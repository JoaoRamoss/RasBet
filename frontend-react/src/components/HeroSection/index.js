import React from 'react'
import { HeroContainer, HeroBg, VideoBg, MiddleWrapper} from './HeroElements'
import Video from '../../videos/video.mp4'

const HeroSection = () => {
  return (
    <div>
    <HeroContainer id='home'>
      <HeroBg>
        <VideoBg autoPlay loop muted src={Video} 
        type="video/mp4"/>
      </HeroBg>
    </HeroContainer>
    <MiddleWrapper>Welcome!</MiddleWrapper>
    </div>
  )
}

export default HeroSection

    