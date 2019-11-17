import React from 'react';
import styled from 'styled-components';
import {Popup} from 'react-map-gl';
import defaultTheme from '../../../themes/defaultTheme';

const c = defaultTheme.colors.c1;

const PopupForm = styled.form`
  display: flex;
  flex-direction: column;
`;

const Title = styled.div`
  
  font-size: 1.25rem;
  padding: 0 0.4rem;
`;
const CommentInput = styled.textarea`
  font-size: 1rem;
  color: #333;
  margin-top: 0.5rem;
  margin-bottom: 0.5rem;
  min-width: 250px;
  border-radius: 5px;
  padding: 5px;
`;
const SubmitButton = styled.button`
  border-radius: 5px;
  background-color: ${c.light2};
  border: none;
  color: ${c.dark2};
  padding: 5px 0.5rem;
`;

export function AddCommentPopup(props) {
  const {location, onSubmit, onClose} = props;
  return (
    <Popup
      latitude={location.latitude}
      longitude={location.longitude}
      closeButton={true}
      closeOnClick={false}
      onClose={() => onClose()}
      anchor="top">
      <PopupForm onSubmit={(event) => {
        event.preventDefault();
        event.stopPropagation();
        onSubmit({comment: event.target.comment.value});
      }}>
        <Title>Report an issue?</Title>
        <CommentInput name={'comment'} placeholder={'Please describe the problem.'}/>
        <SubmitButton type={'submit'}>Submit</SubmitButton>
      </PopupForm>
    </Popup>
  )
}
