import React from 'react';
import styled from 'styled-components';
import ReactMapGL, {FlyToInterpolator} from 'react-map-gl';

import {RpiMarker} from './markers/RpiMarker';

const layers = {
  A: {icon: '☃'},
  B: {icon: '⏱'},
  C: {icon: '⌚'},
  D: {icon: '🍕'},
  E: {icon: '⏰'},
};

const MapContainer = styled.div`
  grid-area: map;
  position: relative;
`;

const LayerSelectionContainer = styled.div`
  position: absolute;
  right: 10px;
  top: 10px;
`;

const LayerSelection = styled.div`
  background-color: ${props => props.highlighted ? 'gold' : 'silver'};
  border-radius: 5px;
  margin: 10px;
  width: 40px;
  height: 40px;
  font-size: 25px;
  line-height: 40px;
  text-align: center;
  cursor: pointer;
`;

export function Map(props) {
  const [state, setState] = React.useState({
    viewport : {
      width : '100%',
      height : '100%',
      latitude : 60.185323,
      longitude : 24.825576
    },
    selectedLayer: Object.keys(layers)[0],
  });

  const generateRpiMarkers = (markers) => markers.map(marker => (
    <RpiMarker key={marker.id} {...marker} highlighted={props.highlightedPois.includes(marker.id)}/>
  ));


  const onViewportChange = (viewport) => {
    setState({...state, viewport})
  };

  const onSelectLayer = (selectedLayer) => {
    setState({...state, selectedLayer})
  };

  return (
    <MapContainer>
      <ReactMapGL
        {...{...state.viewport, zoom: props.zoomLevel}}
        mapStyle={'mapbox://styles/mapbox/streets-v9'}
        onViewportChange={viewport => onViewportChange(viewport)}
      >
        {generateRpiMarkers(props.pois)}
      </ReactMapGL>
      <LayerSelectionContainer>
        {Object.keys(layers).map(layerKey => (
          <LayerSelection
            key={layerKey}
            highlighted={state.selectedLayer === layerKey}
            onClick={() => onSelectLayer(layerKey)}
          >
            {layers[layerKey].icon}
          </LayerSelection>
        ))}
      </LayerSelectionContainer>
    </MapContainer>
  );
}
