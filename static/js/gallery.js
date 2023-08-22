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


const itemModal = document.getElementById('items_modal');
const closeItemModal = itemModal.querySelector('.modal_close');
const div = document.getElementById('items');

document.addEventListener('DOMContentLoaded', function() {
    const items = document.querySelectorAll('#items');
    const title = itemModal.querySelector('.item_modal_title');
    const memo = itemModal.querySelector('.item_modal_memo');

    items.forEach(function(items) {
        items.addEventListener('click', function() {
            const itemTitle = this.dataset.itemTitle;
            const itemMemo = this.dataset.itemMemo;
            title.textContent = itemTitle;
            memo.textContent = itemMemo;
            itemModal.style.display = 'block';
        });
    });
});

div.addEventListener('click', () => {
    itemModal.style.display = 'block';
});

closeItemModal.addEventListener('click', () => {
    itemModal.style.display = 'none';
});