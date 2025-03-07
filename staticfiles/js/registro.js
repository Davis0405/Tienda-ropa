function togglePassword(inputId, iconId) {
    var inputField = document.getElementById(inputId);
    var icon = document.getElementById(iconId);

    // Cambiar el tipo de campo de contraseña
    if (inputField.type === "password") {
        inputField.type = "text";
        icon.classList.remove('fa-eye');
        icon.classList.add('fa-eye-slash');
    } else {
        inputField.type = "password";
        icon.classList.remove('fa-eye-slash');
        icon.classList.add('fa-eye');
    }
}