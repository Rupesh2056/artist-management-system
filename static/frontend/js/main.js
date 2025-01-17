// newsletter subscription
$('.general-form.subscribe__form').submit('.btn-enlist', function (e) {
    e.preventDefault();

    form_data = new FormData($('.general-form.subscribe__form')[0]);
    form_data.append('email', $('input[id=idNewsletter]').val());

    $.ajax({
        type: 'POST',
        url: '/newsletter/submit/',
        data: form_data,
        processData: false,
        contentType: false,
        cache: false,
        success: function (response) {
            if (response.success == true) {
                Toastify({
                    text: '"' + response.email + '"' + " subscribed to newsletter.",
                    duration: 3000,
                    style: {background: "green"},
                }).showToast();
                $("#idNewsletter").val("");
            }
            else {
                Toastify({
                    text: response.message.email,
                    duration: 3000,
                    style: {background: "red"},
                }).showToast();
                $("#idNewsletter").val("");
            }
        }
    })
});
// newsletter subscription end
