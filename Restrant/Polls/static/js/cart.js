const countInputs = document.getElementsByClassName('count__input');

Array.from(countInputs).forEach((input) => {
    input.addEventListener("change", (event) => {
        console.log(event);
        const itemId = +event.target?.getAttribute('data-item');
        const quantity = event.target?.value ? +event.target?.value : 1;

        window.location.href = `http://localhost:8080/cart/item/update-quantity/${itemId}/${quantity}`
    })
})