const container2 = document.querySelector('.fotos-galery'); // Selecione o contêiner do carrossel
const controls2 = document.querySelectorAll(".foto-controls");
let currentItem2 = 0;
const items2 = document.querySelectorAll('.item2');

const maxItems2 = items2.length;

controls2.forEach(control=>{
    control.addEventListener('click', ()=> {
        const isLeft = control.classList.contains("controls-previous");
        
        if (isLeft) {
            currentItem2 -= 1;
        } else {
            currentItem2 += 1;
        }

        if (currentItem2 >= maxItems2) {
            currentItem2 = 0;
        } else if (currentItem2 < 0) {
            currentItem2 = maxItems2 - 1;
        }

        items2.forEach(item => item.classList.remove('current-item'));

        scrollToItem(currentItem2);

        items2[currentItem2].classList.add('current-item');
    })
})

function scrollToItem(index) {
    const item2 = items2[index];
    const containerRect = container2.getBoundingClientRect();
    const itemRect = item2.getBoundingClientRect();
    
    const offsetLeft = itemRect.left - containerRect.left + container2.scrollLeft - (containerRect.width / 2) + (itemRect.width / 2);
    
    container2.scrollTo({
        left: offsetLeft,
        behavior: 'smooth'
    });
}


function carrossel(){
    currentItem2++;

    if (currentItem2 >= maxItems2) {
        currentItem2 = 0;
    } else if (currentItem2 < 0) {
        currentItem2 = maxItems2 - 1;
    }

    items2.forEach(item => item.classList.remove('current-item'));

    scrollToItem(currentItem2);

    items2[currentItem2].classList.add('current-item');
}

