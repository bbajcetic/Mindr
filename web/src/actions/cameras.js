import api from '../api';

export function fetchCameras(userId) {
  return dispatch => api.fetch(`/users/${userId}/cameras/`)
    .then((response) => {
      dispatch({ type: 'FETCH_USER_CAMERAS_SUCCESS', response });
    });
}

export function createCamera(data, userId, router) {
  return dispatch => api.post(`/users/${userId}/cameras/`, data)
    .then((response) => {
      dispatch({ type: 'CREATE_CAMERA_SUCCESS', response });
      console.log(response.id);
      router.transitionTo(`/r/${response.data.id}`);
    });
}

// export function joinCamera(userId, cameraId, router) {
//   return dispatch => api.post(`/users/${userId}/camera/cameraId/`)
//     .then((response) => {
//       dispatch({ type: 'CAMERA_JOINED', response });
//       router.transitionTo(`/r/${response.data.id}`);
//     });
// }
