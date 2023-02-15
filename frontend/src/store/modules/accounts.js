import {Accounts} from '@/api/accounts'
import {LOGIN_USER, LOGOUT_USER} from '@/store/mutations_types'


const state = {
    token: localStorage.getItem('token'),
    authUser: {}
}

const getters = {
    isAuthorized: state => !!state.token
}

const mutations = {
    [LOGIN_USER](state, data) {
        localStorage.setItem('token', data.access)
    },
    [LOGOUT_USER](state) {
        localStorage.removeItem('token')
    }
}

const actions = {
    login({commit}, data) {
        return Accounts.login(data).then(response => commit(LOGIN_USER, response.data))
    },
    logout({commit}) {
        commit(LOGOUT_USER)
    }

}

export default {
  namespaced: true,
  state,
  getters,
  actions,
  mutations
}