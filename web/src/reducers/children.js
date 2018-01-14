const initialState = {
  all: [],
  currentUserChildren: [],
};

export default function (state = initialState, action) {
  switch (action.type) {
    // case 'FETCH_ROOMS_SUCCESS':
    //   return {
    //     ...state,
    //     all: action.response.data,
    //   };
    case 'FETCH_USER_CHILDREN_SUCCESS':
      return {
        ...state,
        currentUserChildren: action.response.data,
      };
    case 'CREATE_CHILD_SUCCESS':
      return {
        ...state,
        all: [
          action.response.data,
          ...state.all,
        ],
        currentUserChildren: [
          ...state.currentUserChildren,
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
