function open_mobile_menu() {
    document.getElementById("mobile-menu").classList.add("visible")
}
function close_mobile_menu() {
    document.getElementById("mobile-menu").classList.remove("visible")
}
function filter_in_stock_produce() {
    var is_checked = document.getElementById("show-only-in-stock").checked
    var offers_out_of_stock = document.querySelectorAll(".out-of-stock")
    for (var offer of offers_out_of_stock) {
        if (is_checked) {
            offer.classList.add("hidden")
        }
        else {
            offer.classList.remove("hidden")
        }
    }
}