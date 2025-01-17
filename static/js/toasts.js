;(function () {
  const toastOptions = { delay: 2000 }

  function createToast(message) {
    let bgColor = "info" 

    if (message.tags == "success")
    {
      bgColor = "green"

    }

    else if (message.tags == "error")
      {
        bgColor = "red"
  
      }


    Toastify({
      text: message.message,
      duration: 2000,
      //destination: "https://github.com/apvarun/toastify-js",
      //newWindow: true,
      close: true,
      gravity: "top", // `top` or `bottom`
      position: "center", // `left`, `center` or `right`
      stopOnFocus: true, // Prevents dismissing of toast on hover
      style: {
        background: bgColor,
      },
      onClick: function(){} // Callback after click
    }).showToast();
    
  }

  htmx.on("messages", (event) => {
    event.detail.value.forEach(createToast)
  })

  // Show all existsing toasts, except the template
  htmx.findAll(".toast:not([data-toast-template])").forEach((element) => {
    const toast = new bootstrap.Toast(element, toastOptions)
    toast.show()
  })
})()
