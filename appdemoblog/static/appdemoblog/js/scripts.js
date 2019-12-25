'use strict';

/**
 * 1. Featured Slider
 * 2. Footer Slider
 * 3. Search
 * 4. Menu Mobile
 */

(function ($) {

	$(document).ready(function () {

		/* 1. Featured Slider */
		var $featuredSlider = $('.featured-slider', '#featured-slider');

		if ($featuredSlider.length) {
			$featuredSlider.owlCarousel({
				items: 1,
				dots : false,
				nav: true,
				navText: ['<i class="fa fa-chevron-left"></i>', '<i class="fa fa-chevron-right"></i>'],
				responsive: {
					0: {
						dots: 0,
						autoplay: 0
					},
					768: {}
				},
				onInitialized: function () {


				}


			});
		}

		/* 2. Footer Slider */
		var $footerSlider = $('.owl-carousel', '#footer-instagram');

		if ($footerSlider.length) {
			$footerSlider.owlCarousel({
				items: 6,
				dots: 0,
				responsive: {
					0: {
						items: 3
					},
					600: {
						items: 4
					},
					991: {
						items: 6
					},
				}
			});
		}

		/* 3. Search */
		var $search = $('.search', '.socials');

		if ($search.length) {
			$search.on('click', function (e) {
				e.preventDefault();
				$search.toggleClass('active');
				$('#box-search').toggleClass('active');

				if ($search.hasClass('active')) {
					setTimeout(function () {
						$('input', '#box-search').focus();
					}, 50);
				}
			});
		}

		/* 4. Menu Mobile */
		var $menu = $('.menu-list'),
			$menuMobile = $('.menu-mobile'),
			$mainMenu = $('.main-menu'),
			$mobileCover = $('.mobile-cover');

		if ($menu.length) {
			$('.menu-item-has-children > a', $menu).on('click', function (e) {
				var ww = $(window).width(),
					$parent = $(this).closest('.menu-item-has-children');

				if ( ww <= 991) {
					e.preventDefault();
					$('> .sub-menu', $parent).slideToggle();
				}
			});
		}
		$menuMobile.on('click', function () {
			$mainMenu.addClass('active');
		});

		$mobileCover.on('click', function () {
			$mainMenu.removeClass('active');
		});
		$('.close-menu').on('click', function () {
			console.log(1);
			$mobileCover.trigger('click');
		});
		$(document).on('keydown', function (event) {
			if ($mainMenu.hasClass('active')) {
				if (event.keyCode === 27) {
					$mobileCover.trigger('click');
				}
			}
		})


		/* Header Small */
		$(window).on('scroll', function () {
			var scrollTop = $(window).scrollTop(),
				$header = $('#header');
			if (scrollTop > 10) {
				$header.addClass('header-small');
			}
			else {
				$header.removeClass('header-small');
			}
		});

		var $backToTop = $('.back-to-top');

		$backToTop.on('click', function () {
			$('html, body').animate({
				scrollTop: 0
			}, 500);
		});

		$(window).on('scroll', function () {
			var wt = $(window).scrollTop();

			if (wt > 500) {
				$backToTop.addClass('active');
			}
			else {
				$backToTop.removeClass('active');
			}
		});
	});
})(jQuery);