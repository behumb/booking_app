import { Restaurants } from '@/api/restaurants'
import { SET_RESTAURANTS_LIST } from '@/store/mutations_types'

const state = {
    restaurantsList: []
}

const getters = {

}

const mutations = {
    [SET_RESTAURANTS_LIST](state, data) {
        state.restaurantsList = data
    }
}

const actions = {
    getAll({commit}) {
        return Restaurants.getAll().then(response => {
            commit(SET_RESTAURANTS_LIST, response.data)
            return response
        })
    }
}

export default {
    namespaced: true,
    state,
    getters,
    mutations,
    actions
}