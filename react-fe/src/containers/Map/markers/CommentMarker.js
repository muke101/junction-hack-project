import React from 'react';
import styled from 'styled-components';
import {Marker} from 'react-map-gl';

const MarkerIcon = styled.div`
  border-radius: 50%;
  width: 10px;
  height: 10px;
  background-color: ${props => props.highlighted ? 'violet' : 'blue'};
`;

export function CommentMarker(props) {
  return (
    <Marker offsetLeft={-20} offsetTop={-10} {...props} id={props.index}>
      <MarkerIcon highlighted={props.highlighted}/>
    </Marker>

  );

}
