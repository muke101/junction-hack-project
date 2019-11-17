import React from "react";
import styled from 'styled-components';

import Map from './Map';
import { DaySlider, WeekSlider } from '../overlays/TimeSlider';
import { List, RpiListItem } from './List';

const OverlayLayer = styled.div`
  top: 0;
  left: 0;
  position: absolute;
  z-index: 100;
`

const MapLayer = styled(Map)`
  width: 100vw;
  height: 100vh;
  position: absolute;
  z-index: 10;
`

const LayerHolder = styled.div`
  position: absolute;
  z-index: 1;
  height: 100vh;
  width: 100vw;
    
  > * {
    position: absolute;
    z-index: 50;
  }
  ${MapLayer} {
    z-index: 1 !important;
  }
`

function MapView(props){
  const [state, setState] = React.useState({
    pointedOnList: undefined
  });

  return (
  <LayerHolder>
    <MapLayer
      pois={props.pois}
      highlightedPois={[state.pointedOnList]}
      zoomLevel={props.zoomLevel}
      style={{zIndex: 1}}
    />
    <List backgroundColor={props.palette.base}>
      {props.pois.map(poi => (
        <RpiListItem
          key={poi.id}
          {...poi}
          onMouseEnter={() => setState({...state, pointedOnList: poi.id})}
          onMouseLeave={() => setState({...state, pointedOnList: undefined})}
        />))}
    </List>
    {props.children}
  </LayerHolder>
  );
};

function ResidentMode(props) {
  return (
    <MapView {...props}>
      <DaySlider past={14} future={2} nowRounded={false} />
      {props.children}
    </MapView>
  );
};

function ManagerMode(props) {
  return (
    <MapView {...props}>
      <WeekSlider past={6} future={4} nowRounded={false} />
      {props.children}
    </MapView>
  );
};

function WorkerMode(props) {
  return (
    <MapView {...props}>
      <DaySlider past={6} future={7} nowRounded={false} />
      {props.children}
    </MapView>
  );
};

function CityMode(props) {
  return (
    <MapView {...props}>
      <DaySlider past={30} future={14} nowRounded={false} />
      {props.children}
    </MapView>
  );
};

export {
  ResidentMode,
  ManagerMode,
  WorkerMode,
  CityMode,
};