import React from 'react';
import styled from 'styled-components';

const ListContainer = styled.div`
  background-color: ${props => props.backgroundColor};
  grid-area: list;
`;

export function List(props) {
  return (
    <ListContainer backgroundColor={props.backgroundColor}>
      {props.children}
    </ListContainer>
  );
}
