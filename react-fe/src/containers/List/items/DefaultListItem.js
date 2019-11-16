import React from 'react';
import styled from 'styled-components';

const ListItemContainer = styled.div`
  background-color: silver;
  margin: 5px;
`;

export function DefaultListItem(props) {
  return (
    <ListItemContainer>{props.children}</ListItemContainer>
  );
}
