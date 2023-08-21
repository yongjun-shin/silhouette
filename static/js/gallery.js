const menuIcon = document.getElementById('menu-icon');
const checkBtn = document.getElementById('check-btn');

checkBtn.addEventListener('change', function() {
    if (this.checked) {
        menuIcon.src = "/static/imgs/close.svg";
    } else {
        menuIcon.src = "/static/imgs/menu.svg";
    }
});

const modal = document.getElementById('modal');
const addDiv = document.getElementById('add');
const closeBtn = modal.querySelector('.modal_close');

addDiv.addEventListener('click', ()=> {
    modal.style.display = 'block';
});
closeBtn.addEventListener("click", e => {
    modal.style.display = "none"
});
