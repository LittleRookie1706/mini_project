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
                                    <p><strong>M??? ??n li???n l?? g???</strong></p>
                                    <p><strong>My ??n li???n (t??n g???i quen thu???c l?? m??? t??m, m??? cua, m??? g??i)</strong> l?? m??n m??? kh?? chi??n tr?????c v???i d???u c???, th?????ng ??n sau khi ????? n?????c s??i v??o v?? ?????i 3-5 ph??t. M??n m?? n??y c??n ???????c g???i m??? g??i hay m??? c???c ho???c m?? ly, t??y c??ch ?????ng m???.</p>
                                    <p>G??i m??? ??n li???n th?????ng c?? c??c g??i gia v??? nh??? t??ch r???i, th?????ng bao g???m b???t ng???t, nh??ng c??ng c?? lo???i kh??ng c?? b???t ng???t. C?? th??? ??n s???ng s???n ph???m n??y, t???i v?? m?? ???? ???????c chi??n tr?????c; th?????ng ph???i b??? m?? tr?????c khi ng??m n?????c. N???u d??ng n?????c ngu???i, c???n ph???i h??m n?? l??n 3 ph??t trong l?? vi s??ng.</p>
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

