import { PropType } from 'vue';
interface News {

    id: number,
    view: number,
    rating: number,
    description: string,
    keywords: string,
    og_img: string,
    title: string,
    content: string,
    created_at: Date,
    created_by: number,
    updated_at: Date,
    updated_by: number,
    thumbnail_img: string,
    banner_img: string,
    is_slideshow: boolean

}

export default News