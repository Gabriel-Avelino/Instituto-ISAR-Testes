function toggleDropdown(tipo, hasImage) {
    var content = document.getElementById('content-' + tipo);
    var dropdown = document.getElementById('dropdown-' + tipo);
    var img = hasImage ? document.getElementById('img-' + tipo) : null;
    if (content.style.display === 'none' || !content.style.display) {
        content.style.display = 'flex';
        setTimeout(function() {
            dropdown.classList.add('open')
            content.classList.add('open');
        }, 10); // Pequeno delay para garantir que display:block é aplicado antes da transição
        if (!img){
            dropdown.textContent = dropdown.textContent.replace('+', '-');
        }
    } else {
        content.classList.remove('open');
        dropdown.classList.remove('open')
        setTimeout(function() {
            content.style.display = 'none';
        }, 500); // Delay para coincidir com a duração da transição
        if (!img){
            dropdown.textContent = dropdown.textContent.replace('-', '+');
        }
    }
}

