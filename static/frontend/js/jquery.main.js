jQuery(function () {
	initSvgSprite();
	initMenuOpener();
	initOpenClose();
	initInputNumber();
	initSlickSlider();
	initIonRangeSlider();
	initDroptoSelect();
	initMagnificPopup();
	// initSelect2();
	// initIonRangeSlider();
	// initStickyRoll();
	// initFixedScrollBlock();
	initIsotope();
	initTabs();
	// initSmoothScroll();
	initPreventEmptyAnchor();
});

// jQuery(document).ready(function(){
// 	setTimeout(function() {
// 		jQuery('.fullads').fadeOut('medium');
// 		jQuery('body').removeClass('adsactive');
// 	}, 8000);

// 	jQuery('.jsxFullads').click(function(){
// 		jQuery('.fullads').fadeOut('medium');
// 		jQuery('body').removeClass('adsactive');
// 	});
// });

// jQuery(".exp-play").click(function(ev){
// 	jQuery(".about__player iframe")[0].src += "?autoplay=1";
// 	jQuery(".about__player").addClass('playing');
// 	ev.preventDefault();
// });

function initIsotope() {
	// init Isotope
	var $grid = jQuery('.accountpanel__isocontent').isotope({
		itemSelector: '.order__item'
	});

	// store filter for each group
	var filters = {};

	jQuery('.accountpanel__isoset').on('click', 'button', function (event) {
		var $button = jQuery(event.currentTarget);
		// get group key
		var $buttonGroup = $button.parents('.button-group');
		var filterGroup = $buttonGroup.attr('data-filter-group');
		// set filter for group
		filters[filterGroup] = $button.attr('data-filter');
		// combine filters
		var filterValue = concatValues(filters);
		// set filter for Isotope
		$grid.isotope({
			filter: filterValue
		});
	});
	// change is-checked class on buttons
	$('.accountpanel__isoset').each(function (i, buttonGroup) {
		var $buttonGroup = $(buttonGroup);
		$buttonGroup.on('click', 'button', function () {
			$buttonGroup.find('.is-checked').removeClass('is-checked');
			$(this).addClass('is-checked');
		});
	});

	// flatten object by concatting values
	function concatValues(obj) {
		var value = '';
		for (var prop in obj) {
			value += obj[prop];
		}
		return value;
	}
}

function initSvgSprite() {
	jQuery("body").prepend(window.SVG_SPRITES.sprite);
}

function initPreventEmptyAnchor() {
	jQuery('a[href="#"]').click(function (e) {
		e.preventDefault();
	});
}

function initStickyRoll() {
	jQuery(".canvass__headline").stick_in_parent({
		parent: ".canvass"
	});

	jQuery(".productdraw__technical-headline").stick_in_parent({
		parent: ".productdraw__technical"
	});
}

function initFixedScrollBlock() {
	// var distance = $('#header').offset().top;

	jQuery(window).on("load scroll", function () {
		if (jQuery(window).scrollTop() > 0) {
			jQuery('#header').addClass("affix");
		} else {
			jQuery('#header').removeClass("affix");
		}
	});
}

function initDroptoSelect() {
	jQuery('.jsxUsrList a').click(function () {
		var scrl = jQuery(this).html();
		jQuery('.jsxUsrCtrl').html(scrl).removeClass('active');
		jQuery(this).parent('li').addClass('active').siblings().removeClass('active');
		jQuery('.jsxUsrList').slideUp();
	});

	jQuery('.jsxUsrCtrl').click(function () {
		jQuery(this).toggleClass('active');
		jQuery('.jsxUsrList').slideToggle();
	});
}

function initOpenClose() {
	jQuery('.jsxFaq').click(function () {
		jQuery(this).parents('.faq__item').toggleClass('faq--active');
		jQuery(this).siblings('.jsxFaqDetail').slideToggle();
	});

	jQuery('.jsxChkContinue').click(function () {
		jQuery(this).parents('li').removeClass('chkactive');
		jQuery(this).parents('.checkout__desc').slideUp();
		jQuery(this).parents('li').next('li').addClass('chkactive').find('.checkout__desc').slideDown();
	});

	jQuery('.jsxChkBack').click(function () {
		jQuery(this).parents('li').removeClass('chkactive');
		jQuery(this).parents('.checkout__desc').slideUp();
		jQuery(this).parents('li').prev('li').addClass('chkactive').find('.checkout__desc').slideDown();
	});
}

function initMenuOpener() {
	jQuery('.jsxHeadNav').click(function () {
		jQuery('body').toggleClass('nav-active');
	});

	jQuery('.jsxHeadSearch').click(function () {
		jQuery('body').toggleClass('search-active');
		jQuery('.siteheader__search').slideToggle();
	});

	jQuery('.jsxHeadSurge').click(function () {
		jQuery('body').toggleClass('surge-active');
		jQuery('.surge-hd-drop').slideToggle();
	});

	jQuery('.jsxViewFilter').click(function () {
		jQuery('body').toggleClass('filter-active');
	});

	jQuery('.jsxViewGrid').click(function () {
		jQuery('.filter__showcase').addClass('gridshot').removeClass('listshot');
		jQuery(this).parent().addClass('active').siblings().removeClass('active');
	});

	jQuery('.jsxViewList').click(function () {
		jQuery('.filter__showcase').addClass('listshot').removeClass('gridshot');
		jQuery(this).parent().addClass('active').siblings().removeClass('active');
	});

	jQuery('.jsxViewSort').click(function () {
		jQuery(this).parents('.sortbox').toggleClass('sortactive');
		jQuery(this).siblings('ul').slideToggle();
	});

	// jQuery('.jsxTileMore').click(function() {
	// 	jQuery(this).siblings('.filter__form--more').slideToggle();
	// 	jQuery(this).html(jQuery(this).html() == 'Show More' ? 'Show Less' : 'Show More');
	// });


	// jQuery('.jsxCatTgr').click(function() {
	// 	jQuery('body, .header__tool').toggleClass('cat-active');
	// 	jQuery('.megadrop').slideToggle();
	// 	jQuery('body').removeClass('compare-active account-active');
	// });

	// jQuery('.jsxFooCompare').click(function() {
	// 	jQuery('body').toggleClass('compare-active');
	// 	jQuery('body').removeClass('cat-active account-active');
	// 	jQuery('.header__tool').removeClass('cat-active');
	// });

	// jQuery('.jsxAccountTgr').click(function() {
	// 	jQuery('body').toggleClass('account-active');
	// 	jQuery('body').removeClass('cat-active compare-active');
	// 	jQuery('.header__tool').removeClass('cat-active');
	// });

	// jQuery('.jsxSignUp').click(function() {
	// 	jQuery('.header__tool').toggleClass('login-active');
	// 	jQuery('#jsxLogindrop').slideToggle();
	// });

	// jQuery('#drpViewPwd').click(function() {
	// 	jQuery(this).toggleClass('pwdactive');
	// 	jQuery('#drpPassword').attr('type', function(index, attr){
	// 		return attr == 'password' ? 'text' : 'password';
	// 	});
	// });

	// jQuery('.jsxViewPwd').click(function() {
	// 	jQuery(this).toggleClass('pwdactive');
	// 	jQuery(this).siblings('.form-set').children('.jsxPwd').attr('type', function(index, attr){
	// 		return attr == 'password' ? 'text' : 'password';
	// 	});
	// });

	// jQuery('.jsxToastClose').click(function() {
	// 	jQuery(this).parents('.toast').fadeOut();
	// });

	// jQuery(window).scroll(function () {
	// 	if(jQuery(window).scrollTop() >= 100) {
	// 		jQuery('.jsxScrollUp').fadeIn();
	// 	} else {
	// 		jQuery('.jsxScrollUp').fadeOut();
	// 	}
	// });

	// jQuery(".jsxScrollUp").click(function() {
	// 	jQuery('html, body').animate({
	// 		scrollTop: 0
	// 	}, 1000);
	// });


	// if(jQuery('.jsxAdvfilter-tgr').length) {
	// 	jQuery('.jsxAdvfilter-tgr').click(function() {
	// 		var text = $(this).html();
	// 		jQuery(this).html(text == "Hide Filter" ? "Advanced Filter" : "Hide Filter");
	// 		jQuery('.form-advanced').slideToggle();
	// 	});
	// }

	// jQuery(".jsxViewGrid").click(function() {
	// 	jQuery(this).parent('li').siblings().removeClass('active');
	// 	jQuery(this).parent('li').addClass('active');
	// 	jQuery('.filter__set .filter__showcase').addClass('gridshow').removeClass('listshow');
	// });

	// jQuery(".jsxViewList").click(function() {
	// 	jQuery(this).parent('li').siblings().removeClass('active');
	// 	jQuery(this).parent('li').addClass('active');
	// 	jQuery('.filter__set .filter__showcase').addClass('listshow').removeClass('gridshow');
	// });

	// jQuery(".jsxSortBy").click(function() {
	// 	jQuery('.filter__bar-sortdrop').slideToggle();
	// });

	// jQuery(".jsxFiMoreTgr").click(function() {
	// 	jQuery(this).html(jQuery(this).html() == "Show Less" ? "Show More" : "Show Less");
	// 	jQuery('.jsxfimoreshow').slideToggle();
	// });

	// jQuery(".jsxFilterOpn").click(function() {
	// 	jQuery('body').toggleClass('filter-active');
	// });

	// jQuery(".jsxCompareClose").click(function() {
	// 	jQuery(this).parent('.compare__unit-block').hide();
	// 	jQuery(this).parent('.compare__unit-block').siblings('.form-compare').show();
	// });

	// jQuery('.jsxOpenTgr').click(function() {
	// 	jQuery(this).parents('.canvass__info').toggleClass('jsxshow');
	// 	jQuery(this).parent('.canvass__info-title').siblings('.jsxCollapse').slideToggle();
	// });

	// jQuery('#jsxCmntOpnr').click(function() {
	// 	jQuery('#jsxCommentForm').slideDown();
	// 	jQuery(this).fadeOut();
	// });

	// jQuery('#jsxCmntCls').click(function() {
	// 	jQuery('#jsxCommentForm').slideUp();
	// 	jQuery('#jsxCmntOpnr').fadeIn();
	// });



	// if(jQuery('.site-navdropper>ul>li').children('ul').length) {
	// 	.addClass('has-dropdown')
	// };
	// jQuery('.site-navdropper>ul>li').each(function () {
	// 	if(jQuery(this).children('ul').length) {
	// 		jQuery(this).addClass('has-drop');
	// 	}
	// });

	// jQuery(document).click(function(event) {
	// 	if (!jQuery(event.target).closest(".megamenu > .dropdown, .dropdown .dropdown-menu").length) {
	// 		jQuery(".megamenu > .dropdown").removeClass('drop-active');
	// 	}
	// });
}

function initSelect2() {
	jQuery(".jsxselect2 select").select2();
	jQuery(".compare__gear .jsxselect2 select").select2({
		dropdownParent: jQuery('#pgComparePanel')
	});
}

// function initIonRangeSlider() {
// 	function numberWithCommas(x) {
// 		return x.toString().replace(/(\d)(?=(\d\d)+\d$)/g, "$1,");
// 	}

// 	var $range = $("#searchRange");
// 	var $inputFrom = $("#searchRange_input_from");
// 	var $inputTo = $("#searchRange_input_to");
// 	var instance;
// 	var min = 0;
// 	var max = 30000;
// 	var from = 2500;
// 	var to = 10000;

// 	jQuery(".jsxIrsRange input").ionRangeSlider({
// 		skin: "round",
// 		type: "double",
// 		min: min,
// 		max: max,
// 		from: from,
// 		to: to,
// 		prefix: "Rs.",
// 		force_edges: true,
// 		prettify_enabled: true,
// 		prettify_separator: ",",
// 		prettify: numberWithCommas,
// 		onStart: updateInputs,
// 		onChange: updateInputs,
// 		onFinish: updateInputs
// 	});

// 	instance = $range.data("ionRangeSlider");

// 	function updateInputs (data) {
// 		from = data.from;
// 		to = data.to;
// 		$inputFrom.prop("value", from);
// 		$inputTo.prop("value", to);
// 	}

// 	$inputFrom.on("change", function () {
// 		var val = $(this).prop("value");

// 		// validate
// 		if (val < min) {
// 			val = min;
// 		} else if (val > to) {
// 			val = to;
// 		}

// 		instance.update({
// 			from: val
// 		});

// 		$(this).prop("value", val);

// 	});

// 	$inputTo.on("change", function () {
// 		var val = $(this).prop("value");

// 		// validate
// 		if (val < from) {
// 			val = from;
// 		} else if (val > max) {
// 			val = max;
// 		}

// 		instance.update({
// 			to: val
// 		});

// 		$(this).prop("value", val);
// 	});
// }


// function initTabs() {
// 	jQuery('.upshot__fullinfo-head button').click(function(){
// 		var tab_id = jQuery(this).attr('data-tab');
// 		jQuery(this).parent('li').addClass('active');
// 		jQuery(this).parent().siblings().removeClass('active');
// 		jQuery('.upshot__fullinfo-tabbox .tabitem').removeClass('active').hide();
// 		jQuery("#"+tab_id).addClass('active').show();
// 	});

// 	jQuery('.productdraw__structure-label button').click(function(){
// 		var tab_id = jQuery(this).attr('data-tab');
// 		jQuery(this).parent('li').addClass('gal-active');
// 		jQuery(this).parent().siblings().removeClass('gal-active');
// 		jQuery('.productdraw__structure-tabblock').removeClass('gal-active').hide();
// 		jQuery("#"+tab_id).addClass('gal-active').show();
// 	});

// 	jQuery('.pointing-list button').click(function(){
// 		var tab_id = jQuery(this).attr('data-tab');
// 		jQuery(this).parent('li').addClass('point-active');
// 		jQuery(this).parent().siblings().removeClass('point-active');
// 		jQuery('.pointab-data').removeClass('point-active').hide();
// 		jQuery("#"+tab_id).addClass('point-active').show();
// 	});
// }

function initIonRangeSlider() {
	function numberWithCommas(x) {
		return x.toString().replace(/(\d)(?=(\d\d)+\d$)/g, "$1,");
	}



	var $range = $("#searchRange");
	var $inputFrom = $("#searchRange_input_from");
	var $inputTo = $("#searchRange_input_to");
	var instance;

	var min = $inputFrom.val();
	var max = $inputTo.val();

	var from = $inputFrom.val();
	var to = $inputTo.val();
	// alert($inputFrom.dataset.value)
	if ($inputFrom.dataset){
		alert($inputFrom.dataset)
		from = $inputFrom.dataset.value;
	}

	// if ($inputTo.dataset.value){
	// 	to = $inputFrom.dataset.value;
	// }

	jQuery(".jsxIrsRange input").ionRangeSlider({
		skin: "round",
		type: "double",
		min: min,
		max: max,
		from: from,
		to: to,
		prefix: "$",
		force_edges: true,
		prettify_enabled: true,
		prettify_separator: ",",
		prettify: numberWithCommas,
		onStart: updateInputs,
		onChange: updateInputs,
		onFinish: updateInputs
	});

	instance = $range.data("ionRangeSlider");

	function updateInputs(data) {
		from = data.from;
		to = data.to;
		$inputFrom.prop("value", from);
		$inputTo.prop("value", to);
	}

	$inputFrom.on("change", function () {
		var val = $(this).prop("value");

		// validate
		if (val < min) {
			val = min;
		} else if (val > to) {
			val = to;
		}

		instance.update({
			from: val
		});

		$(this).prop("value", val);

	});

	$inputTo.on("change", function () {
		var val = $(this).prop("value");

		// validate
		if (val < from) {
			val = from;
		} else if (val > max) {
			val = max;
		}

		instance.update({
			to: val
		});

		$(this).prop("value", val);
	});
}

function initSlickSlider() {
	// if(jQuery(".jsxSortPanelGlide").length) {
	// 	jQuery('.jsxSortPanelGlide').slick({
	// 		mobileFirst: true,
	// 		slidesToShow: 2,
	// 		slidesToScroll: 1,
	// 		autoplay: true,
	// 		autoplaySpeed: 5000,
	// 		responsive: [
	// 		{
	// 			breakpoint: 575,
	// 			settings: {
	// 				slidesToShow: 3,
	// 				slidesToScroll: 1
	// 			}
	// 		},
	// 		{
	// 			breakpoint: 767,
	// 			settings: {
	// 				slidesToShow: 4,
	// 				slidesToScroll: 1
	// 			}
	// 		},
	// 		{
	// 			breakpoint: 991,
	// 			settings: {
	// 				slidesToShow: 5,
	// 				slidesToScroll: 1
	// 			}
	// 		},
	// 		{
	// 			breakpoint: 1199,
	// 			settings: {
	// 				slidesToShow: 7,
	// 				slidesToScroll: 1
	// 			}
	// 		}
	// 		]
	// 	});
	// }

	if (jQuery(".jsxBaseSlider").length) {
		jQuery('.jsxBaseSlider').slick({
			slidesToShow: 1,
			slidesToScroll: 1,
			autoplay: true,
			autoplaySpeed: 3000,
			dots: true
		});
	}

	if (jQuery(".jsxShowDisplay").length) {
		jQuery('.jsxShowDisplay').slick({
			slidesToShow: 1,
			slidesToScroll: 1,
			fade: true,
			asNavFor: '.jsxShowPagination'
		});
		jQuery('.jsxShowPagination').slick({
			mobileFirst: true,
			slidesToShow: 4,
			slidesToScroll: 1,
			asNavFor: '.jsxShowDisplay',
			focusOnSelect: true,
			responsive: [{
				breakpoint: 991,
				settings: {
					slidesToShow: 4,
					slidesToScroll: 1,
					vertical: true
				}
			}]
		});
	}

	if (jQuery(".jsxProductGlide").length) {
		jQuery('.jsxProductGlide').slick({
			mobileFirst: true,
			slidesToShow: 1,
			slidesToScroll: 1,
			autoplay: true,
			autoplaySpeed: 5000,
			responsive: [{
					breakpoint: 575,
					settings: {
						slidesToShow: 2,
						slidesToScroll: 1
					}
				},
				{
					breakpoint: 767,
					settings: {
						slidesToShow: 3,
						slidesToScroll: 1
					}
				},
				{
					breakpoint: 991,
					settings: {
						slidesToShow: 4,
						slidesToScroll: 1
					}
				}
			]
		});
	}

	// if(jQuery(".jsxBrandLineGlide").length) {
	// 	jQuery('.jsxBrandLineGlide').slick({
	// 		mobileFirst: true,
	// 		slidesToShow: 2,
	// 		slidesToScroll: 1,
	// 		autoplay: true,
	// 		autoplaySpeed: 5000,
	// 		responsive: [
	// 		{
	// 			breakpoint: 575,
	// 			settings: {
	// 				slidesToShow: 4,
	// 				slidesToScroll: 1
	// 			}
	// 		},
	// 		{
	// 			breakpoint: 991,
	// 			settings: {
	// 				slidesToShow: 6,
	// 				slidesToScroll: 1
	// 			}
	// 		}
	// 		]
	// 	});
	// }

	// if(jQuery(".jsxShowCaseGlide").length) {
	// 	jQuery('.jsxShowCaseGlide').slick({
	// 		mobileFirst: true,
	// 		slidesToShow: 1,
	// 		slidesToScroll: 1,
	// 		autoplay: true,
	// 		autoplaySpeed: 5000,
	// 		responsive: [
	// 		{
	// 			breakpoint: 575,
	// 			settings: {
	// 				slidesToShow: 2,
	// 				slidesToScroll: 1
	// 			}
	// 		},
	// 		{
	// 			breakpoint: 767,
	// 			settings: {
	// 				slidesToShow: 3,
	// 				slidesToScroll: 1
	// 			}
	// 		},
	// 		{
	// 			breakpoint: 991,
	// 			settings: {
	// 				slidesToShow: 4,
	// 				slidesToScroll: 1
	// 			}
	// 		}
	// 		]
	// 	});
	// }
}

// input type number
function initInputNumber() {
	jQuery('<span class="qty-control"><button type="button" class="qty-btn qty-up">+</button><button type="button" class="qty-btn qty-down">-</button></span>').insertAfter('input[type="number"]');
	jQuery('.form-number').each(function () {
		countSpinner(this);
	});
}

function countSpinner(control) {
	var spinner = jQuery(control),
		input = spinner.find('input[type="number"]'),
		btnUp = spinner.find('.qty-up'),
		btnDown = spinner.find('.qty-down'),
		step = input.attr('step'),
		min = input.attr('min'),
		max = input.attr('max');

	if (typeof step === "undefined") {
		step = 1;
	}

	btnUp.click(function () {
		var oldValue = parseFloat(input.val());
		if (isNaN(oldValue)) {
			var newVal = parseInt(min) + parseInt(step);
		} else if (oldValue >= max) {
			var newVal = oldValue;
		} else {
			var newVal = parseInt(oldValue) + parseInt(step);
			if (newVal >= max) {
				newVal = max;
			}
		}
		spinner.find("input").val(newVal);
		spinner.find("input").trigger("change");
	});

	btnDown.click(function () {
		var oldValue = parseFloat(input.val());
		if (isNaN(oldValue)) {
			var newVal = min;
		} else if (oldValue <= min) {
			var newVal = oldValue;
		} else {
			var newVal = parseInt(oldValue) - parseInt(step);
			if (newVal <= min) {
				newVal = min;
			}
		}
		spinner.find("input").val(newVal);
		spinner.find("input").trigger("change");
	});

	// disable mousewheel on a input number field when in focus
	// (to prevent Cromium browsers change the value when scrolling)
	jQuery('form').on('focus', 'input[type=number]', function (e) {
		jQuery(this).on('mousewheel.disableScroll', function (e) {
			e.preventDefault()
		})
	})
	jQuery('form').on('blur', 'input[type=number]', function (e) {
		jQuery(this).off('mousewheel.disableScroll')
	})
}

// Cache selectors
var lastId,
	topMenu = jQuery(".productdraw__technical-headlinelist"),
	topMenuHeight = topMenu.outerHeight() + 15,
	// All list items
	menuItems = topMenu.find("a"),
	// Anchors corresponding to menu items
	scrollItems = menuItems.map(function () {
		var item = $($(this).attr("href"));
		if (item.length) {
			return item;
		}
	});

// Bind click handler to menu items
// so we can get a fancy scroll animation
menuItems.click(function (e) {
	var href = $(this).attr("href"),
		offsetTop = href === "#" ? 0 : $(href).offset().top - topMenuHeight + 1;
	$('html, body').stop().animate({
		scrollTop: offsetTop
	}, 800);
	e.preventDefault();
});

// Bind to scroll
$(window).scroll(function () {
	// Get container scroll position
	var fromTop = $(this).scrollTop() + topMenuHeight;

	// Get id of current scroll item
	var cur = scrollItems.map(function () {
		if ($(this).offset().top < fromTop)
			return this;
	});
	// Get the id of the current element
	cur = cur[cur.length - 1];
	var id = cur && cur.length ? cur[0].id : "";

	if (lastId !== id) {
		lastId = id;
		// Set/remove active class
		menuItems
			.parent().removeClass("active")
			.end().filter("[href='#" + id + "']").parent().addClass("active");
	}
});

function initSmoothScroll() {
	// direct browser to top right away
	// var headerHeight = jQuery('#header').height();
	var headerHeight = 0;

	if (window.location.hash) {
		scroll(0, 0);
	}

	// takes care of some browsers issue
	setTimeout(function () {
		scroll(0, 0);
	}, 1);

	// if we have anchor on the url (calling from other page)
	if (window.location.hash) {
		// smooth scroll to the anchor id
		jQuery('html,body').animate({
			scrollTop: jQuery(window.location.hash).offset().top - headerHeight + 'px'
		}, 1000, 'swing');
	}
	// if(!jQuery('[id*="pgroll"]').length) {
	//your current click function
	// jQuery('.scroll').on('click',function(e){
	// 	console.log(4);
	// 	e.preventDefault();
	// 	jQuery('html,body').animate({
	// 		scrollTop:jQuery(jQuery(this).attr('href')).offset().top + 'px'
	// 	},1000,'swing');
	// });
	// }

	if (jQuery('[id*="pgroll"]').length) {
		// jQuery(document).on("scroll", onScroll);
		//smoothscroll
		jQuery('a[href*="#pgroll"]').on('click', function (e) {
			e.preventDefault();
			jQuery(document).off("scroll");

			jQuery('a').each(function () {
				jQuery(this).removeClass('active');
			})
			jQuery(this).addClass('active');

			var target = this.hash,
				menu = target;
			$target = jQuery(target);
			jQuery('html, body').stop().animate({
				'scrollTop': $target.offset().top - headerHeight + 'px'
			}, 1000, 'swing');
			// }, 1000, 'swing', function () {
			// 	window.location.hash = target;
			// 	jQuery(document).on("scroll", onScroll);
			// }
		});
	}
}

function onScroll(event) {
	var scrollPos = jQuery(document).scrollTop();
	jQuery('#menu-center a').each(function () {
		var currLink = jQuery(this);
		var refElement = jQuery(currLink.attr("href"));
		if (refElement.position().top <= scrollPos && refElement.position().top + refElement.height() > scrollPos) {
			jQuery('#menu-center ul li a').removeClass("active");
			currLink.addClass("active");
		} else {
			currLink.removeClass("active");
		}
	});
}

function initMagnificPopup() {
	// single popup
	jQuery('.jsxPopupSingle').magnificPopup({
		type: 'image',
		closeOnContentClick: true,
		image: {
			verticalFit: false,
			tError: 'The image could not be loaded.',
		},
		removalDelay: 500, //delay removal by X to allow out-animation
		callbacks: {
			beforeOpen: function () {
				// just a hack that adds mfp-anim class to markup
				this.st.image.markup = this.st.image.markup.replace('mfp-figure', 'mfp-figure mfp-with-anim');
				this.st.mainClass = this.st.el.attr('data-effect');
			}
		},
		midClick: true
	});

	// gallery popup
	jQuery('.jsxPopupGallery').magnificPopup({
		delegate: 'a',
		type: 'image',
		tLoading: 'Loading image #%curr%...',
		mainClass: 'mfp-img-mobile',
		gallery: {
			enabled: true,
			navigateByImgClick: true,
			preload: [0, 1] // Will preload 0 - before current, and 1 after the current image
		},
		image: {
			tError: 'The image could not be loaded.',
		},
		removalDelay: 500, //delay removal by X to allow out-animation
		callbacks: {
			beforeOpen: function () {
				// just a hack that adds mfp-anim class to markup
				this.st.image.markup = this.st.image.markup.replace('mfp-figure', 'mfp-figure mfp-with-anim');
				this.st.mainClass = this.st.el.attr('data-effect');
			}
		},
		midClick: true
	});

	// inline popup
	jQuery('.jsxInline').magnificPopup({
		// fixedBgPos: true,
		// fixedContentPos: false,
		type: 'inline',
		overflowY: 'auto',
		closeBtnInside: true,
		preloader: false,
		midClick: true,
		removalDelay: 500,
		mainClass: 'mfp-inline',
		closeMarkup: '<button title="%title%" type="button" class="mfp-close"><span class="icon-close"></span></button>',
		callbacks: {
			beforeOpen: function () {
				this.st.mainClass = this.st.el.attr('data-effect');
			}
		}
	});

	jQuery('.jsxFrame').magnificPopup({
		disableOn: 700,
		type: 'iframe',
		mainClass: 'mfp-fade',
		removalDelay: 400,
		preloader: false,
		fixedContentPos: false,
		iframe: {
			markup: '<div class="mfp-iframe-scaler">' +
				'<div class="mfp-close"></div>' +
				'<iframe class="mfp-iframe" src="//about:blank" frameborder="0" allowfullscreen allow="autoplay"></iframe>' +
				'</div>',
			patterns: {
				youtube: {
					index: 'youtube.com',
					id: 'v=',
					src: 'https://www.youtube.com/embed/%id%?rel=0&autoplay=1&muted=1',
					allow: 'autoplay'
				}
			}
		},
	});
}
