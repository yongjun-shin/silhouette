const menuIcon = document.getElementById('menu-icon');
const checkBtn = document.getElementById('check-btn');

checkBtn.addEventListener('change', function() {
    if (this.checked) {
        menuIcon.src = "/static/imgs/close_closet.svg";
    } else {
        menuIcon.src = "/static/imgs/menu_closet.svg";
    }
});

const modal = document.getElementById('modal');
const addBtn = document.getElementById('add');
const closeBtn = modal.querySelector('.modal_close');

addBtn.addEventListener('click', ()=> {
    modal.style.display = 'block';
});
closeBtn.addEventListener("click", e => {
    modal.style.display = "none"
})