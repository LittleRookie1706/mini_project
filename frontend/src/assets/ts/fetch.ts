const baseURL = "http://localhost:8000"
const loginURL = "https://discord.com/api/oauth2/authorize?client_id=937351409198829681&redirect_uri=http%3A%2F%2F127.0.0.1%3A8080%2Fdiscord_oauth&response_type=code&scope=identify%20email%20connections%20guilds%20guilds.members.read"
const accessToken = 'm9yKRnFw4ZMPDxek15zykWCoFj77Ms'

const myHeaders = new Headers({
    'Authorization': `Bearer ${accessToken}`,
    'Content-Type': 'application/x-www-form-urlencoded'
})

async function fetchGetUser() {
    const response = await fetch(`${baseURL}/users/self/`,
    {   method: 'GET', 
        headers: myHeaders
    });
    if (!response.ok) {return {}}
    const user = await response.json()
    return user
}

async function fetchGetSlideshow(pageNumber: number) {
    const response = await fetch(`${baseURL}/news?page_number=${pageNumber}&is_slideshow=true`);
    if (!response.ok) {return []}
    const result = await response.json()
    return result
}

async function fetchGetNewsList(pageNumber: number) {
    const response = await fetch(`${baseURL}/news?page_number=${pageNumber}`);
    if (!response.ok) {return []}
    const result = await response.json()
    return result
}

async function fetchGetMostView() {
    const response = await fetch(`${baseURL}/news?order_by_view=true`);
    if (!response.ok) {return []}
    const result = await response.json()
    return result
}

async function fetchGetTags() {
    const response = await fetch(`${baseURL}/tags`);
    if (!response.ok) {return []}
    const result = await response.json()
    return result
}

async function fetchGetNewsComments(news_id: number) {
    const response = await fetch(`${baseURL}/news/${news_id}/comments`,);
    if (!response.ok) {return []}
    const user = await response.json()
    return user
}



export {
    loginURL, 
    fetchGetUser,
    fetchGetMostView,
    fetchGetNewsList,
    fetchGetSlideshow,
    fetchGetTags,
    fetchGetNewsComments
}