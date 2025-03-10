document.getElementById("contactForm").addEventListener("submit", function(event) {
    let nombre = document.getElementById("nombre").value;
    let email = document.getElementById("email").value;
    let mensaje = document.getElementById("mensaje").value;

    if (nombre.length < 3) {
        alert("El nombre debe tener al menos 3 caracteres.");
        event.preventDefault();
    }

    let emailRegex = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
    if (!emailRegex.test(email)) {
        alert("Ingrese un correo electrónico válido.");
        event.preventDefault();
    }

    if (mensaje.length < 10) {
        alert("El mensaje debe tener al menos 10 caracteres.");
        event.preventDefault();
    }
});