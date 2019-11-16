import React from 'react';
import styled from 'styled-components';
import {Marker} from 'react-map-gl';

const MarkerIcon = styled.div`
  border-radius: 50%;
  width: 10px;
  height: 10px;
  background-color: violet;
`;

const MarkerIconHighlighted = styled(MarkerIcon)`
  background-color: yellow;
`;

export function RpiMarker(props) {
  return (
    <Marker offsetLeft={-20} offsetTop={-10} {...props}>
      {props.higlighted ? <MarkerIconHighlighted/> : <MarkerIcon/>}
    </Marker>
  );

}
