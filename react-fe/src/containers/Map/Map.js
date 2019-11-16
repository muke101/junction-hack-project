import React from 'react';
import styled from 'styled-components';
import ReactMapGL from 'react-map-gl';

import {RpiMarker} from './markers/RpiMarker';

const MapContainer = styled.div`
  background-color: red;
  grid-area: map;
`;

export function Map(props) {
  const [state, setState] = React.useState({
    viewport : {
      width : '100%',
      height : '100%',
      latitude : 60.185323,
      longitude : 24.825576,
      zoom : 14
    },
  });

  const generateRpiMarkers = (markers) => markers.map(marker => (
    <RpiMarker key={marker.id} {...marker} higlighted={props.higlightedPois.includes(marker.id)}/>
  ));

  return (
    <MapContainer>
      <ReactMapGL
        {...state.viewport}
        mapStyle={'mapbox://styles/mapbox/streets-v9'}
        onViewportChange={(viewport) => setState({ viewport })}
      >
        {generateRpiMarkers(props.pois)}
      </ReactMapGL>
    </MapContainer>
  );
}
