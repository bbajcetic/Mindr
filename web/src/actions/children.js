import api from '../api';

export function fetchChildren(userId) {
  return dispatch => api.fetch(`/users/${userId}/children/`)
    .then((response) => {
      dispatch({ type: 'FETCH_USER_CHILDREN_SUCCESS', response });
    });
}

export function createChild(data, userId, router) {
  return dispatch => api.post(`/users/${userId}/children/`, data)
    .then((response) => {
      dispatch({ type: 'CREATE_CHILD_SUCCESS', response });
      router.transitionTo(`/r/${response.data.id}`);
    });
}

// export function joinRoom(roomId, router) {
//   return dispatch => api.post(`/rooms/${roomId}/join`)
//     .then((response) => {
//       dispatch({ type: 'ROOM_JOINED', response });
//       router.transitionTo(`/r/${response.data.id}`);
//     });
// }
