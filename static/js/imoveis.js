const cleanning = document.getElementById('cleanning');
const socioenvironmental = document.getElementById('socioenvironmental');
const infrastructure = document.getElementById('infrastructure');
const informations = document.getElementById('informations');

cleanning.addEventListener('click', ()=>{
    informations.innerHTML = ''
    const div = document.createElement('div')
    div.classList.add('info')
    div.id = 'info'
    const p = document.createElement('p')
    p.innerHTML = '<e class= "turquoise">Apartamentos:</e> Lorem ipsum dolor sit amet, consectetur adipiscing elit. Praesent interdum ac eros ac sagittis. Nullam vitae mauris non velit eleifend hendrerit sit amet eu metus. Sed blandit, justo nec facilisis bibendum, enim augue iaculis quam, sed laoreet ligula lorem sit amet lacus.'
    p.classList.add('left')
    div.innerHTML ='<img class="img-info" src="../src/img/caminhao-varredor.png">'
    div.append(p)
    informations.append(div)
    window.location.href = '#informations'
})

socioenvironmental.addEventListener('click', ()=>{
    informations.innerHTML = ''
    const div = document.createElement('div')
    div.classList.add('info')
    div.id = 'info'
    const p = document.createElement('p')
    p.innerHTML = '<e class= "turquoise">Casas:</e> Lorem ipsum dolor sit amet, consectetur adipiscing elit. Praesent interdum ac eros ac sagittis. Nullam vitae mauris non velit eleifend hendrerit sit amet eu metus. Sed blandit, justo nec facilisis bibendum, enim augue iaculis quam, sed laoreet ligula lorem sit amet lacus.'
    p.classList.add('left')
    div.innerHTML ='<img class="img-info" src="../src/img/consciencia.jpeg">'
    div.append(p)
    informations.append(div)
    window.location.href = '#informations'
})

infrastructure.addEventListener('click', ()=>{
    informations.innerHTML = ''
    const div = document.createElement('div')
    div.classList.add('info')
    div.id = 'info'
    const p = document.createElement('p')
    p.innerHTML = '<e class= "turquoise">Terrenos:</e> Lorem ipsum dolor sit amet, consectetur adipiscing elit. Praesent interdum ac eros ac sagittis. Nullam vitae mauris non velit eleifend hendrerit sit amet eu metus. Sed blandit, justo nec facilisis bibendum, enim augue iaculis quam, sed laoreet ligula lorem sit amet lacus.'
    p.classList.add('left')
    div.innerHTML ='<img class="img-info" src="../src/img/obra.jpeg">'
    div.append(p)
    informations.append(div)
    window.location.href = '#informations'
})