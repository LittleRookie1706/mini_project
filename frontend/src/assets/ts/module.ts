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

function randomString(length: number) {
    let result           = '';
    const characters       = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789';
    const charactersLength = characters.length;
    for ( let i = 0; i < length; i++ ) {
        result += characters.charAt(Math.floor(Math.random() * charactersLength));
    }
    return result;
}



export {
    compareObject, 
    randomString
}