function specialMark(content: string){
    while(content.indexOf("**")!=-1){
        content = content.replace("**", "<strong>")
        content = content.replace("**", "</strong>")
    }
    while(content.indexOf("*")!=-1){
        content = content.replace("*", "<em>")
        content = content.replace("*", "</em>")
    }

    return content
}
function newsConverter(data: any){
    let result = ""

    for (let i = 0; i < data.length; i++) {
        switch(data[i].content_type) {
            case 'p':
                result += `<p>${data[i].content}</p>`
                break
            case 'h2':
                if(data[i].content.id){
                    result += `<h2 id="${data[i].content.id}">${data[i].content.content}</h2>`
                }
                else{
                    result += `<h2>${data[i].content.content}</h2>`
                }
                break
            case 'ul':
                result += '<ul>'
                for (let j = 0; j < data[i].content.length; j++) {
                    if(data[i].content[j].href){
                        
                        result += `<li><a href="${data[i].content[j].href}">${data[i].content[j].content}</a></li>`
                    }
                    else{
                        result += `<li>${data[i].content[j].content}</li>`
                    }
                    
                }
                result += '</ul>'
                break
            case 'img':
                result += `<p style="text-align: center;"><img alt="${data[i].content.alt}" class="lazy"  height="372" src="${data[i].content.src}" width="600"><br>${data[i].content.img_text}</p>`
                break
            case 'video':
                result += 
                    `<div class="responsive" style="position:relative;padding-top:56%">
                        <iframe allowfullscreen="" class="lazy" src="${data[i].content}" frameborder="0" height="315" style="position:absolute;width:100%;height:100%;top:0;left:0" title="YouTube video player" width="560">
                        </iframe>
                    </div>`
                break
            case 'table':
                result += 
                    `<table border="2" class="d-flex justify-center">
                        <tbody>
                            <tr class="d-flex justify-center align-center">
                                <td class="pa-5">
                                    <p><strong>Mỳ ăn liền là gì?</strong></p>
                                    <p><strong>My ăn liền (tên gọi quen thuộc là mỳ tôm, mỳ cua, mỳ gói)</strong> là món mỳ khô chiên trước với dầu cọ, thường ăn sau khi đổ nước sôi vào và đợi 3-5 phút. Món mì này còn được gọi mỳ gói hay mỳ cốc hoặc mì ly, tùy cách đựng mỳ.</p>
                                    <p>Gói mỳ ăn liền thường có các gói gia vị nhỏ tách rời, thường bao gồm bột ngọt, nhưng cũng có loại không có bột ngọt. Có thể ăn sống sản phẩm này, tại vì mì đã được chiên trước; thường phải bẻ mì trước khi ngâm nước. Nếu dùng nước nguội, cần phải hâm nó lên 3 phút trong lò vi sóng.</p>
                                </td>
                            </tr>
                        </tbody>
                    </table>`
                break
        }
    }

    result = specialMark(result)
    return result
}

export {
    newsConverter
}

