import HTTP from '@/api/common'

const restaurantsResource = 'restaurants'


export const Restaurants = {
    getAll(){
        return HTTP.get(restaurantsResource)
    }
}