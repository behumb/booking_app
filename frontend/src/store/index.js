import { createStore, createLogger } from 'vuex'
import accounts from "@/store/modules/accounts"
import restaurants from '@/store/modules/restaurants'

const debug = process.env.NODE_ENV !== 'production'

export default createStore({
  modules: {
    accounts,
    restaurants
  },
  strict: debug,
  plugins: debug ? [createLogger()] : []
})