import React from "react";
import Slider, { Range } from 'rc-slider';
import styled from 'styled-components';

import 'rc-slider/assets/index.css';

import moment from 'moment';

const SliderWrapper = styled.div`
  position: absolute;
  width: 90vw;
  margin-left: 5vw;
  margin-right: 5vw;
  bottom: 8rem;
  .rc-slider-handle {
    background-color: ${props => props.palette.light1};
    border-color: ${props => props.palette.base};
    border-width: 4px;
    width: 30px;
    height: 30px;
    margin-top: -13px;
  }
  .rc-slider-track {
    background-color:  ${props => props.palette.dark1};
  }
  .rc-slider-rail {
    background-color:  ${props => props.palette.light1};
  }
`;

const TimeSlider = (props) => {
  // Figure out slider parameters and conversion lookup for dates.
  // We map a range of start times to an array of integers, which are then used for the slider.
  // Props:
  //   past = n <units> backwards
  //   future = m <units> forwards
  //   nowSpecial = if true, now is exact and not rounded down to start of this time unit
  // Current <unit> is always included.
  const now = moment();
  const start = now.startOf(props.unit);
  const end = now.endOf(props.unit);
  const options = [];
  let startPos = 0;

  console.log('past', props.past);
  if(props.past) {
    startPos += props.past;
    for (let i = props.past; i > 0; --i) {
      options.push(start.subtract(i, props.unit));
    }
  }

  options.push(props.nowRounded ? start : now);

  console.log('future', props.future)
  if(props.future) {
    for (let i = 0; i < props.future; ++i) {
      options.push(end.add(i, props.unit));
    }
  }

  function onChange(value) {
    if(props.onChange) {
      return props.onChange(value, ); // Extra argument tells whether the selection represents "now"
    }
  }

  return (<SliderWrapper palette={props.palette}>
    <Slider className="test" min={0} max={options.length} defaultValue={startPos} onChange={props.onChange}
    />
  </SliderWrapper>);
};

export function DaySlider(props) {
  return (<TimeSlider {...props} unit={'day'} />);
};

export function WeekSlider(props) {
  return (<TimeSlider {...props} unit={'week'} />);
};

export function MonthSlider(props) {
  return (<TimeSlider {...props} unit={'month'} />);
};
