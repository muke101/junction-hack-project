import React from "react";
import styled from 'styled-components';

import Map from './Map';
import { DaySlider, WeekSlider } from '../overlays/TimeSlider';
import { List, RpiListItem } from './List';
import axios from "axios";

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
    
  > div {
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
      showComments={props.showComments}
      palette={props.palette}
      pois={props.pois}
      highlightedPois={[state.pointedOnList]}
      zoomLevel={props.zoomLevel}
      style={{zIndex: 1}}
    />
    <List palette={props.palette}>
      {props.pois.map(poi => (
        <RpiListItem
          key={poi.id}
          {...poi}
          palette={props.palette}
          onMouseEnter={() => setState({...state, pointedOnList: poi.id})}
          onMouseLeave={() => setState({...state, pointedOnList: undefined})}
        />))}
    </List>
    {props.children}
  </LayerHolder>
  );
};

const TimeWrapper = styled.div`
  width: 100vw;
  position: absolute;
  bottom: 10rem;
  left: 0;
  justify-content: center;
`

const TimeInfo = styled.div`
  padding-top: 0.5rem;
  padding-bottom: 0.5rem;
  border-radius: 1rem;
  background: rgba(255,255,255,0.7);
  z-index: 100;
  min-width: 300px;
  max-width: 80vw;
  text-align: center;
  margin-left: 10vw;
  width: 80vw;
`

const Title = styled.div`
  font-size: 1.2rem;
`
const SubTitle = styled.div`
  font-size: 0.8rem;
  color: #888;
`


/*
axios.get('/api/v1/backend/reports').then((res) => {

});
*/

function ResidentMode(props) {
  const [state, setState] = React.useState({
    title: "Current time",
    subTitle: 'Daily information',
    moment: undefined,
  });

  function onChange(starting, isNow) {
    console.log(starting);
    setState({...state,
      title: isNow || !starting ? 'Current time' : starting.format('LLL'),
      moment: isNow ? undefined : starting,
    });
  }

  return (
    <MapView {...props}>
      <TimeWrapper><TimeInfo><Title>{state.title}</Title><SubTitle>{state.subTitle}</SubTitle></TimeInfo></TimeWrapper>
      <DaySlider past={14} future={2} nowRounded={false} palette={props.palette} onChange={onChange} />
      {props.children}
    </MapView>
  );
};

function ManagerMode(props) {
  const [state, setState] = React.useState({
    title: "Current time",
    subTitle: 'Weekly information',
    moment: undefined,
  });

  function onChange(starting, isNow) {
    console.log(starting);
    setState({...state,
      title: isNow || !starting ? 'Current time' : starting.format('LLL'),
      moment: isNow ? undefined : starting,
    });
  }

  return (
    <MapView {...props} showComments={true}>
      <TimeWrapper><TimeInfo><Title>{state.title}</Title><SubTitle>{state.subTitle}</SubTitle></TimeInfo></TimeWrapper>
      <WeekSlider past={6} future={4} nowRounded={false} palette={props.palette} onChange={onChange} />
      {props.children}
    </MapView>
  );
};

function WorkerMode(props) {
  const [state, setState] = React.useState({
    title: "Current time",
    subTitle: 'Daily information',
    moment: undefined,
  });

  function onChange(starting, isNow) {
    console.log(starting);
    setState({...state,
      title: isNow || !starting ? 'Current time' : starting.format('LLL'),
      moment: isNow ? undefined : starting,
    });
  }

  return (
    <MapView {...props}>
      <TimeWrapper><TimeInfo><Title>{state.title}</Title><SubTitle>{state.subTitle}</SubTitle></TimeInfo></TimeWrapper>
      <DaySlider past={6} future={7} nowRounded={false} palette={props.palette} onChange={onChange} />
      {props.children}
    </MapView>
  );
};

function CityMode(props) {
  const [state, setState] = React.useState({
    title: "Current time",
    subTitle: 'Daily information',
    moment: undefined,
  });

  function onChange(starting, isNow) {
    console.log(starting);
    setState({...state,
      title: isNow || !starting ? 'Current time' : starting.format('LLL'),
      moment: isNow ? undefined : starting,
    });
  }

  return (
    <MapView {...props}>
      <TimeWrapper><TimeInfo><Title>{state.title}</Title><SubTitle>{state.subTitle}</SubTitle></TimeInfo></TimeWrapper>
      <DaySlider past={30} future={14} nowRounded={false} palette={props.palette} onChange={onChange} />
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
