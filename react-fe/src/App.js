import React from 'react';
import styled from 'styled-components';

import Menu from './Menu';
import Map from './containers/Map';
import { List, RpiListItem } from './containers/List';

import mockRpis from './mockData/rpis';

const AppContainer = styled.div`
  background-color: yellow;
  width: 100vw;
  height: 100vh;  
  display: grid;
  grid-template-columns: auto 400px;
  grid-template-rows: 60px auto;
  grid-template-areas:
    "menu menu"
    "map list";
`;

const modes = {
  resident: {title: 'Resident', color: 'green', zoomLevel: 16},
  worker: {title: 'Worker', color: 'yellow', zoomLevel: 15},
  manager: {title: 'Manager', color: 'blue', zoomLevel: 13},
  official: {title: 'CityOfficial', color: 'violet', zoomLevel: 11},
};

const mockLocation = {latitude: 60.185323, longitude: 24.825576};
const pois = Object.keys(mockRpis).map((id, index) => ({
  ...mockRpis[id],
  id,
  latitude: mockLocation.latitude + (index / 1000),
  longitude: mockLocation.longitude + (index / 1000)
}));

export default function App() {
  const [state, setState] = React.useState({
    pointedOnList: undefined,
    selectedMode: Object.keys(modes)[0],
  });

  const onModeSelection = (selectedMode) => {
    setState({...state, selectedMode});
  };

  return (
    <AppContainer>
      <Menu modes={modes} selectedMode={state.selectedMode} onModeSelection={onModeSelection}/>
      <Map
        pois={pois}
        highlightedPois={[state.pointedOnList]}
        zoomLevel={modes[state.selectedMode].zoomLevel}
      />
      <List backgroundColor={modes[state.selectedMode].color}>
        {pois.map(poi => (
          <RpiListItem
            key={poi.id}
            {...poi}
            onMouseEnter={() => setState({...state, pointedOnList: poi.id})}
            onMouseLeave={() => setState({...state, pointedOnList: undefined})}
          />))}
      </List>
    </AppContainer>
  );
}
