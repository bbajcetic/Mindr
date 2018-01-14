const initialState = {
  isAuthenticated: false,
  willAuthenticate: true,
  currentUser: null,
};

export default function (state = initialState, action) {
  switch (action.type) {
    case 'AUTHENTICATION_REQUEST':
      return {
        ...state,
        willAuthenticate: true,
      };
    case 'AUTHENTICATION_SUCCESS':
      return {
        ...state,
        willAuthenticate: false,
        isAuthenticated: true,
        currentUser: action.response.user,
      };
    case 'AUTHENTICATION_FAILURE':
      return {
        ...state,
        willAuthenticate: false,
        currentUser: null,
      };
    case 'LOGOUT':
      return {
        ...state,
        willAuthenticate: false,
        isAuthenticated: false,
        currentUser: null,
      };
    default:
      return state;
  }
}
