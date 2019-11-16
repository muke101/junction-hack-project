import React from 'react';
import styled from 'styled-components';
import ReactMapGL, {FlyToInterpolator} from 'react-map-gl';

import {RpiMarker} from './markers';
import {HeatmapLayer} from './layers';
import { AddCommentPopup } from './popups';

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
      longitude : 24.825576,
      zoom: props.zoomLevel
    },
    selectedLayer: Object.keys(layers)[0],
    addCommentPopupLocation: undefined
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
        {...{...state.viewport}}
        mapStyle={'mapbox://styles/mapbox/streets-v9'}
        onViewportChange={viewport => onViewportChange(viewport)}
        onClick={(event) => setState({
          ...state,
          addCommentPopupLocation: {
            latitude : event.lngLat[1],
            longitude : event.lngLat[0],
          }
        })}
      >
        {state.selectedLayer === 'D' && <HeatmapLayer/>}
        {generateRpiMarkers(props.pois)}
        {state.addCommentPopupLocation &&
          <AddCommentPopup
            location={state.addCommentPopupLocation}
            onSubmit={(formData) => {
              window.alert(`User just commented "${formData.comment}" to (${state.addCommentPopupLocation.latitude}, ${state.addCommentPopupLocation.longitude}). what should we do?`);
              setState({...state, addCommentPopupLocation: undefined});
            }}
            onClose={() => setState({...state, addCommentPopupLocation: undefined})}
          />
        }
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
