import React from 'react';
import styled from 'styled-components';

const ListItemContainer = styled.div`
  background-color: violet;
  margin: 5px;
  &:hover {
  background-color: yellow;
  }
`;

export function RpiListItem(props) {
  return (
    <ListItemContainer
      onMouseEnter={props.onMouseEnter}
      onMouseLeave={props.onMouseLeave}
    >
      <p>MAC: {props.id}</p>
      <p>Temp: {props.temperature}</p>
    </ListItemContainer>
  );
}
