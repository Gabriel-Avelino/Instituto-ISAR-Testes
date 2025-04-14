const header = document.querySelector('header.off');

const debounce = (func, wait, immediate, timeout) => 
(...args) => {
        const later =  () => {
            if (!immediate) func(args);
        };
        const callNow = immediate && !timeout;
        clearTimeout(timeout);
        timeout = setTimeout(later, wait);
        if (callNow) func(args);
    };

function scrollposition (){
    if (window.scrollY > 40){
        header.classList.add('color')
    } else if (window.scrollY <= 40){
        header.classList.remove('color')
    }
}
scrollposition()

window.addEventListener('scroll', debounce(() => {
    scrollposition();
}, 0));

