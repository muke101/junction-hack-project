import React from 'react';
import styled from 'styled-components';

const MenuContainer = styled.div`
  background-color: ${props => props.backgroundColor};
  grid-area: menu;
`;

const MenuButton = styled.div`
  background-color: ${props => props.highlighted ? 'gold' : 'silver'};
  border-radius: 5px;
  margin: 10px;
  width: 150px;
  height: 40px;
  font-size: 25px;
  line-height: 40px;
  text-align: center;
  cursor: pointer;
  float: left;
`;

export default function Menu(props) {
  const {modes, selectedMode, onModeSelection} = props;
  return (
    <MenuContainer backgroundColor={modes[selectedMode].color}>
      {Object.keys(modes).map(modeKey => (
        <MenuButton
          key={modeKey}
          highlighted={selectedMode === modeKey}
          onClick={() => onModeSelection(modeKey)}
        >
          {modes[modeKey].title}
        </MenuButton>
      ))}
    </MenuContainer>
  );
}
