// Get current path
var currentPath = window.location.pathname;

// Get all links in the navigation menu
var navLinks = document.querySelectorAll('.nav-link');

// Checking and adding the "active" class for each link
navLinks.forEach(function(link) {
  if (link.getAttribute('href') === currentPath) {
    link.classList.add('active');
  }
});

/////////////////////////////////////////////////////////////////////////////////

window.addEventListener('scroll', function() {
  var scrollToTopBtn = document.getElementById('scrollToTopBtn');

  // Show the button when the page scrolls down
  if (window.pageYOffset > 100) {
      scrollToTopBtn.style.display = 'block';
  } else {
      scrollToTopBtn.style.display = 'none';
  }
});

document.getElementById('scrollToTopBtn').addEventListener('click', function() {
  // Smoothly scroll up the page
  window.scrollTo({
      top: 0,
      behavior: 'smooth'
  });
});


