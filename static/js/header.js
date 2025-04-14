const header = document.querySelector('header');

const debounce = (func, wait, imediate, timeout) =>
(...args) => {
    const later = () => {
        if(!imediate) func(args);
    };

    const callNow = imediate && !timeout;
    clearTimeout(timeout);
    timeout = setTimeout(later, wait);
    if(callNow) func(args)
}

function scrollposition (){
    if(window.scrollY > 40){
        header.classList.add("color")
    } else{
        header.classList.remove("color")
    }
}

window.addEventListener('scroll', debounce(()=>{
    scrollposition()
}, 0))
