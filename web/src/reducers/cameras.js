const initialState = {
  all: [],
  currentUserCameras: [],
};

export default function (state = initialState, action) {
  switch (action.type) {
    // case 'FETCH_ROOMS_SUCCESS':
    //   return {
    //     ...state,
    //     all: action.response.data,
    //   };
    case 'FETCH_USER_CAMERAS_SUCCESS':
      return {
        ...state,
        currentUserCameras: action.response.data,
      };
    case 'CREATE_CAMERA_SUCCESS':
      return {
        ...state,
        all: [
          action.response.data,
          ...state.all,
        ],
        currentUserCameras: [
          ...state.currentUserCameras,
          action.response.data,
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
