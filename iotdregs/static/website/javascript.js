function collectuserinfo() {
    let username = prompt("Enter username: ")
    let password = prompt("Enter password: ");
};

document.addEventListener("DOMContentLoaded", function() {
    document.getElementById("login").addEventListener('click', collectuserinfo)
});
