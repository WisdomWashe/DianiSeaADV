document.addEventListener('DOMContentLoaded', function () {
  var toggle = document.querySelector('.nav-toggle');
  var nav = document.querySelector('.main-nav');

  if (toggle && nav) {
    toggle.addEventListener('click', function () {
      var isOpen = nav.classList.toggle('is-open');
      toggle.setAttribute('aria-expanded', isOpen ? 'true' : 'false');
    });

    nav.querySelectorAll('a').forEach(function (link) {
      link.addEventListener('click', function () {
        nav.classList.remove('is-open');
        toggle.setAttribute('aria-expanded', 'false');
      });
    });
  }

  // Auto-dismiss flash messages after a few seconds
  document.querySelectorAll('.flash').forEach(function (el) {
    setTimeout(function () {
      el.style.transition = 'opacity 0.4s ease, max-height 0.4s ease, padding 0.4s ease';
      el.style.opacity = '0';
      el.style.maxHeight = el.offsetHeight + 'px';
      requestAnimationFrame(function () {
        el.style.maxHeight = '0';
        el.style.padding = '0 20px';
      });
    }, 5000);
  });
});
