import createPersistedState from 'vuex-persistedstate';
import {createStore} from 'vuex';

import admins from './modules/admins';

const store = createStore({
    modules: {
        admins
    },
    plugins: [createPersistedState()]
})

export default store;
// export default new Vuex.Store({
//   modules: {
//     notes,
//     admins,
//   },
//   plugins: [createPersistedState()]
// });