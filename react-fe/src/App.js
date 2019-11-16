import React from 'react';
import styled from 'styled-components';

import Map from './containers/Map';
import { List, RpiListItem } from './containers/List';

import mockRpis from './mockData/rpis';

const AppContainer = styled.div`
  background-color: yellow;
  width: 100vw;
  height: 100vh;  
  display: grid;
  grid-template-columns: auto 400px;
  grid-template-rows: auto;
  grid-template-areas: 
    "map list";
`;


const mockLocation = {latitude: 60.185323, longitude: 24.825576};
const pois = Object.keys(mockRpis).map((id, index) => ({
  ...mockRpis[id],
  id,
  latitude: mockLocation.latitude + (index / 1000),
  longitude: mockLocation.longitude + (index / 1000)
}));

function App() {
  const [state, setState] = React.useState({
    pointedOnList: undefined
  });

  return (
    <AppContainer>
      <Map pois={pois} higlightedPois={[state.pointedOnList]}/>
      <List>
        {pois.map(poi => (
          <RpiListItem
            key={poi.id}
            {...poi}
            onMouseEnter={() => setState({pointedOnList: poi.id})}
            onMouseLeave={() => setState({pointedOnList: undefined})}
          />))}
      </List>
    </AppContainer>
  );
}

export default App;
