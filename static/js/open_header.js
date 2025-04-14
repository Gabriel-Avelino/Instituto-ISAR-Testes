const openHeader = document.querySelector('.blue')
const header_resp = document.querySelector('.header_responsivo')

openHeader.addEventListener('click', ()=>{
    if (header_resp.classList.contains('background-color')){
        header_resp.classList.remove('background-color')
    } else{
        header_resp.classList.add('background-color')
    }  
})