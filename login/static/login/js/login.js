

function togglePasswordVisibility() {
    var password = document.getElementById("id_password1");
    var confirmPassword = document.getElementById("id_password2");
    var mostrarContrasena = document.getElementById("mostrar_contrasena");

    if (mostrarContrasena.checked) {
        password.type = "text";
        confirmPassword.type = "text";
    } else {
        password.type = "password";
        confirmPassword.type = "password";
    }
}
