// Função para decrementar valor
function decrementValue(inputId) {
    const input = document.getElementById(inputId);
    if (input.value > 0) {
        input.value--;
    }
}

// Função para incrementar valor
function incrementValue(inputId) {
    const input = document.getElementById(inputId);
    input.value++;
}