
function toggleDropdown() {
    const dropdown = document.querySelector('.dropdown');
    dropdown.classList.toggle('active');
}

function storbyname(){
    const dropdown = document.querySelector('.dropdown');
    dropdown.classList.remove('active');

}

document.addEventListener('click', function (event) {
    const dropdown = document.querySelector('.dropdown');
    if (dropdown.classList.contains('active') && !dropdown.contains(event.target)) {
        dropdown.classList.remove('active');
    }
});