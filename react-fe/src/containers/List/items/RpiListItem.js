import React from 'react';
import styled from 'styled-components';

const ListItemContainer = styled.div`
  background-color: silver;
  margin: 5px;
  &:hover {
    background-color: darkgray;
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
