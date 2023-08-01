const menuIcon = document.getElementById('menu-icon');
const checkBtn = document.getElementById('check-btn');

checkBtn.addEventListener('change', function() {
    if (this.checked) {
        menuIcon.src = "/static/imgs/close_closet.svg";
    } else {
        menuIcon.src = "/static/imgs/menu_closet.svg";
    }
});

const addBtn = document.getElementById('add');
