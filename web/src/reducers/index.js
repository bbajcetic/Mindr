import { combineReducers } from 'redux';
import { reducer as form } from 'redux-form';
import session from './session';
import children from './children';

const appReducer = combineReducers({
  form,
  session,
  children,
});

export default function (state, action) {
  if (action.type === 'LOGOUT') {
    return appReducer(undefined, action);
  }
  return appReducer(state, action);
}
