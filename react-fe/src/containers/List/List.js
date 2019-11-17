import React from 'react';
import styled from 'styled-components';

const ListContainer = styled.div`
/*  background-color: ${props => props.backgroundColor};
  grid-area: list;*/
  padding-top: 0.5rem;
`;

export function List(props) {
  return (
    <ListContainer palette={props.palette}>
      {props.children}
    </ListContainer>
  );
}
