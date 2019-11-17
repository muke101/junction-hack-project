import React from 'react';
import styled from 'styled-components';
import ReactMapGL from 'react-map-gl';
import axios from 'axios';

import {RpiMarker} from './markers';
import {HeatmapLayer} from './layers';
import { AddCommentPopup } from './popups';

const layers = {
  bluetooth: {icon: '☃', url: '/api/v1/backend/bluetooth'},
  B: {icon: '⏱'},
  C: {icon: '⌚'},
  D: {icon: '🍕'},
  E: {icon: '⏰'},
};

const MapContainer = styled.div`
  grid-area: map;
  position: absolute;
  width: 100vw;
  height: 100vh;
  
  .mapboxgl-popup-content {
    background-color: rgba(255,255,255,0.6);
  }
  .mapboxgl-popup-tip {
    border-bottom-color: rgba(255,255,255,0.6);
  }
`;

const LayerSelectionContainer = styled.div`
  position: absolute;
  right: 10px;
  bottom: 15rem;
`;

const LayerSelection = styled.div`
  background-color: ${props => props.highlighted ? props.palette.light1 : 'rgba(255,255,255,0.7)'};
  color: ${props => props.highlighted ? '#000' : '#555'};
  border-radius: 100%;
  border-width: 3px;
  border-color: ${props => props.highlighted ? props.palette.dark1 : 'rgba(255,255,255,0.7)'};
  border-style: solid;
  margin: 10px;
  margin-bottom: 20px;
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
    addCommentPopupLocation: undefined,
    data: {}
  });
  if (!state.data.bluetooth) {
    axios.get(layers.bluetooth.url)
      .then(function (response) {
        setState({...state, data: {...state.data, bluetooth: response.data}});
      })
  }

  const generateRpiMarkers = (markers) => markers.map(marker => (
    <RpiMarker key={marker.id} {...marker} highlighted={props.highlightedPois.includes(marker.id)}/>
  ));


  const onViewportChange = (viewport) => {
    setState({...state, viewport})
  };

  const onSelectLayer = (selectedLayer) => {
    setState({...state, selectedLayer})
  };

  console.log(state.data.bluetooth);
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
        {state.selectedLayer === 'bluetooth' && state.data.bluetooth && <HeatmapLayer data={state.data.bluetooth}/>}
        {generateRpiMarkers(props.pois)}
        {state.addCommentPopupLocation &&
          <AddCommentPopup
            location={state.addCommentPopupLocation}
            onSubmit={(formData) => {
              axios.post('/api/v1/backend/reports', {
                user: '57c7f752a8f44af9b7cd3b111cb1837f',
                comment: formData.comment,
                priority: 3, // 0 through 5
                latitude: state.addCommentPopupLocation.latitude,
                longitude: state.addCommentPopupLocation.longitude,
              }).then((res) => {
                setState({...state, addCommentPopupLocation: undefined});
              }).catch((err) => {
                alert('Oh no! Something went boom... :(\n' + err);
              })
            }}
            onClose={() => setState({...state, addCommentPopupLocation: undefined})}
          />
        }
      </ReactMapGL>
      <LayerSelectionContainer>
        {Object.keys(layers).map(layerKey => (
          <LayerSelection
            palette={props.palette}
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
