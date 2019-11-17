import React from 'react';
import styled from 'styled-components';

const ListItemContainer = styled.div`
  background-color: rgba(255,255,255,0.8);
  border: 2px solid rgba(255,255,255,0.9);
  border-left: 0;
  
  border-radius: 0 6px 6px 0;
  margin-top: 5px;
  margin-bottom: 0.5rem;
  
  &:hover {
    background-color: ${props => props.palette.light1};
    border-color: ${props => props.palette.base};
  }
  
  padding-top: 0.2rem;
  padding-bottom: 0.2rem;
  
  div {
    padding: 0.1rem 1rem;
    font-size: 0.8rem;
  }
`;

export function RpiListItem(props) {
  return (
    <ListItemContainer
      onMouseEnter={props.onMouseEnter}
      onMouseLeave={props.onMouseLeave}
      palette={props.palette}
    >
      <div>MAC: {props.id}</div>
      <div>Temp: {props.temperature}</div>
    </ListItemContainer>
  );
}
