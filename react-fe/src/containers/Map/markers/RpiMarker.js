import React from 'react';
import styled from 'styled-components';
import {Marker} from 'react-map-gl';

const MarkerIcon = styled.div`
  border-radius: 50%;
  width: 10px;
  height: 10px;
  background-color: ${props => props.highlighted ? 'violet' : 'yellow'};
`;

export function RpiMarker(props) {
  return (
    <Marker offsetLeft={-20} offsetTop={-10} {...props}>
      <MarkerIcon highlighted={props.highlighted}/>
    </Marker>

  );

}
