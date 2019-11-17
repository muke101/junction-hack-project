import React from 'react';
import styled from 'styled-components';

import { FontAwesomeIcon } from '@fortawesome/react-fontawesome';

const MenuContainer = styled.div`
  position: absolute;
  bottom: 0.5rem;
  display: flex;
  justify-content: space-around;
  width: 100%;
  z-index: 50;
`;

const Icon = styled.div`
  text-align: center;
  margin-bottom: 0.5rem;
`

const MenuButton = styled.div`
  display: flex;
  flex-direction: column;
  padding: 1rem;
  text-align: center;
  
  background-color: ${props => props.highlighted ? props.palette.light1 : 'rgba(255,255,255,0);'};
  color: ${props => props.highlighted ? props.palette.dark1 : '#333'}
  border-radius: 5px;
  font-size: 1rem;
  
  cursor: pointer;

  .fa {
    display: block;
    text-align: center;
    font-size: 2rem;
    margin.bottom: 0.5rem;
  }
`;

export default function BottomControls(props) {
  const {modes, mode, selectedMode, onModeSelection} = props;

  return (
    <MenuContainer>
      {Object.keys(modes).map(modeKey => (
        <MenuButton
          key={modeKey}
          highlighted={selectedMode === modeKey}
          palette={modes[modeKey].palette}
          onClick={() => onModeSelection(modeKey)}
        >
          <Icon><FontAwesomeIcon icon={modes[modeKey].icon} size='2x' /></Icon>
          {modes[modeKey].title}
        </MenuButton>
      ))}
    </MenuContainer>
  );
}