const initialState = {
  currentUserCameras: [],
};

export default function (state = initialState, action) {
  switch (action.type) {
    case 'FETCH_USER_CAMERAS_SUCCESS':
      return {
        ...state,
        currentUserCameras: action.response,
      };
    case 'CREATE_CAMERA_SUCCESS':
      return {
        ...state,
        currentUserCameras: [
          ...state.currentUserCameras,
          action.response,
        ],
      };
    // case 'ROOM_JOINED':
    //   return {
    //     ...state,
    //     currentUserChildren: [
    //       ...state.currentUserChildren,
    //       action.response.data,
    //     ],
    //   };
    default:
      return state;
  }
}
