import { randomString } from '@/assets/ts/module'

const baseURL = "http://localhost/api"
const loginURL = "https://discord.com/api/oauth2/authorize?client_id=937351409198829681&redirect_uri=http%3A%2F%2F127.0.0.1%3A8080%2Fdiscord_oauth&response_type=code&scope=identify%20email%20connections%20guilds%20guilds.members.read"
const accessToken = 'XQlYdTHW5G02ZG1N6rOR2Y50A8uYSs'

const myHeaders = new Headers({
    'Authorization': `Bearer ${accessToken}`,
    'Accept': 'application/json',
    'Content-Type': 'application/json',
})

const FormDataHeaders = new Headers({
    'Authorization': `Bearer ${accessToken}`,
    // 'Content-Type': 'multipart/form-data',
})

// GET
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

async function fetchGetNews(newsId: number) {
    const response = await fetch(`${baseURL}/news/${newsId}`);
    if (!response.ok) {return {}}
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

async function fetchGetNewsTags(newsId: number) {
    const response = await fetch(`${baseURL}/news/${newsId}/tags`);
    if (!response.ok) {return []}
    const result = await response.json()
    return result
}

async function fetchGetNewsComments(newsId: number) {
    const response = await fetch(`${baseURL}/news/${newsId}/comments`);
    if (!response.ok) {return []}
    const result = await response.json()
    return result
}

async function fetchGetSearch(searchContent: string, tags: number) {
    let api
    if(tags!=0){api = `${searchContent}?tag=${tags}`}
    else{api = searchContent}
    const response = await fetch(`${baseURL}/search/${api}`);
    if (!response.ok) {return []}
    const result = await response.json()
    return result
}

async function fetchGetStatistic(startDate: Date, endDate: Date, viewByDate: boolean, viewByTag: boolean, avgRateByYag: boolean, rateByTag: boolean){
    const response = await fetch(`${baseURL}/admin/statistic?start_date=${startDate}&end_date=${endDate}&view_by_date=${viewByDate}&view_by_tag=${viewByTag}&avg_rate_by_tag=${avgRateByYag}&rate_by_tag=${rateByTag}`,
    {   method: 'GET', 
        headers: myHeaders
    });
    if (!response.ok) {return []}
    const result = await response.json()
    return result
}

// POST
async function fetchPostComment(newsId: number, rating: number, content: string){
    const response = await fetch(`${baseURL}/news/comments`,
    {   method: 'POST', 
        headers: myHeaders,
        body: JSON.stringify({
            news: newsId, 
            rating: rating, 
            content: content
        })
    })
    if (!response.ok) {return []}
    const result = await response.json()
    return result
}

async function fetchCreateNews(data: any, thumbnailImage: any, bannerImage: any, ogImage: any, tags: Array<number>) {

    const body = new FormData()
    for (const key of Object.keys(data)) {body.set(key, data[key])}
    if(thumbnailImage.files[0]){body.set('thumbnail_img', thumbnailImage.files[0], `thumbnail-${randomString(10)}.png`)}
    if(ogImage.files[0]){body.set('og_img', ogImage.files[0], `og-${randomString(10)}.png`)}
    if(bannerImage.files[0]){body.set('banner_img', bannerImage.files[0], `banner-${randomString(10)}.png`)}
    for (const tag of tags){body.append('tags', String(tag))}

    const response = await fetch(`${baseURL}/admin/news/`,
    {   method: 'POST', 
        headers: FormDataHeaders,
        body: body
    })
    if (!response.ok) {return {}}
    const result = await response.json()
    return result
}

// PATCH
async function fetchUpdateNews(newsId: number, data: any, thumbnailImage: any, bannerImage: any, ogImage: any, tags: Array<number>) {

    const body = new FormData()
    for (const key of Object.keys(data)){body.set(key, data[key])}
    if(thumbnailImage.files[0]){body.set('thumbnail_img', thumbnailImage.files[0], `thumbnail-${randomString(10)}.png`)}
    if(ogImage.files[0]){body.set('og_img', ogImage.files[0], `og-${randomString(10)}.png`)}
    if(bannerImage.files[0]){body.set('banner_img', bannerImage.files[0], `banner-${randomString(10)}.png`)}
    for (const tag of tags){body.append('tags', String(tag))}


    const response = await fetch(`${baseURL}/admin/news/${newsId}`,
    {   method: 'PATCH', 
        headers: FormDataHeaders,
        body: body
    })
    if (!response.ok) {return {}}
    const result = await response.json()
    return result
}

// DELETE
async function fetchDeleteNews(newsId: number) {
    const response = await fetch(`${baseURL}/admin/news/${newsId}`,
    {   method: 'DELETE', 
        headers: myHeaders
    })
    if (!response.ok) {return {}}
    const result = await response.json()
    return result
}

export {
    // VAL
    baseURL, loginURL,
    // GET
    fetchGetUser,
    fetchGetNewsList, fetchGetSlideshow,fetchGetMostView,
    fetchGetTags,fetchGetNewsTags,
    fetchGetNews,fetchGetNewsComments,
    fetchGetSearch,
    fetchGetStatistic,
    // POST
    fetchPostComment, 
    fetchCreateNews,
    // PATCH
    fetchUpdateNews,
    // DELETE
    fetchDeleteNews,
}