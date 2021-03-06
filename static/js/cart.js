$(document).ready(function(){
    var updateBtns = document.getElementsByClassName("update-cart")

    for (var i = 0; i < updateBtns.length; i++) {
        updateBtns[i].addEventListener("click", function() {
            var productId = this.dataset.product;
            var action = this.dataset.action;

            console.log("User", user);
            if(user == "AnonymousUser") {
                console.log("User is not authenticated");
            }
            else {
                updateUeserOrder(productId, action)
            }
        })
        
    }

    function updateUeserOrder(productId, action) {
        console.log('User is authenticated, sendimg data... ')

        var url = '/update_item/'

        fetch(url, {
            method: 'POST',
            headers: {
                'Content-Type':'application/json',
                "X-CSRFToken": csrftoken,
            },
            body: JSON.stringify({"productId": productId, "action": action})
        })
        .then((response) => {
            return response.json();
        })
        .then((data) => {
            console.log(data)
            location.reload()
        })
    }
})