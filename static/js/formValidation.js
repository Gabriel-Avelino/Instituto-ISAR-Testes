const form = document.querySelector('.form');
const inputs = document.querySelectorAll('.input');
const result = document.querySelector('.result');
const message = document.querySelector('.result-text')
let password;
let email;
let check = []
let dependenteValue;
let gender;

document.addEventListener('DOMContentLoaded', function() {
    form.addEventListener('keydown', function(event) {
        if (event.key === 'Enter') {
            event.preventDefault();
        }
    });
});

if (message){
    document.addEventListener('DOMContentLoaded', (e) => {
        setTimeout(() => {
            if (message.parentElement){
                result.style.visibility = 'hidden'
                message.parentElement.innerHTML = ''
            }
        }, 5000);
    })
}

form.addEventListener('submit', (e) => {
    e.preventDefault();
    let valid = checkInputs();
    if (valid.every(value => value === true)) {
        const btnEnviar = document.querySelector('[data-button]');
        var textoDoBotao = btnEnviar.textContent
        btnEnviar.disabled = true; 
        btnEnviar.innerText = textoDoBotao.replace(/.$/, 'ndo...');
        setTimeout(() => {
            form.submit(); 
            form.reset(); 
        }, 5000);
    }
});

function checkInputs() {
    let validate = [];
    inputs.forEach(input => {
        const inputValue = input.value.trim()
        const classInput = input.classList.value.split(' ')
        
        if (inputValue === ''){
            errorValidation(input, 'Preencha esse campo');
            validate.push(false)
        } else{
            if(classInput.includes("email")){
                email = inputValue
            } 
            successValidation(input);
            validate.push(true)
        }
    });
    return validate
}


function errorValidation(input, message) {
    const formControl = input.parentElement;
    formControl.classList.add('error');
    formControl.classList.remove('success');
    shake(formControl);

    const messageError = formControl.querySelector('small');
    messageError.innerHTML = message;
};

function successValidation(input) {
    const formControl = input.parentElement;
    formControl.classList.add('success');
    formControl.classList.remove('error');
};

function shake(formControl) {
    formControl.classList.add('shake');
    formControl.addEventListener('animationend', () => {
        formControl.classList.remove('shake');
    });
};