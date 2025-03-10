const togglePassword = document.querySelector('#toggle-password');
        const passwordField = document.querySelector('#id_password');

        togglePassword.addEventListener('click', function (e) {
            // Alternar entre mostrar y ocultar la contraseña
            const type = passwordField.type === 'password' ? 'text' : 'password';
            passwordField.type = type;
            this.innerHTML = type === 'password' ? '<i class="fas fa-eye"></i>' : '<i class="fas fa-eye-slash"></i>';
        });