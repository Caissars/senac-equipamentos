function decrementValue() {
    if (document.getElementById("tool").value < 1) {
        return
    }
    document.getElementById("tool").value--;
}

function incrementValue(){
    document.getElementById("tool").value++;
}