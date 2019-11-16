import React from 'react';
import styled from 'styled-components';

const ListContainer = styled.div`
  background-color: blue;
  grid-area: list;
`;

export function List(props) {
  return (
    <ListContainer>
      {props.children}
    </ListContainer>
  );
}
