import React from 'react';
import styled from 'styled-components';
import {Popup} from 'react-map-gl';

const PopupForm = styled.form`
  background-color: silver;
  border: 1px solid black;
`;
const CommentInput = styled.textarea`
`;
const SubmitButton = styled.button`
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
        <CommentInput name={'comment'} placeholder={'Your message'}/>
        <SubmitButton type={'submit'}>Submit</SubmitButton>
      </PopupForm>
    </Popup>
  )
}
