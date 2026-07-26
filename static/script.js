document.querySelector("form").addEventListener("submit", function () {

    const button = document.querySelector("button");

    button.innerHTML =
    '<i class="fa-solid fa-spinner fa-spin"></i> Predicting...';

    button.disabled = true;

});