import api from '../api';

export function fetchCameras(userId) {
  return dispatch => api.fetch(`/users/${userId}/cameras/`)
    .then((response) => {
      console.log(response);
      dispatch({ type: 'FETCH_USER_CAMERAS_SUCCESS', response });
    });
}

export function createCamera(data, userId, router) {
  return dispatch => api.post(`/users/${userId}/cameras/`, data)
    .then((response) => {
      dispatch({ type: 'CREATE_CAMERA_SUCCESS', response });
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
