import React from 'react';
import styled from 'styled-components';

import BottomControls from './overlays/BottomControls';
import { ResidentMode, WorkerMode, ManagerMode, CityMode } from './containers/modes';

import mockRpis from './mockData/rpis';

import { ThemeProvider } from 'styled-components';
import defaultTheme from './themes/defaultTheme';

import { fa, faUserNinja, faHardHat, faUserSecret, faCity } from '@fortawesome/free-solid-svg-icons';

const AppContainer = styled.div`
  position: absolute;
  width: 100vw;
  height: 100vh;  
`;

const modes = {
  resident: {
    title: 'Resident',
    Interface: ResidentMode,
    palette: defaultTheme.colors.c1,
    zoomLevel: 16,
    icon: faUserNinja,
  },
  worker: {
    title: 'Worker',
    Interface: WorkerMode,
    palette: defaultTheme.colors.c3,
    zoomLevel: 15,
    icon: faHardHat,
  },
  manager: {
    title: 'Manager',
    Interface: ManagerMode,
    palette: defaultTheme.colors.c2,
    zoomLevel: 13,
    icon: faUserSecret,
  },
  city: {
    title: 'City Official',
    Interface: CityMode,
    palette: defaultTheme.colors.c4,
    zoomLevel: 11,
    icon: faCity,
  }
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
    selectedMode: Object.keys(modes)[0],
    mode: Object.values(modes)[0]
  });

  const onModeSelection = (selectedMode) => {
    setState({...state, selectedMode, mode: modes[selectedMode]});
  };

  const Interface = state.mode.Interface;

  return (
    <ThemeProvider theme={defaultTheme}>
      <AppContainer>
        <Interface pois={pois} {...state.mode}>
          <BottomControls modes={modes} {...state} onModeSelection={onModeSelection} />
        </Interface>
      </AppContainer>
    </ThemeProvider>
  );
}
