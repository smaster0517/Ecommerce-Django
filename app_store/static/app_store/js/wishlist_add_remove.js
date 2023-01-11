// Code Snippet from https://testdriven.io/blog/django-ajax-xhr/#post-request
function getCookie(name) {
    let cookieValue = null;
    if (document.cookie && document.cookie !== "") {
      const cookies = document.cookie.split(";");
      for (let i = 0; i < cookies.length; i++) {
        const cookie = cookies[i].trim();
        // Does this cookie string begin with the name we want?
        if (cookie.substring(0, name.length + 1) === (name + "=")) {
          cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
          break;
        }
      }
    }
    return cookieValue;
}

const updateWishlist = (e) => {
    const productID = e.target.id;
    // const buttonText = e.target.innerText;
    const productData = {productID:productID}
    fetch('/api_update_wishlist/', {
        method: 'POST',
        headers: {
            "X-Requested-With": "XMLHttpRequest",
            "X-CSRFToken": getCookie("csrftoken"),
        },
        credentials: 'same-origin', 
        body: JSON.stringify(productData)
    })
    .then(response => response.json())
    .then(data => {
        console.log('Success:', data);
        e.target.innerText = data.data
      })
    .catch(error => {
        console.error('Error:', error);
      });
}

let wishlistButton = document.querySelectorAll('.alter-wishlist');

wishlistButton.forEach(element => {
    element.addEventListener('click', updateWishlist);
});

const delete_product = (e) => {
    const productID = e.target.id;
    const productData = {productID:productID}
    fetch('/api_delete_product/', {
        method: 'POST',
        headers: {
            "X-Requested-With": "XMLHttpRequest",
            "X-CSRFToken": getCookie("csrftoken"),
        },
        credentials: 'same-origin', 
        body: JSON.stringify(productData)
    })
    .then(response => response.json())
    .then(data => {
        console.log('Success:', data);
        e.target.innerText = data.data
      })
    .catch(error => {
        console.error('Error:', error);
      });
}

let deleteButton = document.querySelectorAll('.delete-product');

deleteButton.forEach(element => {
    element.addEventListener('click', delete_product);
});