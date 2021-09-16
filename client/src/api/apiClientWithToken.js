import { create } from 'apisauce';

const apiClientWithToken = (token) => create({
    baseURL: window.location.hostname === "localhost" || window.location.hostname === '127.0.0.1'? 'http://127.0.0.1:5000' : '',
    headers:{
        Authorization: `Bearer ${token}`,
        'Content-Type':'application/json'
    }
})

// post liked pet
const endpointLiked = 'api/liked';
export const liked = async (token, data) =>{
    const response = await apiClientWithToken(token).post(endpointPosts,data);
    if ( response.ok ){ return true }
    else { return false }
}
