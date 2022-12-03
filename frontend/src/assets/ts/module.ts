interface AddObject {
    [key: string]: any
}

function compareObject(object1: any, object2: any){
    const result: AddObject = {};
    // console.log(object1, object2)
    for (const key of Object.keys(object1)) {
        if(object1[key]!=object2[key]){
            result[key] = object2[key]
        }
    }
    // console.log(result)
    return result
}


export {
    compareObject
}