document.addEventListener('DOMContentLoaded', () => {

	let = searchWrapper = document.querySelector('.search-wrapper');
	let = mobileMenu = document.querySelector('.mobile-menu-wrap');

	// Open Search
	document.querySelectorAll('.header-search-btn').forEach(el => el.addEventListener('click', function() {
		searchWrapper.classList.add('is-active');
	}));
	

	// Close Search
	document.querySelector('.search-close').addEventListener('click', function() {
		searchWrapper.classList.remove('is-active');
	});

	// Open Mobile Menu
	document.querySelector('.hamburger').addEventListener('click', function() {
		mobileMenu.classList.add('is-active');
	});

	// Close Mobile Menu
	document.querySelector('.mobile-close').addEventListener('click', function() {
		mobileMenu.classList.remove('is-active');
	});
	
})