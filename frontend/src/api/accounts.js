import HTTP from '@/api/common'

const userResource = 'user'
const tokenResource = 'jwt'


export const Accounts = {
    login (data) {
        return HTTP.post(`${tokenResource}/create/`, data)
    }
}