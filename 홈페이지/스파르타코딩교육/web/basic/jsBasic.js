/* hello */
console.log("hello")

/* variable */
let num=2
let name="chang"

num+name
// 2chang

/* variable name rule */
let nameCamel='2' // camel
let name_snake='1'  // snake

/* list */
let a=[1,2,3,4]
a.push('hi') // python equal
a.length // python : len 

/* dict */
let a={1:'hw',2:'ow',3:'44'}
a[1] // 'hw'
a[4]='ww'

/* str */
let a='123-456'
let b=a.split('-') // ['123','456']
let c=b.join('_') // '123_456'

/* func */
function mul(a,b){
    return a*b;
}

// mul(2,4)=8

function alert(a){
    if (a>3) {
        alert('high')
    } else if (a>1) {
        alert('low')
    } else {
        alert('no way')
    }
}

// alert(3) = 'no way'

/* for-loop */
for (let i=0;i<5;i++){
    console.log('hi');
}