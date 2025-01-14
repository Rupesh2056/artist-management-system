// Prevent users from submitting by hitting Enter
$(document).on("keydown", "form", function(event) {
    return event.key != "Enter";
});


// shipping address radio buttons (in addresses list)
$(document).on("click", ".radio-opt.shipping", function() {
    if ($(this).attr("class") == "radio-opt shipping") {
        $(this).attr("class", "radio-opt shipping optactive");
    }
    // unselect others
    $(".radio-opt.shipping").not($(this)).each(function() {
        $(this).attr("class", "radio-opt shipping");
    });
});
// shipping address radio buttons (in addresses list) end


// things to do after selecting address from shipping address list
$(document).on("click", ".shipping-address-save", function() {
    $("#shipping_address").attr("value", $(".radio-opt.shipping.optactive").attr("value"));
    $(".jsxInline").magnificPopup("close");

    $.ajax({
        url: "/get-address/",
        type: "GET",
        data: {
            "id": $(".radio-opt.shipping.optactive").attr("value")
        },
        success: function(response) {
            $("#billing_address").attr("value", response.data.id); // update input value of billine-address
            $(".billing-address.shipping").attr("value", response.data.id); // update "same as shipping" billing address id
            $(".shipping-address.optactive").attr("value", response.data.id);

            html = response.data.receiver_name + " " + response.data.receiver_contact_number +
            "<address>" + response.data.address + ", " + response.data.city +
            "</address><a href='#chkShippingEdit' class='optedit jsxInline' data-effect='mfp-zoom-in'>Edit</a>"
            $(".shipping-address.optactive").html(html);
            initMagnificPopup();
        }
    });
});

// things to do after selecting address from shipping address list



// billing address radio buttons (in div)
$(document).on("click", ".billing-address", function() {
    if ($(this).attr("class") == "billing-address") {
        $(this).attr("class", "billing-address optactive");
        // assign the selected value in input
        $("#billing_address").attr("value", $(this).attr("value"));
    }
    // unselect others
    $(".billing-address").not($(this)).each(function() {
        $(this).attr("class", "billing-address");
    });
});
// billing address radio buttons (in div) end


// billing address radio buttons (in addresses list)
$(document).on("click", ".radio-opt.billing", function() {
    if ($(this).attr("class") == "radio-opt billing") {
        $(this).attr("class", "radio-opt billing optactive");
    }
    // unselect others
    $(".radio-opt.billing").not($(this)).each(function() {
        $(this).attr("class", "radio-opt billing");
    });
});
// billing address radio buttons (in addresses list) end


// things to do after selecting address from billing address list
$(document).on("click", ".billing-address-save", function() {
    $("#billing_address").attr("value", $(".radio-opt.billing.optactive").attr("value"));
    $(".jsxInline").magnificPopup("close");

    $.ajax({
        url: "/get-address/",
        type: "GET",
        data: {
            "id": $(".radio-opt.billing.optactive").attr("value")
        },
        success: function(response) {
            $(".billing-address.optactive").attr("value", response.data.id);
            html = response.data.receiver_name + " " + response.data.receiver_contact_number +
            "<address>" + response.data.address + ", " + response.data.city +
            "</address><a href='#chkBillingEdit' class='optedit jsxInline' data-effect='mfp-zoom-in'>Edit</a>"
            $(".billing-address.optactive").html(html);
            initMagnificPopup();
        }
    });
});
// things to do after selecting address from billing address list


// payment method radio buttons
$(document).on("click", ".radio-opt-amount", function() {
    if ($(this).attr("class") == "radio-opt-amount") {
        $(this).attr("class", "radio-opt-amount optactive");
        // assign the selected value in input
        $("#payment_option").attr("value", $(this).attr("value"));
    }
    // unselect others
    $(".radio-opt-amount").not($(this)).each(function() {
        $(this).attr("class", "radio-opt-amount");
    });
});
// payment method radio buttons end



// Add shipping & billing addresses
$("#shippingForm").on("submit", function(e) {
    e.preventDefault();

    const form = $(this);
    const url = form.attr("action");
	const data = Object.fromEntries(new FormData(e.target).entries());

	$.ajax({
		url: url,
		type: "POST",
		data: data,
		cache: false,
		success: function(response) {
			if (response.success == false) {
                $(".receiver_contact_number").text(response.message.receiver_contact_number);
            } else {
				form[0].reset();
				$(".receiver_contact_number").css("display", "none");
				Toastify({
                    text: response.message,
                    duration: 2000,
                    style: {background: "green"},
                }).showToast();
				setTimeout(function(){
					window.location.reload();
				}, 1000);
			}
		}
	});
});

// Add shipping & billing addresses end
